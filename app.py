import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

st.title("📊 Dashboard de Ventas")

archivo = st.file_uploader(
    "Seleccione un archivo CSV",
    type=["csv"]
)

if archivo is not None:
    df = pd.read_csv(archivo)

    # Calcular ventas
    df["Venta"] = df["Cantidad"] * df["Precio"]

    # KPIs
    ventas_totales = df["Venta"].sum()
    productos_vendidos = df["Cantidad"].sum()
    ciudades = df["Ciudad"].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric("Ventas Totales", f"${ventas_totales:,.0f}")
    col2.metric("Productos Vendidos", productos_vendidos)
    col3.metric("Ciudades", ciudades)

    st.divider()

    st.subheader("Datos de Ventas")
    st.dataframe(df)

    st.divider()

    st.subheader("Ventas por Ciudad")

    ventas_ciudad = (
        df.groupby("Ciudad")["Venta"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(ventas_ciudad)

    st.subheader("Ventas por Categoría")

    ventas_categoria = (
        df.groupby("Categoria")["Venta"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(ventas_categoria)

    st.subheader("Productos Más Vendidos")

    productos = (
        df.groupby("Producto")["Cantidad"]
        .sum()
        .sort_values(ascending=False)
    )

    st.dataframe(productos)

else:
    st.info("Por favor, cargue un archivo CSV para comenzar.")
