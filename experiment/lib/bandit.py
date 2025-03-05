import numpy as np
from scipy.stats import beta


class Bandit:
    def __init__(self, n_arms: int):
        self.n_arms = n_arms
        self.n_success = np.zeros(n_arms)
        self.n_failure = np.zeros(n_arms)
        self.n_impressions = np.zeros(n_arms)

    def pull(self, return_probs=False):
        samples = [self.beta(i) for i in range(self.n_arms)]
        best_arm = np.argmax(samples)

        self.n_impressions[best_arm] += 1

        if return_probs:
            return best_arm, samples

        return best_arm

    def beta(self, arm: int):
        s = self.n_success[arm]
        f = self.n_failure[arm]
        i = self.n_impressions[arm] / 10  # Add penalty to impressions.

        return np.random.beta(s + 1 + i, f + 1 + i)

    def beta_pdf(self, x, arm: int):
        s = self.n_success[arm]
        f = self.n_failure[arm]
        i = self.n_impressions[arm] / 10

        return beta.pdf(x, s + 1 + i, f + 1 + i)

    def update(self, arm: int, reward: bool):
        if reward:
            self.n_success[arm] += 1
        else:
            self.n_failure[arm] += 1
