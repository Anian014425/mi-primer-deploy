# ☕ Café Gourmet | Centro de Inteligencia

> **De los datos a las decisiones: descubre el potencial de cada venta.**

Dashboard web interactivo desarrollado con **Python, Streamlit y Plotly Express** para analizar las ventas de una cafetería gourmet mediante indicadores clave, filtros dinámicos y visualizaciones interactivas.

## 🌐 Aplicación desplegada en Render

**👉 https://mi-primer-deploy-b2as.onrender.com/**

La aplicación puede probarse directamente desde el navegador, sin instalar nada.

> ⏳ Render (plan gratuito) suspende el servicio tras un periodo sin uso. Si la página tarda en cargar, espera entre 30 y 60 segundos a que el servidor se reactive.

## ✨ Descripción del proyecto

El dashboard responde preguntas de negocio como:

- ☕ ¿Qué productos generan mayores ingresos?
- 🍰 ¿Qué categorías tienen mayor participación en las ventas?
- 📈 ¿Cómo se distribuyen los importes de venta?
- 🎯 ¿Cómo cambian los resultados al filtrar por categoría, producto, sucursal o método de pago?

### Funcionalidades

- **📌 Indicadores KPI:** ventas totales, número de registros y venta promedio.
- **🎛️ Filtros interactivos:** categoría, producto, sucursal, método de pago y ventas con descuento.
- **🏆 Gráfico de barras:** ventas por producto.
- **🍩 Gráfico de dona:** participación de cada categoría.
- **📊 Histograma con boxplot:** distribución de los importes de venta.
- **🔎 Vista previa:** primeras 5 o 10 filas de los datos filtrados.
- **📥 Exportación:** descarga de los registros filtrados en CSV.

## 📁 Estructura del repositorio

```text
mi-primer-deploy/
├── app.py              # Aplicación Streamlit (dashboard)
├── EDA.ipynb           # Análisis Exploratorio de Datos
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Documentación
├── data/
│   ├── datos.csv       # Dataset de ventas usado por la app y el EDA
│   └── ejemplo.csv     # Archivo de práctica (no lo usa la app)
├── script.py           # Script de práctica (no forma parte de la app)
└── script2.py          # Script de práctica con Seaborn (no forma parte de la app)
```

### ¿Cómo se manejan los archivos?

| Archivo | Función |
|---|---|
| `app.py` | Punto de entrada de la aplicación. Lee `data/datos.csv` con una ruta relativa, convierte tipos (fechas y numéricos), valida las columnas necesarias y construye los filtros, KPIs y gráficos. |
| `data/datos.csv` | Fuente de datos única: 150 ventas (enero a marzo de 2026) con 17 columnas. La app espera encontrarlo exactamente en esta ruta y con este nombre. |
| `EDA.ipynb` | Exploración del dataset previa al desarrollo: estructura, tipos de datos, faltantes, duplicados, estadísticas, distribuciones, correlaciones y conclusiones que justifican el diseño del dashboard. |
| `requirements.txt` | Librerías que Render instala al desplegar y que se necesitan para ejecutar la app y el notebook. |

### Dataset (`data/datos.csv`)

| Columna | Descripción |
|---|---|
| `id_venta` | Identificador único de la venta |
| `fecha_venta`, `dia_semana` | Fecha y día de la venta |
| `sucursal` | Roma Norte, Condesa o Polanco |
| `id_cliente` | Identificador del cliente |
| `producto`, `categoria` | Producto vendido y su categoría |
| `precio_unitario`, `cantidad` | Precio por unidad (MXN) y unidades |
| `ventas_totales`, `costo_total` | Importe cobrado y costo (MXN) |
| `metodo_pago` | Tarjeta, Efectivo, Transferencia o Billetera digital |
| `satisfaccion` | Calificación del cliente de 1 a 5 |
| `tiempo_preparacion_min` | Minutos de preparación |
| `es_cliente_frecuente`, `es_pedido_para_llevar`, `tiene_descuento` | Indicadores `true`/`false` |

## 🔍 Análisis Exploratorio de Datos (EDA)

Antes de construir la aplicación se exploró el dataset en [`EDA.ipynb`](EDA.ipynb). Principales hallazgos:

- El dataset no tiene valores faltantes ni duplicados; solo se convierte `fecha_venta` a tipo fecha.
- Las diferencias entre `precio × cantidad` y `ventas_totales` se explican por los descuentos (13% de las ventas, ~9% de descuento).
- El importe por venta tiene sesgo a la derecha (promedio $113.18 vs. mediana $90.00), impulsado sobre todo por la cantidad de unidades.
- *Café* es la categoría con más ingresos (33.6%) y *Cold brew* el producto más vendido en importe.
- *Roma Norte* lidera en ingresos por volumen; *Polanco* tiene el ticket promedio más alto.

Estos hallazgos definieron los filtros, KPIs y gráficos del dashboard.

## ⚙️ Cómo ejecutar el proyecto localmente

### 1. Requisitos

- [Python](https://www.python.org/downloads/) 3.10 o posterior
- [Git](https://git-scm.com/downloads)

### 2. Clonar el repositorio

```bash
git clone https://github.com/Anian014425/mi-primer-deploy.git
cd mi-primer-deploy
```

### 3. Crear y activar un entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
streamlit run app.py
```

Abre en el navegador la dirección que indique la terminal (normalmente `http://localhost:8501`).

### 6. Abrir el EDA

```bash
python -m pip install notebook
jupyter notebook EDA.ipynb
```

También puede abrirse directamente en VS Code con la extensión de Jupyter, o verse en GitHub con sus resultados ya guardados.

## ☁️ Despliegue en Render

La aplicación se desplegó como **Web Service** conectado a este repositorio de GitHub:

| Configuración | Valor |
|---|---|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |

Cada `git push` a la rama `main` vuelve a desplegar la aplicación automáticamente.

## 🧰 Tecnologías

| Tecnología | Uso |
|---|---|
| 🐍 Python | Lógica de la aplicación |
| 🖥️ Streamlit | Interfaz web interactiva |
| 🧮 Pandas | Carga, limpieza y filtrado de datos |
| 📊 Plotly Express | Gráficos interactivos del dashboard |
| 📉 Matplotlib / Seaborn | Visualizaciones del EDA |
| ☁️ Render | Despliegue de la aplicación |
| 🧑‍💻 Git y GitHub | Control de versiones |

---

**Desarrollado con ☕, 🐍 Python y 📊 pasión por los datos.**
