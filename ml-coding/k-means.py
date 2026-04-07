import random
import math
from typing import List


class KMeans:
    """
    K-Means clustering with naive or K-Means++ initialization.
    Time: O(n·k·d·i)  Space: O(n·d + k·d)

    assumption: len(points) > k, k >= 1
    """

    def __init__(self, k: int, max_iters: int = 100,
                 tol: float = 1e-6, init: str = "kmeans++"):
        if k < 1:
            raise ValueError("k must be >= 1")
        if init not in ("kmeans++", "naive"):
            raise ValueError("init must be 'kmeans++' or 'naive'")
        self.k = k
        self.max_iters = max_iters
        self.tol = tol # tolerance: threshold for deciding when the algorithm has converged

        self.init = init
        self.centroids: List[List[float]] = []
        self.labels_: List[int] = []

        # Inertia: the total sum of squared distances from each point to its assigned centroid.
        # measures how tight the clusters are. Lower inertia means points are closer to their centroids
        self.inertia_: float = float('inf') 

    def _dist(self, a, b) -> float:
        """
        Time O(d), Space O(1)
        """
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def _init_naive(self, points):
        """Pick k distinct random points as starting centroids. 
        Time O(k), Space O(k*d)
        """
        indices = random.sample(range(len(points)), self.k)
        return [list(points[i]) for i in indices]

    def _init_kmeanspp(self, points):
        """First centroid random, each next chosen proportional
        to squared distance from nearest existing centroid.
        Uses prefix sum + binary search for weighted sampling. 
        Time: O(n·k^2·d), Space: O(n) for dists + O(k·d) for centroids. Total Sapce O(n + k·d).
        
        optimized distance caching in K-Means++
        Time: O(n·k·d)
        """
        
        centroids = [list(random.choice(points))]
        # cache: min squared distance from each point to nearest centroid so far
        min_dists = [self._dist(p, centroids[0]) ** 2 for p in points]

        for _ in range(self.k - 1):
            # dists = [min(self._dist(p, c) ** 2 for c in centroids) for p in points]
            # to-do optimized idea: cache min distances, only update against new centroid each round

            # prefix sum (same pattern as LC528)
            prefix_sum, cur_sum = [], 0.0
            for d in min_dists:
                cur_sum += d
                prefix_sum.append(cur_sum)

            # lower bound binary search
            target = cur_sum * random.random()
            l, r, res = 0, len(prefix_sum) - 1, len(prefix_sum) - 1
            while l <= r:
                m = l + (r - l) // 2
                if prefix_sum[m] >= target:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            centroids.append(list(points[res]))

            # update cache: only compare against the newly added centroid
            new_c = centroids[-1]
            for i, p in enumerate(points):
                d = self._dist(p, new_c) ** 2
                if d < min_dists[i]:
                    min_dists[i] = d
                    
        return centroids

    def fit(self, points: List[List[float]]) -> "KMeans":
        # if len(points) < self.k:
        #     raise ValueError("Not enough points for k clusters")

        # Step 1: choose initialization
        if self.init == "kmeans++":
            self.centroids = self._init_kmeanspp(points)
        else:
            self.centroids = self._init_naive(points)

        for _ in range(self.max_iters):
            # Step2: assign each point to nearest centroid
            assignments = [
                min(range(self.k), key=lambda j: self._dist(p, self.centroids[j]))
                for p in points
            ]

            # Step3: recompute centroids, reinitialize empty clusters
            new_centroids = []
            for j in range(self.k):
                cluster = [points[i] for i, a in enumerate(assignments) if a == j]
                if cluster:
                    d = len(cluster[0])
                    new_centroids.append([sum(p[i] for p in cluster) / len(cluster) for i in range(d)])
                else:
                    new_centroids.append(list(random.choice(points)))

            # Step4: check convergence, stop if centroids barely moved
            if sum(self._dist(o, n) for o, n in zip(self.centroids, new_centroids)) < self.tol:
                self.centroids = new_centroids
                break
            self.centroids = new_centroids

        self.labels_ = assignments
        self.inertia_ = sum(
            self._dist(points[i], self.centroids[assignments[i]]) ** 2
            for i in range(len(points))
        )
        return self


# ── TEST CASES ─────────────────────────────────────────────────────────────

def test_kmeans():
    points = [[1,1],[1,2],[2,1],[8,8],[9,8],[8,9]]

    # normal: two clear clusters with kmeans++
    km = KMeans(k=2).fit(points)
    assert len(set(km.labels_)) == 2
    assert km.labels_[0] == km.labels_[1] == km.labels_[2]
    assert km.labels_[3] == km.labels_[4] == km.labels_[5]
    assert km.labels_[0] != km.labels_[3]
    assert 0 < km.inertia_ < float('inf')

    # normal: naive init also finds correct clusters
    km_naive = KMeans(k=2, init="naive").fit(points)
    assert len(set(km_naive.labels_)) == 2
    assert km_naive.labels_[0] == km_naive.labels_[1] == km_naive.labels_[2]
    assert km_naive.labels_[3] == km_naive.labels_[4] == km_naive.labels_[5]
    assert km_naive.labels_[0] != km_naive.labels_[3]

    # edge: k=1, all points in one cluster
    km1 = KMeans(k=1).fit(points)
    assert all(l == 0 for l in km1.labels_)

    # edge: k=n, each point its own cluster
    assert len(set(KMeans(k=3).fit([[0,0],[5,5],[10,10]]).labels_)) == 3

    # edge: k > n raises error
    try:
        KMeans(k=10).fit([[1,1],[2,2]])
        assert False
    except ValueError:
        pass

    # edge: invalid init raises error
    try:
        KMeans(k=2, init="random")
        assert False
    except ValueError:
        pass

    # n-dimensional: works in 5D
    KMeans(k=2).fit([[i]*5 for i in range(6)])

    print("all tests passed")


test_kmeans()