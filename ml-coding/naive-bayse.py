from collections import defaultdict
import math
from typing import List, Dict, Any


class NaiveBayes:
    """
    Multinomial Naive Bayes used for discrete data, such as word count in text classification.
    Uses Laplace smoothing to handle unseen words.

    Fit:     time O(n·d + k·V). Space O(k·V)
    Predict: time O(k·L) per doc, k=classes. Space O(1)
             time O(m·k·L). Space O(m) for output
    where n=documents, 
          d=avg words per doc, 
          k=classes, 
          V=vocab size, 
          L=test doc length.


    """

    def __init__(self, alpha: float = 1.0):
        """alpha: smoothing strength. 1.0 is standard add-1 smoothing."""
        self.alpha = alpha
        self.class_log_priors: Dict[Any, float] = {}
        self.feature_log_probs: Dict[Any, Dict[str, float]] = {}
        self.unseen_log_prob: Dict[Any, float] = {}
        self.vocab: set = set()
        self.classes: List[Any] = []

    def fit(self, X: List[List[str]], y: List[Any]) -> "NaiveBayes":
        """
        X: list of tokenized documents e.g. [["good","film"], ["bad","plot"]]
        y: class labels e.g. ["pos", "pos", "neg", "neg"]

        time: O(n·d) for building vocab, O(k·V) for feature_log_probs, in practice O(n·d) dominate
        space: O(k·V) to store the log probability table for every word in every class.
        """
        n = len(X)
        self.classes = list(set(y))
        self.vocab = {word for doc in X for word in doc} # set comprehension

        for cls in self.classes:
            # collect all documents for this class
            class_docs = [X[i] for i, label in enumerate(y) if label == cls]

            # log prior: log(count of this class / total documents)
            self.class_log_priors[cls] = math.log(len(class_docs) / n)

            # count every word in this class
            word_counts = {}
            for doc in class_docs:
                for word in doc:
                    word_counts[word] = 1 + word_counts.get(word, 0)

            total_words = sum(word_counts.values())
            vocab_size = len(self.vocab)

            # smoothed log probability for each known word
            self.feature_log_probs[cls] = {
                word: math.log(
                    (word_counts[word] + self.alpha)
                    / (total_words + self.alpha * vocab_size)
                )
                for word in self.vocab
            }

            # log probability for unseen words (count = 0 with smoothing)
            self.unseen_log_prob[cls] = math.log(
                self.alpha / (total_words + self.alpha * vocab_size)
            )

        return self

    def _predict_one(self, doc: List[str]) -> Any:
        """
        Score each class using log prior + sum of log word probabilities.
        Return class with highest score.

        time:  Total O(k·L) per document. L is average document length.
        space: O(1)

        """
        best_class = None
        best_score = float('-inf')

        for cls in self.classes:
            # start with log prior
            score = self.class_log_priors[cls]

            # add log probability of each word
            for word in doc:
                if word in self.feature_log_probs[cls]:
                    score += self.feature_log_probs[cls][word]
                else:
                    # unseen word: use smoothed probability with count=0
                    score += self.unseen_log_prob[cls]

            if score > best_score:
                best_score = score
                best_class = cls

        return best_class

    def predict(self, X: List[List[str]]) -> List[Any]:
        """Predict class for each document."""
        if not self.classes:
            raise RuntimeError("Call fit() before predict()")
        return [self._predict_one(doc) for doc in X]


# ── TEST CASES ─────────────────────────────────────────────────────────────

def test_naive_bayes():

    X_train = [
        ["great", "film"],
        ["amazing", "movie"],
        ["terrible", "film"],
        ["bad", "movie"]
    ]
    y_train = ["pos", "pos", "neg", "neg"]

    nb = NaiveBayes(alpha=1.0).fit(X_train, y_train)

    # normal: clear positive signal
    assert nb.predict([["great", "film"]]) == ["pos"]
    assert nb.predict([["terrible", "movie"]]) == ["neg"]

    # normal: multiple documents at once
    assert nb.predict([["great", "film"], ["bad", "movie"]]) == ["pos", "neg"]

    # edge: unseen word should not crash, Laplace handles it
    result = nb.predict([["unseen_word_xyz", "great"]])
    assert result[0] in ["pos", "neg"], "unseen word should not crash"

    # edge: empty document returns majority class
    result_empty = nb.predict([[]])
    assert result_empty[0] in ["pos", "neg"], "empty doc should return some class"

    # edge: predict before fit raises error
    try:
        NaiveBayes().predict([["great"]])
        assert False
    except RuntimeError:
        pass

    # alpha=0: no smoothing, known words still work
    nb_no_smooth = NaiveBayes(alpha=0.0).fit(X_train, y_train)
    assert nb_no_smooth.predict([["great"]]) == ["pos"]

    print("all tests passed")


test_naive_bayes()