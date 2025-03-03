 # Pie char

import streamlit as st
import pandas as pd
import plotly.express as px

a = 1
b = 2
c = 3

data = pd.DataFrame({
    "Kategorie" : ["A","B","C"],
    "Hodnoty" : [a,b,c]
})


fig_pie = px.pie(
    data, 
    names = "Kategorie",
    values = "Hodnoty",
    title = "Kolacovy graf plotlib"
)

st.plotly_chart(fig_pie)