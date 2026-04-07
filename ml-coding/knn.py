"""
KNN stands for K-Nearest Neighbors. Given a new point you want to classify, you look at the k closest points in your training data and take a majority vote on their labels. The new point gets the label that appears most among its k nearest neighbors.
That is the entire algorithm. There is no training in the traditional sense. You just store the data and do all the work at prediction time.

"""

import math
import heapq
from typing import List, Any


class KNNClassifier:
    """
    K-Nearest Neighbors classifier.

    fit:     Time O(1), Space O(n*d)
    predict: Time O(m · (n·d + n log k))  — heap is faster than sort; Space O(k) for heap
    dist: Time O(d), Space O(1)

    Space:   O(n·d) training data + O(k) heap + O(m) for output list
    """

    def __init__(self, k: int = 3, distance: str = "euclidean"):
        # if k < 1:
        #     raise ValueError("k must be at least 1")
        self.k = k
        if distance == "euclidean":
            self._dist_fn = self._euclidean
        elif distance == "cosine":
            self._dist_fn = self._cosine
        # else:
        #     raise ValueError(f"Unknown distance: {distance}")
        self.X_train = None
        self.y_train = None

    def _euclidean(self, a: List[float], b: List[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def _cosine(self, a: List[float], b: List[float]) -> float:
        dot   = sum(x * y for x, y in zip(a, b))
        mag_a = math.sqrt(sum(x ** 2 for x in a))
        mag_b = math.sqrt(sum(y ** 2 for y in b))
        if mag_a == 0 or mag_b == 0:
            return 1.0
        return 1.0 - dot / (mag_a * mag_b)

    def fit(self, X: List[List[float]], y: List[Any]) -> None:
        # if len(X) != len(y):
        #     raise ValueError("X and y must have same length")
        # if len(X) < self.k:
        #     raise ValueError(f"Not enough training points for k={self.k}")
        self.X_train = X
        self.y_train = y

    def predict(self, X_test: List[List[float]]) -> List[Any]:
        """
        calls _predict_one once per test point.
        For m test points: Time O(m * (nd + nlogk)) 
        """
        # if self.X_train is None:
        #     raise RuntimeError("Call fit() before predict()")
        return [self._predict_one(x) for x in X_test]

    def _predict_one(self, x: List[float]) -> Any:
        """
        Use max-heap of size k to track k closest neighbors.
        Avoids full sort: O(n log k) instead of O(n log n).
        Negate distance because Python heapq is a min-heap.

        time: O(n * (d + logk)) -> O(nd + nlogk)
        """
        heap = []

        for xt, yt in zip(self.X_train, self.y_train):
            dist = self._dist_fn(x, xt)
            heapq.heappush(heap, (-dist, yt))
            if len(heap) > self.k:
            	heapq.heappop(heap)

        # manual vote count. time O(k)
        votes = {}
        for _, label in heap:
            votes[label] = 1 + votes.get(label, 0)

        # best vote. time O(k)
        best_label = None
        best_count = 0
        for label, count in votes.items():
            if count > best_count:
                best_count = count
                best_label = label

        return best_label


# ── TEST CASES ────────────────────────────────────────────────────────────

def test_knn():

    X = [[1,1],[1,2],[2,1],[8,8],[9,8],[8,9]]
    y = ['A','A','A','B','B','B']
    knn = KNNClassifier(k=3)
    knn.fit(X, y)

    assert knn.predict([[1,1]]) == ['A']
    assert knn.predict([[9,9]]) == ['B']
    assert knn.predict([[1,1],[9,9]]) == ['A','B']

    # k=1
    knn1 = KNNClassifier(k=1)
    knn1.fit([[0,0],[10,10]], ['X','Y'])
    assert knn1.predict([[1,1]]) == ['X']
    assert knn1.predict([[9,9]]) == ['Y']

    # tie
    knn2 = KNNClassifier(k=2)
    knn2.fit([[0,0],[2,0]], ['A','B'])
    result = knn2.predict([[1,0]])
    assert result[0] in ['A','B']

    # predict before fit
    try:
        KNNClassifier(k=3).predict([[1,1]])
        assert False
    except RuntimeError:
        pass

    # k > training points
    try:
        knn_bad = KNNClassifier(k=10)
        knn_bad.fit([[1,1],[2,2]], ['A','B'])
        assert False
    except ValueError:
        pass

    # cosine distance
    knn_cos = KNNClassifier(k=3, distance="cosine")
    knn_cos.fit(X, y)
    assert knn_cos.predict([[1,1]]) == ['A']
    assert knn_cos.predict([[9,9]]) == ['B']

    # unknown distance
    try:
        KNNClassifier(k=3, distance="manhattan")
        assert False
    except ValueError:
        pass

    print("all tests passed")


test_knn()