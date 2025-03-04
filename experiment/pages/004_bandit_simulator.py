import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from lib.bandit import Bandit

st.title("Multi-Armed Bandit Simulator")

probs = st.text_input("Arm probabilities", value="0.7,0.3,0.1", key="probs")
probs = [float(p) for p in probs.split(",")]

n_arms = len(probs)
bandit = Bandit(n_arms)
empty = st.empty()

x = np.linspace(0, 1.0, 100)

for i in range(100):
    for arm in range(n_arms):
        y = bandit.beta_pdf(x, arm)
        plt.plot(x, y, label=str(probs[arm]))
    plt.legend()
    plt.title("Beta distributions for each arm (iters: %d)" % i)

    arm = bandit.pull()
    reward = np.random.random() < probs[arm]
    bandit.update(arm, reward)
    with empty.container():
        st.pyplot(plt, clear_figure=True)


for arm in range(n_arms):
    st.write(
        f"Arm {arm} has a success rate of {bandit.n_success[arm] / (bandit.n_success[arm] + bandit.n_failures[arm]):.2f} ({int(bandit.n_success[arm])} / {int(bandit.n_success[arm] + bandit.n_failures[arm])})"
    )
