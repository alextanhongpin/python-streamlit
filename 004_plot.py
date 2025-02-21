import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

st.pyplot(fig)

fig = go.Figure(
    data=go.Bar(y=[2, 3, 1], marker_color="red")  # replace with your own data source
)

st.plotly_chart(fig)
