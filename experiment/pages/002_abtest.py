import streamlit as st
from lib.ab import test_proportions_2indep

st.set_page_config(page_title="A/B Test", page_icon="🔎")

st.header("A/B Testing")
st.write(
    "This is a simple A/B testing calculator. Enter the number of visitors and conversions for each group to calculate the conversion rate and test the hypothesis."
)

cols = st.columns(3)
visitors_a = cols[0].number_input("Visitors A", step=1, min_value=0, value=80000)
conversion_a = cols[1].number_input("Conversion A", step=1, min_value=0, value=1600)
conversion_rate_a = conversion_a / visitors_a * 100
cols[2].number_input("Conversion rate A (%)", value=conversion_rate_a, disabled=True)

cols = st.columns(3)
visitors_b = cols[0].number_input("Visitors B", step=1, min_value=0, value=80000)
conversion_b = cols[1].number_input("Conversion B", step=1, min_value=0, value=1712)
conversion_rate_b = conversion_b / visitors_b * 100
cols[2].number_input("Conversion rate B (%)", value=conversion_rate_b, disabled=True)

relative_uplift = (conversion_rate_b - conversion_rate_a) / conversion_rate_a * 100
st.write(f"Relative uplift in Conversion Rate: {relative_uplift:.2f}%")

hypothesis = st.radio("Hypothesis", ["two-sided", "smaller", "larger"])

stats, p_value = test_proportions_2indep(
    conversion_a, conversion_b, visitors_a, visitors_b, alternative=hypothesis
)
st.write(f"p-value: {p_value:.4f}")
st.write(f"Z-score: {stats:.4f}")

if p_value < 0.05:
    st.write("We reject the null hypothesis")
else:
    st.write("We fail to reject the null hypothesis")
