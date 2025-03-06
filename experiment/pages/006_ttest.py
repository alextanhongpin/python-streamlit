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
alpha = 0.05

if p_value < alpha:
    st.success("The result is statistically significant.")
    st.write(
        """
    The result is statistically significant, meaning the observed difference between the control and variation groups is unlikely to be due to random chance. This suggests that the variation has a real effect on the conversion rate. You can confidently conclude that the changes implemented in the variation group have led to an improvement (or decline) in performance. Consider implementing the changes from the variation group to your overall user base if they align with your business goals.
    """
    )
else:
    st.warning("The result is not statistically significant.")
    st.write(
        """
    The result is not statistically significant, meaning the observed difference between the control and variation groups could be due to random chance. This suggests that you cannot confidently conclude that the variation has a real effect on the conversion rate. Consider running the test for a longer period, increasing the sample size, or reevaluating the test design and hypotheses.
    """
    )
