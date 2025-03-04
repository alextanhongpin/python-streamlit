import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from lib.bandit import Bandit

st.title("Pick a fruit")


n_arms = 3
if 'bandit' not in st.session_state:
    st.session_state.bandit = Bandit(n_arms)
fruits = ['Apple', 'Banana', 'Orange']

cols = st.columns(3)
for i, col in enumerate(cols):
    if col.button(fruits[i], use_container_width=True):
        st.session_state.bandit.update(i, 1)

arm = st.session_state.bandit.pull()
st.write(f"Suggesting {fruits[arm]} for the next pick!")
for i in range(n_arms):
    success = int(st.session_state.bandit.n_success[i])
    failure = int(st.session_state.bandit.n_failure[i])
    st.write(f"{fruits[i]}: {success}/{success+failure}")
