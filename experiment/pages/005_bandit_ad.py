import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from lib.bandit import Bandit


fruits = ["Apple", "Banana", "Orange"]
images = [
    "assets/images/apple.jpg",
    "assets/images/banana.jpg",
    "assets/images/orange.webp",
]

n_arms = len(fruits)
if "bandit" not in st.session_state:
    st.session_state.bandit = Bandit(n_arms)

arm, probs = st.session_state.bandit.pull(return_probs=True)


def update(arm, reward):
    st.session_state.bandit.update(arm, reward)


st.title("Fruit Bandit")
st.image(images[arm])
st.write(f"Do you like {fruits[arm]}?")
st.write(probs)

yes, no, skip = st.columns(3)
yes.button(
    "Yes", type="primary", use_container_width=True, on_click=update, args=[arm, True]
)
no.button(
    "No", type="secondary", use_container_width=True, on_click=update, args=[arm, False]
)
skip.button("Skip", type="secondary", use_container_width=True)

for i in range(n_arms):
    bandit = st.session_state.bandit
    success, failure = bandit.engagements[i]
    success = int(success)
    failure = int(failure)
    impressions = int(bandit.impressions[i])
    st.write(f"{fruits[i]}: {success}/{failure} (shown {impressions} times)")
