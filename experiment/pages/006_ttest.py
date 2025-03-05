import streamlit as st
from lib.ab import test_mean_2indep

st.set_page_config(page_title="Significant Test", page_icon="🔎")

st.header("Independent Two-Sample T-Test")
st.write(
    "This is a simple two-sample t-test calculator. Enter the sample statistics for each group to test the hypothesis."
)

cols = st.columns(3)

mean1 = cols[0].number_input("Mean 1", min_value=0.0, value=48.0, format="%0.4f")
nobs1 = cols[1].number_input("Nobs 1", step=1, min_value=0, value=30)
std1 = cols[2].number_input("Std 1", min_value=0.0, value=5.0, format="%0.4f")

cols = st.columns(3)

mean2 = cols[0].number_input("Mean 2", min_value=0.0, value=50.0, format="%0.4f")
nobs2 = cols[1].number_input("Nobs 2", step=1, min_value=0, value=30)
std2 = cols[2].number_input("Std 2", min_value=0.00, value=5.0, format="%0.4f")


hypothesis = st.radio("Hypothesis", ["two-sided", "less", "greater"])

stats, p_value = test_mean_2indep(
    mean1=mean1,
    mean2=mean2,
    std1=std1,
    std2=std2,
    nobs1=nobs1,
    nobs2=nobs2,
    alternative=hypothesis,
)
st.write(f"p-value: {p_value:.4f}")
st.write(f"Z-score: {stats:.4f}")

tail = "two-tailed" if hypothesis == "two-sided" else "one-tailed"

if p_value < 0.05:
    f"The {tail} P value is less than {p_value:.4f}"
    "By conventional criteria, this difference is considered to be extremely statistically significant."
else:
    f"The {tail} P value equals {p_value:.4f}"
    "By conventional criteria, this difference is considered to be not statistically significant."
