# mi-primer-deploy

Aplicación interactiva en Python preparada para abrirse en Visual Studio Code y desplegarse en un servidor.

## Estructura

```text
mi-primer-deploy/
├── README.md
├── data/
│   └── ejemplo.csv
├── app.py
└── requirements.txt
```

## 1. Requisitos

- Python 3.10 o posterior recomendado
- Visual Studio Code
- Extensión Python de Microsoft para VS Code

## 2. Abrir el proyecto

Descomprime el proyecto y abre la carpeta `mi-primer-deploy` en Visual Studio Code:
**Archivo → Abrir carpeta**.

## 3. Crear y activar un entorno virtual

En la terminal integrada de VS Code, desde la carpeta del proyecto:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, puedes ejecutar los comandos usando el intérprete del entorno virtual directamente:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

## 4. Instalar las librerías

Con el entorno virtual activado:

```bash
python -m pip install -r requirements.txt
```

## 5. Ejecutar la aplicación

```bash
python app.py
```

La aplicación se abrirá en el navegador. Permite cargar un CSV propio o usar el archivo de ejemplo de `data/ejemplo.csv`, ver una vista previa y consultar estadísticas descriptivas.

## 6. Preparar un despliegue

Este proyecto usa Streamlit. Para desplegarlo en un servicio compatible con Streamlit, sube el repositorio a GitHub y configura:

- Archivo principal: `app.py`
- Dependencias: `requirements.txt`

Asegúrate de no subir archivos con datos privados o confidenciales.
#------------------------------------------------------------
# ☕ Café Gourmet | Centro de Inteligencia 📊

> **De los datos a las decisiones: descubre el potencial de cada venta.**

Una aplicación web interactiva desarrollada con **Python, Streamlit y Plotly Express** para analizar el rendimiento comercial de una cafetería gourmet mediante indicadores clave, filtros dinámicos y visualizaciones interactivas.

## ✨ Descripción del proyecto

**Café Gourmet | Centro de Inteligencia** transforma los datos de ventas en información visual que facilita la exploración de productos, categorías y patrones de consumo.

El dashboard está diseñado para responder preguntas de negocio como:

- ☕ ¿Qué productos generan mayores ingresos?
- 🍰 ¿Qué categorías tienen mayor participación en las ventas?
- 📈 ¿Cómo se distribuyen los importes de venta?
- 🎯 ¿Cómo cambian los resultados al filtrar por producto, sucursal o método de pago?

> 💡 **Objetivo:** demostrar cómo las herramientas de análisis y visualización de datos pueden apoyar decisiones comerciales más informadas.

## 🚀 Funcionalidades principales

- **📌 Indicadores KPI:** ventas totales, número de registros y venta promedio.
- **🎛️ Filtros interactivos:** exploración por categoría, producto, sucursal y método de pago.
- **🏆 Gráfico de barras:** comparación de ventas por producto.
- **🍩 Gráfico de dona:** participación de cada categoría en las ventas.
- **📊 Histograma:** análisis de la distribución de los importes de venta.
- **🔎 Vista previa:** consulta de las primeras 5 o 10 filas de los datos filtrados.
- **📥 Exportación de datos:** descarga de los registros filtrados en formato CSV.

## 🖥️ Vista general del dashboard

La aplicación permite interactuar con los gráficos, consultar valores al pasar el cursor y aplicar filtros para analizar diferentes segmentos de las ventas.

## 🧰 Tecnologías utilizadas

| Tecnología | Aplicación |
|---|---|
| 🐍 **Python** | Desarrollo y lógica de la aplicación |
| 🖥️ **Streamlit** | Construcción de la interfaz web interactiva |
| 🧮 **Pandas** | Manipulación, filtrado y análisis de datos |
| 📊 **Plotly Express** | Creación de visualizaciones interactivas |
| 🗂️ **CSV** | Fuente de datos para el dashboard |
| 🧑‍💻 **Git y GitHub** | Control de versiones y alojamiento del proyecto |

## 📁 Estructura del proyecto

```text
mi-primer-deploy/
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── datos.csv
```

- `app.py`: código fuente de la aplicación.
- `requirements.txt`: bibliotecas necesarias para ejecutar el proyecto.
- `README.md`: documentación e instrucciones de uso.
- `data/datos.csv`: conjunto de datos de ventas.

> ⚠️ El archivo CSV debe estar dentro de la carpeta `data` y llamarse exactamente `datos.csv`. No publiques información confidencial en repositorios públicos.

## ⚙️ Instalación y ejecución local

Sigue estos pasos para ejecutar el proyecto en tu computadora.

### 1. Requisitos previos

Instala [Python](https://www.python.org/downloads/) y [Git](https://git-scm.com/downloads).

Verifica que Python esté disponible desde la terminal:

```bash
python --version
```

### 2. Clona el repositorio

Sustituye `TU-USUARIO` por tu nombre de usuario de GitHub y utiliza la URL real de tu repositorio:

```bash
git clone https://github.com/TU-USUARIO/mi-primer-deploy.git
cd mi-primer-deploy
```

### 3. Crea un entorno virtual

**Windows — PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS o Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instala las dependencias

Asegúrate de que el archivo `requirements.txt` incluya las bibliotecas utilizadas por la aplicación:

```text
streamlit
pandas
plotly
```

Instálalas con:

```bash
python -m pip install -r requirements.txt
```

Si PowerShell bloquea la activación del entorno virtual, en Windows puedes instalar las dependencias sin activarlo mediante:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 5. Prepara el archivo de datos

Coloca el archivo CSV en la siguiente ruta:

```text
data/datos.csv
```

Verifica que el conjunto de datos contenga las columnas necesarias para el dashboard, entre ellas:

- `ventas_totales`
- `producto`
- `categoria`

Las funciones de filtrado por sucursal o método de pago requieren que esas columnas también existan en el archivo.

### 6. Ejecuta la aplicación

Con el entorno virtual activado, inicia Streamlit:

```bash
streamlit run app.py
```

Si no activaste el entorno virtual en Windows, puedes ejecutar:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Abre en tu navegador la dirección que muestre la terminal, normalmente:

```text
http://localhost:8501
```

¡Listo! 🎉 Ya puedes explorar el dashboard y analizar las ventas de la cafetería.

## 📈 Posibles mejoras futuras

- 📅 Incorporar análisis de ventas por fecha y periodo.
- 🏪 Comparar el rendimiento entre sucursales.
- 🎯 Agregar objetivos comerciales y seguimiento de KPIs.
- 👥 Explorar la satisfacción y recurrencia de clientes.
- ☁️ Publicar la aplicación para consultarla desde Internet.

## 👩‍💻 Competencias demostradas

Este proyecto permite mostrar experiencia práctica en:

- Preparación y análisis de datos con Pandas.
- Desarrollo de aplicaciones analíticas con Streamlit.
- Creación de gráficos interactivos con Plotly Express.
- Diseño de indicadores para apoyar decisiones de negocio.
- Documentación y organización de proyectos de Python.

## 🌟 Conclusión

> **Los datos cuentan historias; la visualización correcta ayuda a descubrirlas.**

Café Gourmet | Centro de Inteligencia combina tecnología, análisis y creatividad para explorar resultados, detectar patrones y formular nuevas preguntas de negocio.

---

**Desarrollado con ☕, 🐍 Python y 📊 pasión por los datos.**
