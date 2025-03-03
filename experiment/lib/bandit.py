import numpy as np
from scipy.stats import beta


class Bandit:
    def __init__(self, n_arms: int):
        self.n_arms = n_arms
        self.n_success = np.zeros(n_arms)
        self.n_failures = np.zeros(n_arms)

    def pull(self):
        samples = [self.beta(i) for i in range(self.n_arms)]
        best_arm = np.argmax(samples)

        return best_arm

    def beta(self, arm: int):
        s = self.n_success[arm]
        f = self.n_failures[arm]

        return np.random.beta(s + 1, f + 1)

    def beta_pdf(self, x, arm: int):
        s = self.n_success[arm]
        f = self.n_failures[arm]

        return beta.pdf(x, s + 1, f + 1)

    def update(self, arm: int, reward: bool):
        if reward:
            self.n_success[arm] += 1
        else:
            self.n_failures[arm] += 1
