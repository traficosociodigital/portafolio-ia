import streamlit as st
import pandas as pd

st.title("Dashboard de Ventas")

df = pd.read_csv("ventas.csv")

st.subheader("Datos cargados")

st.dataframe(df)