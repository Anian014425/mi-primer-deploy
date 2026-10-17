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
