import streamlit as st
from lib.ab import test_proportions_2indep

st.set_page_config(page_title="A/B Test", page_icon="🔎")

st.header("A/B Testing")
st.write(
    "This is a simple A/B testing calculator. Enter the number of visitors and conversions for each group to calculate the conversion rate and test the hypothesis."
)


# Control Group
cols = st.columns(3)
visitors_a = cols[0].number_input("Visitors A", step=1, min_value=0, value=80000)
conversion_a = cols[1].number_input("Conversion A", step=1, min_value=0, value=1600)
conversion_rate_a = conversion_a / visitors_a
cols[2].number_input(
    "Conversion rate A (%)", value=conversion_rate_a * 100, disabled=True
)

cols = st.columns(3)
visitors_b = cols[0].number_input("Visitors B", step=1, min_value=0, value=80000)
conversion_b = cols[1].number_input("Conversion B", step=1, min_value=0, value=1712)
conversion_rate_b = conversion_b / visitors_b
cols[2].number_input(
    "Conversion rate B (%)", value=conversion_rate_b * 100, disabled=True
)

relative_uplift = (conversion_rate_b - conversion_rate_a) / conversion_rate_a * 100
st.write(f"Relative uplift in Conversion Rate: {relative_uplift:.2f}%")

alpha = 0.05
hypothesis = st.radio("Hypothesis", ["two-sided", "smaller", "larger"])

z_score, p_value = test_proportions_2indep(
    conversion_a, conversion_b, visitors_a, visitors_b, alternative=hypothesis
)

st.subheader("Results")
st.write(f"**Z-score**: {z_score:.4f}")
st.write(f"**P-value**: {p_value:.4f}")

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
