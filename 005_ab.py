import streamlit as st
from ab import analyze

a, b = st.columns(2)
visitors_a = a.number_input("Visitors A", step=1, min_value=0, value=80000)
conversion_a = b.number_input("Conversion A", step=1, min_value=0, value=1600)

c, d = st.columns(2)
visitors_b = c.number_input("Visitors B", step=1, min_value=0, value=80000)
conversion_b = d.number_input("Conversion B", step=1, min_value=0, value=1712)

hypothesis = st.radio("Hypothesis", ["two-sided", "smaller", "larger"])
confidence = st.radio("Confidence level", [90, 95, 99])


alpha = 1 - confidence / 100

stats, p_value = analyze(
    conversion_a, conversion_b, visitors_a, visitors_b, alternative=hypothesis
)
st.write(f"p-value: {p_value:.4f}")
st.write(f"statistic: {stats:.4f}")

if p_value < 0.05:
    st.write("We reject the null hypothesis")
else:
    st.write("We fail to reject the null hypothesis")
