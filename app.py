# Importamos Streamlit para crear la aplicación web
import streamlit as st

# Importamos Pandas para leer archivos CSV y Excel
import pandas as pd


# ==============================
# CONFIGURACIÓN DE SESSION STATE
# ==============================

# Guardamos el dataset cargado
if "data" not in st.session_state:
    st.session_state.data = None

# Guardamos el nombre del archivo cargado
if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None


# ==============================
# TÍTULO E IMÁGENES
# ==============================

st.title("Proyecto Final Diploma BI")
st.sidebar.title("Parámetros")

st.image("logophyton.png", width=500)
st.sidebar.image("logoDMC.png", width=100)

st.write("Elaborado por: Carlos Carrillo")


# ==============================
# MENÚ DE MÓDULOS
# ==============================

modulos = st.sidebar.selectbox(
    "Seleccione un módulo",
    ["Home", "Carga y perfil del dataset", "Procesamiento de datos", "Análisis visual"]
)


# ==============================
# MÓDULO HOME
# ==============================

if modulos == "Home":

    st.write("Bienvenido a la aplicación")

    if st.session_state.data is not None:
        st.success(f"Dataset cargado: {st.session_state.nombre_archivo}")
    else:
        st.info("Aún no se ha cargado ningún dataset.")


# ==============================
# MÓDULO CARGA Y PERFIL
# ==============================

elif modulos == "Carga y perfil del dataset":

    st.subheader("Carga y perfil del dataset")

    archivo = st.file_uploader(
        "Cargue el archivo Excel o CSV",
        type=["csv", "xlsx"]
    )

    if archivo is not None:

        st.session_state.nombre_archivo = archivo.name

        if archivo.name.endswith(".csv"):
            st.session_state.data = pd.read_csv(archivo)

        elif archivo.name.endswith(".xlsx"):
            st.session_state.data = pd.read_excel(archivo)

        else:
            st.error("Formato no válido")

        st.success("Archivo cargado correctamente")

    if st.session_state.data is not None:

        st.write(f"Archivo actual: **{st.session_state.nombre_archivo}**")

        st.subheader("Vista previa del dataset")
        st.dataframe(st.session_state.data)

        st.subheader("Perfil básico del dataset")

        st.write("Filas:", st.session_state.data.shape[0])
        st.write("Columnas:", st.session_state.data.shape[1])

        st.write("Columnas del dataset:")
        st.write(st.session_state.data.columns.tolist())

        st.write("Tipos de datos:")
        st.write(st.session_state.data.dtypes)

        st.write("Valores nulos por columna:")
        st.write(st.session_state.data.isnull().sum())

        st.write("Estadística descriptiva:")
        st.write(st.session_state.data.describe())

        if st.button("Eliminar dataset cargado"):
            st.session_state.data = None
            st.session_state.nombre_archivo = None
            st.rerun()

    else:
        st.write("Por favor cargue su archivo.")


# ==============================
# MÓDULO PROCESAMIENTO DE DATOS
# ==============================

elif modulos == "Procesamiento de datos":

    st.subheader("Procesamiento de datos")

    if st.session_state.data is not None:

        data = st.session_state.data

        st.write("Dataset disponible para procesamiento:")
        st.dataframe(data)

        st.write("Valores nulos por columna:")
        st.write(data.isnull().sum())

    else:
        st.warning(
            "Primero debe cargar un dataset en el módulo "
            "'Carga y perfil del dataset'."
        )


# ==============================
# MÓDULO ANÁLISIS VISUAL
# ==============================

elif modulos == "Análisis visual":

    st.subheader("Análisis visual")

    if st.session_state.data is not None:

        data = st.session_state.data

        st.write("Dataset disponible para análisis visual:")
        st.dataframe(data)

        # Columnas numéricas
        lista_columna_numerica = data.select_dtypes(include="number").columns.tolist()

        if lista_columna_numerica:
            variable_numerica = st.selectbox(
                "Seleccione la columna numérica",
                lista_columna_numerica
            )
        else:
            st.info("No hay columnas numéricas en el dataset")

        # Columnas categóricas
        lista_columna_categorica = data.select_dtypes(include=["object", "category"]).columns.tolist()

        if lista_columna_categorica:
            variable_categorica = st.selectbox(
                "Seleccione la columna categórica",
                lista_columna_categorica
            )
        else:
            st.info("No hay columnas categóricas en el dataset")

    else:
        st.warning(
            "Primero debe cargar un dataset en el módulo "
            "'Carga y perfil del dataset'."
        )
