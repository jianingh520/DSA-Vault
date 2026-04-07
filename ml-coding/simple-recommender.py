import math
from collections import defaultdict
from typing import List, Dict, Any


class RecommenderSystem:
    """
    Item-based collaborative filtering recommender.

    Similarity:  cosine distance over co-raters only,
                 scaled by log(num_co_raters + 1) for confidence weighting.
    Prediction:  weighted average of similarities to already rated items.
    Ranking:     items sorted by predicted rating descending.

    load_ratings:        O(r)       r = number of ratings
    _cosine_similarity:  O(u)       u = number of co-raters
    predict_rating:      O(s)       s = number of items user has rated
    recommend:           O(s * i)   i = total unique items

    Space: O(r) for both indexes combined
    """

    def __init__(self):
        # user -> {item -> rating}
        # defaultdict(dict): accessing a new user auto-creates an empty dict
        self.user_items: Dict[str, Dict[str, float]] = defaultdict(dict)
        # item -> {user -> rating}
        self.item_users: Dict[str, Dict[str, float]] = defaultdict(dict)
        self.global_avg: float = 0.0

    def load_ratings(self, ratings: List[Dict[str, Any]]) -> "RecommenderSystem":
        """
        Build both indexes in one pass from a flat list of rating dicts.
        Each rating: {"user_id": str, "item_id": str, "rating": float}
        Returns self for method chaining.

        Before defaultdict:
            if user not in self.user_items:
                self.user_items[user] = {}
            self.user_items[user][item] = rating
        After defaultdict:
            self.user_items[user][item] = rating
            (missing key auto-creates empty dict on first access)
        """
        for r in ratings:
            user   = r["user_id"]
            item   = r["item_id"]
            rating = float(r["rating"])

            self.user_items[user][item] = rating
            self.item_users[item][user] = rating

        # compute global average across all ratings
        all_ratings = [
            rating
            for user_ratings in self.user_items.values()
            for rating in user_ratings.values()
        ]
        self.global_avg = sum(all_ratings) / len(all_ratings)

        return self

    def _cosine_similarity(self, item_a: str, item_b: str) -> float:
        """
        Cosine similarity between two items using co-raters only.
        Co-rater: a user who has rated BOTH items.

        Scaled by log(num_co_raters + 1) for confidence weighting.
        Why +1: avoids log(1)=0 zeroing out single co-rater pairs entirely.
            1 co-rater   -> log(2)   = 0.69  discounted but not erased
            10 co-raters -> log(11)  = 2.4   reasonably trusted
            100 co-raters -> log(101) = 4.6  highly trusted

        Returns 0.0 if no co-raters exist or either item is unknown.

        Time: O(u)  u = number of co-raters
        """
        if item_a not in self.item_users or item_b not in self.item_users:
            return 0.0

        raters_a  = set(self.item_users[item_a].keys())
        raters_b  = set(self.item_users[item_b].keys())
        co_raters = raters_a & raters_b   # set intersection: rated both items

        if len(co_raters) == 0:
            return 0.0

        # build rating vectors from co-raters only
        # non-co-raters excluded to avoid treating missing ratings as 0
        vec_a = [self.item_users[item_a][u] for u in co_raters]
        vec_b = [self.item_users[item_b][u] for u in co_raters]

        dot   = sum(a * b for a, b in zip(vec_a, vec_b))
        mag_a = sum(a * a for a in vec_a) ** 0.5
        mag_b = sum(b * b for b in vec_b) ** 0.5

        if mag_a == 0 or mag_b == 0:
            return 0.0

        cos_sim = dot / (mag_a * mag_b)
        return cos_sim * math.log(len(co_raters) + 1)

    def predict_rating(self, user_id: str, item_id: str) -> float:
        """
        Predict the rating a user would give an unseen item.

        Formula: weighted average of similarities to already rated items.
            numerator   = sum(similarity * user_rating)
            denominator = sum(similarity)
            prediction  = numerator / denominator

        Why divide by sum of similarities:
            Normalizes result back into rating scale regardless of
            how many rated items contributed. Without it, users with
            more rated items always produce inflated raw scores.

        Returns 0.0 for cold start or no similar items found.

        Time: O(s)  s = number of items the user has rated
        """
        if user_id not in self.user_items:
            return self.global_avg
            # 0.0   # cold start: no history
            
        if item_id not in self.item_users:
            return self.global_avg   # brand new item, use global average
            # 0.0   # unknown item

        rated = self.user_items[user_id]

        numerator   = 0.0
        denominator = 0.0

        for seen_item, user_rating in rated.items():
            sim = self._cosine_similarity(seen_item, item_id)
            if sim <= 0:
                continue
            numerator   += sim * user_rating
            denominator += sim

        if denominator == 0:
            return 0.0   # no similar rated items found

        return numerator / denominator

    def recommend(self, user_id: str, top_n: int = 5) -> List[str]:
        """
        Recommend top_n unrated items ranked by predicted rating.

        Flow:
            1. find all items the user has not yet rated
            2. predict a rating for each candidate
            3. sort by predicted rating descending
            4. return top_n item ids

        Returns empty list for cold start or user rated every item.

        Time: O(s * i)  s = items user rated, i = total unique items
        """
        if user_id not in self.user_items:
            return []   # cold start

        rated   = self.user_items[user_id]
        unrated = set(self.item_users.keys()) - set(rated.keys())

        # defaultdict(float): missing candidate auto-initializes to 0.0
        predictions: Dict[str, float] = defaultdict(float)
        for candidate in unrated:
            score = self.predict_rating(user_id, candidate)
            if score > 0:
                predictions[candidate] = score

        ranked = sorted(predictions.keys(),
                        key=lambda x: predictions[x],
                        reverse=True)
        return ranked[:top_n]


# ── TEST CASES ────────────────────────────────────────────────────────────

def test_recommender():

    ratings = [
        {"user_id": "alice", "item_id": "action1", "rating": 5.0},
        {"user_id": "alice", "item_id": "comedy1", "rating": 3.0},
        {"user_id": "alice", "item_id": "drama1",  "rating": 4.0},
        {"user_id": "bob",   "item_id": "comedy1", "rating": 4.0},
        {"user_id": "bob",   "item_id": "drama1",  "rating": 4.0},
        {"user_id": "carol", "item_id": "action1", "rating": 4.0},
        {"user_id": "carol", "item_id": "action2", "rating": 5.0},
    ]

    rec = RecommenderSystem().load_ratings(ratings)

    # Both indexes built correctly in one pass
    assert rec.user_items["alice"]["action1"] == 5.0
    assert rec.item_users["comedy1"]["bob"]   == 4.0
    assert rec.item_users["drama1"]["alice"]  == 4.0

    # Cosine similarity: action1 and action2 share carol as co-rater
    sim = rec._cosine_similarity("action1", "action2")
    assert sim > 0.0, "shared co-rater should give positive similarity"

    # Cosine similarity: no co-raters means similarity is 0
    sim_none = rec._cosine_similarity("action2", "comedy1")
    assert sim_none == 0.0, "no co-raters should give 0 similarity"

    # predict_rating: alice loved action1 (5.0), action2 is similar to action1
    pred = rec.predict_rating("alice", "action2")
    assert pred > 0.0
    assert 1.0 <= pred <= 5.0, "predicted rating should stay in rating scale"

    # predict_rating: cold start user returns 0.0
    assert rec.predict_rating("new_user", "action2") == 0.0

    # predict_rating: unknown item returns 0.0
    assert rec.predict_rating("alice", "unknown_item") == 0.0

    # predict_rating: item with no co-raters to any rated item returns 0.0
    ratings2 = [
        {"user_id": "alice", "item_id": "action1", "rating": 5.0},
        {"user_id": "bob",   "item_id": "isolated", "rating": 3.0},
    ]
    rec2 = RecommenderSystem().load_ratings(ratings2)
    assert rec2.predict_rating("alice", "isolated") == 0.0

    # recommend: alice only unrated item is action2, should appear in results
    recs_alice = rec.recommend("alice", top_n=3)
    assert "action2" in recs_alice

    # recommend: results sorted by predicted rating descending
    recs_bob = rec.recommend("bob", top_n=5)
    if len(recs_bob) > 1:
        scores = [rec.predict_rating("bob", item) for item in recs_bob]
        assert scores == sorted(scores, reverse=True), "must be sorted descending"

    # recommend: cold start returns empty list
    assert rec.recommend("new_user") == []

    # recommend: user who rated every item returns empty list
    ratings3 = [
        {"user_id": "x", "item_id": "a", "rating": 5.0},
        {"user_id": "y", "item_id": "a", "rating": 4.0},
    ]
    rec3 = RecommenderSystem().load_ratings(ratings3)
    assert rec3.recommend("x") == []

    print("All Recommender tests passed")


test_recommender()