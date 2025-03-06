import streamlit as st
from lib.ab import sample_size_for_proportions


st.title("A/B Test Sample Size Calculator")
st.write(
    "Welcome to the A/B Test Sample Size Calculator! This tool helps you determine the minimum sample size needed for your A/B test to achieve statistically significant results."
)

cols = st.columns(3)
conversion_rate_a = cols[0].number_input(
    "Conversion rate control\n\n(in %)",
    min_value=0,
    value=2,
    help="**Baseline Conversion Rate**: The current conversion rate of the control group (in percentage).",
)
expected_improvement = cols[1].number_input(
    "Expected improvement over control\n(relative, in %)",
    min_value=0,
    value=15,
    help="**Minimum Detectable Effect (MDE)**: The smallest change in conversion rate that you want to detect (in percentage).",
)
conversion_rate_b = conversion_rate_a * (1 + expected_improvement / 100)
cols[2].number_input(
    "Conversion rate B\n\n(in %)", value=conversion_rate_b, disabled=True
)

hypothesis = st.radio("Hypothesis", ["two-sided", "smaller", "larger"])
confidence = st.radio(
    "Confidence level (1-alpha)",
    ["90%", "95%", "99%"],
    index=1,
    help="**Significance Level (Alpha)**: The probability of rejecting the null hypothesis when it is true (common values: 0.05 or 0.01).",
)
power = st.radio(
    "Power",
    ["75%", "80%", "90%", "95%"],
    index=1,
    help="**Statistical Power (1 - Beta)**: The probability of correctly rejecting the null hypothesis (common value: 0.80).",
)

alpha = 1 - int(confidence[:-1]) / 100
power = int(power[:-1]) / 100

sample_size = sample_size_for_proportions(
    conversion_rate_a / 100,
    conversion_rate_b / 100,
    alpha=alpha,
    alternative=hypothesis,
    power=power,
)

with st.container():
    st.write(f"Minimum sample size:")
    st.subheader(f"{sample_size:,}")
    st.write("unique visitors per group")
