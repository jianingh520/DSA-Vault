from typing import List, Tuple, Iterator, Any
import random
from collections import defaultdict

# ─────────────────────────────────────────────
# 1. CLASSIC K-FOLD
# ─────────────────────────────────────────────
# Split n samples into k folds.
# Each fold takes a turn as the validation set.
# The rest become the training set.
#
# Time:  O(n) per split call
# Space: O(n) for the index list

class KFoldCV:
    def __init__(self, k: int, shuffle: bool = False, seed: int = 42):
        if k < 2:
            raise ValueError("k must be >= 2")
        self.k = k
        self.shuffle = shuffle
        self.seed = seed

    def split(self, n: int) -> Iterator[Tuple[List[int], List[int]]]:
        """Yields (train_indices, val_indices) for each of k folds."""
        if n < self.k:
            raise ValueError(f"Not enough samples ({n}) for {self.k} folds")

        indices = list(range(n))
        if self.shuffle:
            random.seed(self.seed)
            random.shuffle(indices)

        # Distribute any remainder across the first (n % k) folds
        # e.g. n=10, k=3 → fold sizes: [4, 3, 3]
        fold_sizes = [n // self.k] * self.k
        for i in range(n % self.k):
            fold_sizes[i] += 1

        start = 0
        for fold_size in fold_sizes:
            val_idx   = indices[start : start + fold_size]
            train_idx = indices[:start] + indices[start + fold_size:]
            yield train_idx, val_idx
            start += fold_size


# ─────────────────────────────────────────────
# 2. STRATIFIED K-FOLD
# ─────────────────────────────────────────────
# Problem with classic K-Fold on imbalanced data:
# a fold might get all the rare class samples, or none at all.
# Fix: group indices by class label first, then distribute
# each group evenly across folds.
#
# Example: labels = [0,0,0,0,1,1]  k=2
#   class-0 indices: [0,1,2,3] → fold0 gets [0,1], fold1 gets [2,3]
#   class-1 indices: [4,5]     → fold0 gets [4],   fold1 gets [5]
#   fold0 val = [0,1,4], fold1 val = [2,3,5]  ← ratio preserved
#
# Time:  O(n) per split call
# Space: O(n)

class StratifiedKFoldCV:
    def __init__(self, k: int, shuffle: bool = False, seed: int = 42):
        if k < 2:
            raise ValueError("k must be >= 2")
        self.k = k
        self.shuffle = shuffle
        self.seed = seed

    def split(
        self, labels: List[Any]
    ) -> Iterator[Tuple[List[int], List[int]]]:
        """
        Yields (train_indices, val_indices) with class ratio preserved.
        labels: the class label for each sample (e.g. [0,1,0,1,1])
        """
        n = len(labels)
        if n < self.k:
            raise ValueError(f"Not enough samples ({n}) for {self.k} folds")

        # Group sample indices by their label
        class_indices: dict = defaultdict(list)
        for i, label in enumerate(labels):
            class_indices[label].append(i)

        if self.shuffle:
            random.seed(self.seed)
            for idx_list in class_indices.values():
                random.shuffle(idx_list)

        # Build k buckets; distribute each class's indices round-robin
        # into buckets so each bucket gets ~equal share of each class
        buckets: List[List[int]] = [[] for _ in range(self.k)]
        for idx_list in class_indices.values():
            for i, idx in enumerate(idx_list):
                buckets[i % self.k].append(idx)

        # Each bucket takes a turn as validation
        for fold in range(self.k):
            val_idx   = buckets[fold]
            train_idx = [idx for b in range(self.k) if b != fold
                             for idx in buckets[b]]
            yield train_idx, val_idx


# ─────────────────────────────────────────────
# 3. TIME SERIES K-FOLD
# ─────────────────────────────────────────────
# In time series data, shuffling is not allowed.
# A model must never see future events during training.
# This is called "data leakage" (future info leaking into training).
#
# Strategy: always expand the training window forward.
# fold 0: train=[0..train_size-1],      val=[train_size..train_size+val_size-1]
# fold 1: train=[0..train_size+val_size-1], val=[next val_size window]
# ...
#
# Time:  O(n) per split call
# Space: O(n)

class TimeSeriesKFoldCV:
    def __init__(self, k: int):
        if k < 2:
            raise ValueError("k must be >= 2")
        self.k = k

    def split(self, n: int) -> Iterator[Tuple[List[int], List[int]]]:
        """
        Yields (train_indices, val_indices) in chronological order.
        Training window expands; validation window slides forward.
        No shuffling. No future data in training.
        """
        # We need at least k+1 chunks to have k folds
        # Divide n into (k+1) equal chunks
        # chunk 0..fold-1 = train, chunk fold = val
        chunk_size = n // (self.k + 1)
        if chunk_size == 0:
            raise ValueError(f"Not enough samples ({n}) for {self.k} folds")

        for fold in range(1, self.k + 1):
            train_end = fold * chunk_size        # exclusive
            val_end   = train_end + chunk_size   # exclusive
            if val_end > n:
                break
            train_idx = list(range(0, train_end))
            val_idx   = list(range(train_end, val_end))
            yield train_idx, val_idx


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

def test_kfold():
    # Normal: 9 samples, k=3 → 3 folds of 3 each
    folds = list(KFoldCV(k=3).split(9))
    assert len(folds) == 3
    for train, val in folds:
        assert len(train) + len(val) == 9
        assert len(set(train) & set(val)) == 0, "train and val must not overlap"

    # All val indices together cover every sample exactly once
    all_val = [idx for _, val in folds for idx in val]
    assert sorted(all_val) == list(range(9))

    # Uneven split: 10 samples, k=3 → folds of size 4, 3, 3
    folds2 = list(KFoldCV(k=3).split(10))
    fold_sizes = [len(val) for _, val in folds2]
    assert sum(fold_sizes) == 10

    # Edge: n == k → each fold has exactly 1 sample
    folds3 = list(KFoldCV(k=4).split(4))
    assert all(len(val) == 1 for _, val in folds3)

    print("Classic K-Fold: all tests passed")


def test_stratified_kfold():
    # 6 samples: 4 class-0, 2 class-1
    labels = [0, 0, 0, 0, 1, 1]
    folds = list(StratifiedKFoldCV(k=2).split(labels))
    assert len(folds) == 2

    for train, val in folds:
        assert len(set(train) & set(val)) == 0, "no overlap"
        assert len(train) + len(val) == 6

    # All val indices together cover every sample exactly once
    all_val = sorted(idx for _, val in folds for idx in val)
    assert all_val == list(range(6))

    # Each val fold should have at least one sample from each class
    for _, val in folds:
        val_labels = [labels[i] for i in val]
        assert 0 in val_labels, "class 0 missing from val fold"
        assert 1 in val_labels, "class 1 missing from val fold"

    print("Stratified K-Fold: all tests passed")


def test_time_series_kfold():
    # 10 samples, k=4 → chunk_size=2
    # fold 0: train=[0,1],       val=[2,3]
    # fold 1: train=[0,1,2,3],   val=[4,5]
    # fold 2: train=[0..5],      val=[6,7]
    # fold 3: train=[0..7],      val=[8,9]
    folds = list(TimeSeriesKFoldCV(k=4).split(10))
    assert len(folds) == 4

    for i, (train, val) in enumerate(folds):
        # Training set must always end before val set starts
        assert max(train) < min(val), "future data leaked into training"
        # Training set must grow with each fold
        if i > 0:
            prev_train = folds[i-1][0]
            assert len(train) > len(prev_train), "training window must expand"

    # No overlap between train and val in any fold
    for train, val in folds:
        assert len(set(train) & set(val)) == 0

    print("Time Series K-Fold: all tests passed")


test_kfold()
test_stratified_kfold()
test_time_series_kfold()