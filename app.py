from pathlib import Path

import pandas as pd
import streamlit as st

# Ruta del CSV incluido con el proyecto
DATA_PATH = Path(__file__).parent / "data" / "ejemplo.csv"

st.set_page_config(
    page_title="Mi primer deploy",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Mi primer deploy")
st.write(
    "Una aplicación interactiva en Python para explorar archivos CSV. "
    "Puedes empezar con los datos de ejemplo o cargar tu propio archivo."
)

uploaded_file = st.file_uploader("Carga un archivo CSV", type=["csv"])
use_example = st.checkbox("Usar el archivo de ejemplo", value=uploaded_file is None)

df = None

try:
    if uploaded_file is not None and not use_example:
        df = pd.read_csv(uploaded_file)
    elif use_example:
        if DATA_PATH.exists():
            df = pd.read_csv(DATA_PATH)
        else:
            st.error(f"No se encontró el archivo de ejemplo: {DATA_PATH}")
except (pd.errors.ParserError, UnicodeDecodeError, OSError) as exc:
    st.error(f"No se pudo leer el CSV. Revisa el formato del archivo. Detalle: {exc}")

if df is not None:
    st.subheader("Vista previa")
    st.dataframe(df.head(20), use_container_width=True)

    st.subheader("Resumen del conjunto de datos")
    col1, col2, col3 = st.columns(3)
    col1.metric("Filas", f"{df.shape[0]:,}")
    col2.metric("Columnas", f"{df.shape[1]:,}")
    col3.metric("Valores ausentes", f"{int(df.isna().sum().sum()):,}")

    with st.expander("Estadísticas descriptivas"):
        st.dataframe(df.describe(include="all").transpose(), use_container_width=True)

    with st.expander("Tipos de datos y valores ausentes"):
        summary = pd.DataFrame({
            "tipo_de_dato": df.dtypes.astype(str),
            "valores_ausentes": df.isna().sum(),
        })
        st.dataframe(summary, use_container_width=True)

    csv_bytes = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar datos como CSV",
        data=csv_bytes,
        file_name="datos_explorados.csv",
        mime="text/csv",
    )
else:
    st.info("Carga un archivo CSV o selecciona la opción para usar el archivo de ejemplo.")
