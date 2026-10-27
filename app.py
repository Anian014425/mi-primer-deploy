from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# --------------------------------------------------
# 1. Configuración general de la aplicación
# --------------------------------------------------
st.set_page_config(
    page_title="Dashboard | Cafetería Gourmet",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# 2. Diseño visual con CSS
# --------------------------------------------------
st.markdown(
    """
    <style>
        .main {
            background-color: #FAF7F2;
        }

        h1 {
            color: #5B3924;
            font-weight: 800;
        }

        h2, h3 {
            color: #754C30;
        }

        [data-testid="stMetric"] {
            background-color: #FFFFFF;
            border: 1px solid #E7D9C8;
            padding: 18px;
            border-radius: 12px;
        }

        div[data-testid="stPlotlyChart"] {
            background-color: #FFFFFF;
            border-radius: 12px;
            padding: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# 3. Carga de datos
# --------------------------------------------------
RUTA_DATOS = Path("data/datos.csv")


@st.cache_data
def cargar_datos(ruta):
    """Carga el CSV y prepara las columnas necesarias."""
    df = pd.read_csv(ruta)

    # Elimina espacios accidentales en los nombres
    df.columns = df.columns.str.strip()

    # Convierte las fechas, si existe la columna
    if "fecha_venta" in df.columns:
        df["fecha_venta"] = pd.to_datetime(
            df["fecha_venta"], errors="coerce"
        )

    # Convierte las ventas a valores numéricos
    if "ventas_totales" in df.columns:
        df["ventas_totales"] = pd.to_numeric(
            df["ventas_totales"], errors="coerce"
        )

    return df


if not RUTA_DATOS.exists():
    st.error(
        "No se encontró el archivo data/datos.csv. "
        "Verifica que exista la carpeta data y que el CSV "
        "tenga ese nombre."
    )
    st.stop()


try:
    df = cargar_datos(str(RUTA_DATOS))
except Exception as error:
    st.error(f"No fue posible cargar el archivo CSV: {error}")
    st.stop()


if df.empty:
    st.warning("El archivo CSV no contiene registros.")
    st.stop()


# --------------------------------------------------
# 4. Título y subtítulo
# --------------------------------------------------
st.title("☕ Café & Datos: Dashboard Gourmet")
st.subheader(
    "📊 Descubre tus productos estrella, analiza tus ventas "
    "y transforma los datos en decisiones inteligentes."
)

st.markdown(
    "Explora el rendimiento de tu cafetería con filtros "
    "interactivos y visualizaciones que se actualizan en tiempo real."
)

st.divider()


# --------------------------------------------------
# 5. Validación de columnas necesarias
# --------------------------------------------------
columnas_requeridas = [
    "ventas_totales",
    "producto",
    "categoria"
]

faltantes = [
    columna
    for columna in columnas_requeridas
    if columna not in df.columns
]

if faltantes:
    st.error(
        "Faltan estas columnas necesarias en el CSV: "
        + ", ".join(faltantes)
    )
    st.write("Columnas encontradas:", df.columns.tolist())
    st.stop()


# --------------------------------------------------
# 6. Barra lateral: filtros interactivos
# --------------------------------------------------
st.sidebar.header("🎛️ Panel de filtros")
st.sidebar.caption("Personaliza los datos que quieres analizar.")

df_filtrado = df.copy()

# Filtro por categoría
categorias = sorted(
    df["categoria"].dropna().astype(str).unique().tolist()
)

categorias_seleccionadas = st.sidebar.multiselect(
    "🛍️ Selecciona las categorías",
    options=categorias,
    default=categorias,
    help="Puedes seleccionar una o varias categorías."
)

df_filtrado = df_filtrado[
    df_filtrado["categoria"].astype(str).isin(
        categorias_seleccionadas
    )
]

# Filtro por producto
productos = sorted(
    df_filtrado["producto"].dropna().astype(str).unique().tolist()
)

productos_seleccionados = st.sidebar.multiselect(
    "🍰 Selecciona los productos",
    options=productos,
    default=productos
)

df_filtrado = df_filtrado[
    df_filtrado["producto"].astype(str).isin(
        productos_seleccionados
    )
]

# Filtro opcional por sucursal
if "sucursal" in df_filtrado.columns:
    sucursales = sorted(
        df_filtrado["sucursal"].dropna().astype(str).unique().tolist()
    )

    sucursales_seleccionadas = st.sidebar.multiselect(
        "📍 Selecciona las sucursales",
        options=sucursales,
        default=sucursales
    )

    df_filtrado = df_filtrado[
        df_filtrado["sucursal"].astype(str).isin(
            sucursales_seleccionadas
        )
    ]

# Filtro opcional por método de pago
if "metodo_pago" in df_filtrado.columns:
    metodos_pago = sorted(
        df_filtrado["metodo_pago"].dropna().astype(str).unique().tolist()
    )

    metodos_seleccionados = st.sidebar.multiselect(
        "💳 Método de pago",
        options=metodos_pago,
        default=metodos_pago
    )

    df_filtrado = df_filtrado[
        df_filtrado["metodo_pago"].astype(str).isin(
            metodos_seleccionados
        )
    ]

# Checkbox: solo ventas con descuento
if "tiene_descuento" in df_filtrado.columns:
    solo_descuentos = st.sidebar.checkbox(
        "🏷️ Mostrar solo ventas con descuento",
        value=False
    )

    if solo_descuentos:
        descuentos = (
            df_filtrado["tiene_descuento"]
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["true", "1", "si", "sí", "yes"])
        )
        df_filtrado = df_filtrado[descuentos]

st.sidebar.divider()

if st.sidebar.button("🔄 Restablecer filtros"):
    st.rerun()


# --------------------------------------------------
# 7. Indicadores principales (KPI)
# --------------------------------------------------
if df_filtrado.empty:
    st.warning(
        "No hay ventas que coincidan con los filtros seleccionados. "
        "Modifica los filtros de la barra lateral."
    )
    st.stop()

ventas_totales = df_filtrado["ventas_totales"].sum()
numero_ventas = len(df_filtrado)
ticket_promedio = df_filtrado["ventas_totales"].mean()

col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Ventas totales",
    f"${ventas_totales:,.2f}"
)

col2.metric(
    "🧾 Número de registros",
    f"{numero_ventas:,}"
)

col3.metric(
    "☕ Venta promedio",
    f"${ticket_promedio:,.2f}"
)

st.divider()


# --------------------------------------------------
# 8. Gráfico 1: barras horizontales por producto
# --------------------------------------------------
st.subheader("🏆 1. Productos con mayores ventas")

ventas_producto = (
    df_filtrado.groupby("producto", as_index=False)
    ["ventas_totales"]
    .sum()
    .sort_values("ventas_totales", ascending=True)
)

fig_barras = px.bar(
    ventas_producto,
    x="ventas_totales",
    y="producto",
    orientation="h",
    title="Ventas totales por producto",
    labels={
        "ventas_totales": "Ventas ($)",
        "producto": "Producto"
    },
    color="ventas_totales",
    color_continuous_scale="YlOrBr",
    hover_data={"ventas_totales": ":,.2f"}
)

fig_barras.update_layout(
    template="plotly_white",
    height=max(400, len(ventas_producto) * 32),
    margin=dict(l=20, r=20, t=70, b=30),
    coloraxis_showscale=False,
    xaxis_tickprefix="$",
    xaxis_tickformat=",.0f"
)

st.plotly_chart(
    fig_barras,
    use_container_width=True
)


# --------------------------------------------------
# 9. Gráfico 2: dona de ventas por categoría
# --------------------------------------------------
st.subheader("🍩 2. Distribución de ventas por categoría")

ventas_categoria = (
    df_filtrado.groupby("categoria", as_index=False)
    ["ventas_totales"]
    .sum()
    .sort_values("ventas_totales", ascending=False)
)

fig_dona = px.pie(
    ventas_categoria,
    names="categoria",
    values="ventas_totales",
    hole=0.55,
    title="Participación de cada categoría",
    color_discrete_sequence=px.colors.qualitative.Set3
)

fig_dona.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "Ventas: $%{value:,.2f}<br>"
        "Participación: %{percent}"
        "<extra></extra>"
    )
)

fig_dona.update_layout(
    template="plotly_white",
    height=480,
    margin=dict(l=20, r=20, t=70, b=20),
    legend_title_text="Categoría"
)

st.plotly_chart(
    fig_dona,
    use_container_width=True
)


# --------------------------------------------------
# 10. Gráfico 3: histograma de ventas
# --------------------------------------------------
st.subheader("📈 3. Distribución de los importes de venta")

fig_histograma = px.histogram(
    df_filtrado,
    x="ventas_totales",
    nbins=20,
    title="Frecuencia de los importes de venta",
    labels={
        "ventas_totales": "Importe de venta ($)",
        "count": "Número de registros"
    },
    color_discrete_sequence=["#B87942"],
    marginal="box",
    hover_data=["producto"]
)

fig_histograma.update_layout(
    template="plotly_white",
    height=480,
    margin=dict(l=20, r=20, t=70, b=30),
    xaxis_tickprefix="$",
    xaxis_tickformat=",.0f",
    yaxis_title="Número de registros"
)

st.plotly_chart(
    fig_histograma,
    use_container_width=True
)


# --------------------------------------------------
# 11. Vista previa interactiva del DataFrame filtrado
# --------------------------------------------------
st.divider()
st.subheader("🔎 Explora los datos")

mostrar_datos = st.checkbox(
    "Mostrar vista previa de los datos filtrados",
    value=False
)

if mostrar_datos:
    cantidad_filas = st.selectbox(
        "¿Cuántas filas deseas visualizar?",
        options=[5, 10],
        index=1
    )

    st.caption(
        f"Mostrando hasta {cantidad_filas} filas "
        f"de {len(df_filtrado):,} registros filtrados."
    )

    st.dataframe(
        df_filtrado.head(cantidad_filas),
        use_container_width=True,
        hide_index=True
    )

    # Permite descargar todos los datos filtrados
    csv_filtrado = df_filtrado.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="📥 Descargar todos los datos filtrados",
        data=csv_filtrado,
        file_name="ventas_filtradas.csv",
        mime="text/csv"
    )


# --------------------------------------------------
# 12. Pie de página
# --------------------------------------------------
st.divider()
st.caption(
    "☕ Dashboard de análisis de ventas | "
    "Python · Streamlit · Pandas · Plotly Express"
)
