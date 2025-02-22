import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

st.pyplot(fig)

fig = go.Figure(
    data=go.Bar(y=[2, 3, 1], marker_color="red")  # replace with your own data source
)

st.plotly_chart(fig)


a = np.random.binomial(80000, 1600 / 80000, 1000)
b = np.random.binomial(80000, 1696 / 80000, 1000)

df = pd.DataFrame(
    {
        "labels": np.concatenate([["a"] * 1000, ["b"] * 1000]),
        "conversion": np.concatenate([a, b]),
    }
)

fig = px.box(df, x="labels", y="conversion")
st.plotly_chart(fig)


fig = go.Figure()
fig.add_trace(go.Box(x=a, name="A"))
fig.add_trace(go.Box(x=b, name="B"))
st.plotly_chart(fig)

st.write("A", len(a), "B", len(b))
