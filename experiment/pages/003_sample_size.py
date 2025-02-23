import streamlit as st
from lib.ab import sample_size_for_proportions

st.header('A/B Sample Size Calculator')
st.write("This app calculates the sample size needed for an A/B test.")

cols = st.columns(3)
conversion_rate_a = cols[0].number_input("Conversion rate control\n\n(in %)", min_value=0, value=2)
expected_improvement = cols[1].number_input("Expected improvement over control\n(relative, in %)", min_value=0, value=15)
conversion_rate_b  = conversion_rate_a * (1 + expected_improvement / 100)
cols[2].number_input("Conversion rate B\n\n(in %)", value=conversion_rate_b, disabled=True)

hypothesis = st.radio("Hypothesis", ["two-sided", "smaller", "larger"])
confidence = st.radio("Confidence level (1-alpha)", ['90%', '95%', '99%'], index=1)
power = st.radio("Power", ['75%', '80%', '90%', '95%'], index=1)

alpha = 1 - int(confidence[:-1]) / 100
power = int(power[:-1]) / 100

sample_size = sample_size_for_proportions(
    conversion_rate_a / 100, conversion_rate_b / 100, alpha=alpha, alternative=hypothesis, power=power 
)

with st.container():
    st.write(f"Minimum sample size:")
    st.subheader(f"{sample_size:,}")
    st.write("unique visitors per group")
