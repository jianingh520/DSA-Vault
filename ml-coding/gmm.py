import math
from typing import List


class GMM1D:
    """
    Simplified 1D Gaussian Mixture Model using EM algorithm.
    Full n-D GMM needs matrix operations for covariance.
    Use this to demonstrate understanding of the concept.

    Per iteration: O(n·k)
    Space:         O(n·k) for responsibilities matrix
    """

    def __init__(self, k: int, max_iters: int = 50, tol: float = 1e-6):
        if k < 1:
            raise ValueError("k must be >= 1")
        self.k = k
        self.max_iters = max_iters
        self.tol = tol
        self.means = []
        self.sigmas = []
        self.pis = []

    def _gaussian(self, x: float, mu: float, sigma: float) -> float:
        """
        1D Gaussian probability density function.
        Clamp sigma to avoid division by zero.
        """
        sigma = max(sigma, 1e-6)
        return (math.exp(-0.5 * ((x - mu) / sigma) ** 2)
                / (sigma * math.sqrt(2 * math.pi)))

    def fit(self, data: List[float]) -> "GMM1D":
        n = len(data)

        # initialize: evenly spaced means, unit variance, equal mixing weights
        mn, mx = min(data), max(data)
        self.means  = [mn + (mx - mn) * (i + 1) / (self.k + 1) for i in range(self.k)]
        self.sigmas = [1.0] * self.k
        self.pis    = [1.0 / self.k] * self.k

        prev_ll = float('-inf')

        for _ in range(self.max_iters):

            # E-step: compute responsibility r[i][k] for each point and component
            r = []
            for x in data:
                probs = [self.pis[k] * self._gaussian(x, self.means[k], self.sigmas[k])
                         for k in range(self.k)]
                total = sum(probs) + 1e-300    # small constant avoids division by zero
                r.append([p / total for p in probs])

            # M-step: update parameters using responsibilities as soft weights
            for k in range(self.k):
                Nk = sum(r[i][k] for i in range(n)) + 1e-300
                self.means[k]  = sum(r[i][k] * data[i] for i in range(n)) / Nk
                self.sigmas[k] = math.sqrt(
                    sum(r[i][k] * (data[i] - self.means[k]) ** 2 for i in range(n)) / Nk
                )
                self.pis[k] = Nk / n

            # convergence: check if log likelihood improved
            ll = sum(
                math.log(
                    sum(self.pis[k] * self._gaussian(x, self.means[k], self.sigmas[k])
                        for k in range(self.k)) + 1e-300
                )
                for x in data
            )
            if abs(ll - prev_ll) < self.tol:
                break
            prev_ll = ll

        return self

    def predict_proba(self, data: List[float]) -> List[List[float]]:
        """Return soft cluster probabilities for each point."""
        result = []
        for x in data:
            probs = [self.pis[k] * self._gaussian(x, self.means[k], self.sigmas[k])
                     for k in range(self.k)]
            total = sum(probs) + 1e-300
            result.append([p / total for p in probs])
        return result


# ── TEST CASES ─────────────────────────────────────────────────────────────

def test_gmm():

    # normal: two well separated clusters
    data = [1.0, 1.1, 0.9, 1.2, 0.8, 5.0, 4.9, 5.1, 4.8, 5.2]
    gmm = GMM1D(k=2).fit(data)

    # means should be near 1.0 and 5.0
    means_sorted = sorted(gmm.means)
    assert 0.5 < means_sorted[0] < 2.0, f"lower mean off: {means_sorted[0]}"
    assert 4.0 < means_sorted[1] < 6.0, f"upper mean off: {means_sorted[1]}"

    # soft probabilities: point near 1.0 should be confident in one cluster
    probs = gmm.predict_proba([1.0, 5.0])
    assert max(probs[0]) > 0.9, "point 1.0 should have confident assignment"
    assert max(probs[1]) > 0.9, "point 5.0 should have confident assignment"

    # probabilities should sum to 1 for each point
    for p in probs:
        assert abs(sum(p) - 1.0) < 1e-6, "probabilities must sum to 1"

    # edge: k=1, single component explains everything
    gmm1 = GMM1D(k=1).fit(data)
    assert abs(gmm1.pis[0] - 1.0) < 1e-6

    # edge: k > n should still not crash on small data
    GMM1D(k=2).fit([1.0, 5.0])

    print("all tests passed")


test_gmm()