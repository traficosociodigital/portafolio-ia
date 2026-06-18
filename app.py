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

    st.write(df.columns)

    # Calcular ventas
    df["Venta"] = df["Cantidad"] * df["Precio"]
    st.sidebar.header("Filtros")

categoria = st.sidebar.selectbox(
    "Categoría",
    ["Todas"] + list(df["Categoria"].unique())
)

if categoria != "Todas":
    df = df[df["Categoria"] == categoria]

    # KPIs
    ventas_totales = df["Venta"].sum()
    productos_vendidos = df["Cantidad"].sum()
    clientes = df["Cliente"].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric("Ventas Totales", f"${ventas_totales:,.0f}")
    col2.metric("Productos Vendidos", productos_vendidos)
    col3.metric("Clientes", clientes)

    st.divider()

    st.subheader("Datos de Ventas")
    st.dataframe(df)

    st.divider()


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
