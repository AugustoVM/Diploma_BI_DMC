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
# MÓDULO ANÁLISIS VISUAL
# ==============================

elif modulos == "Análisis visual":

    st.subheader("Análisis visual")

    if st.session_state.data is not None:

        import matplotlib.pyplot as plt
        import seaborn as sns

        data = st.session_state.data

        st.write("Dataset disponible para análisis visual:")
        st.dataframe(data)

        # Columnas numéricas
        lista_columna_numerica = data.select_dtypes(include="number").columns.tolist()

        # Columnas categóricas
        lista_columna_categorica = data.select_dtypes(include=["object", "category"]).columns.tolist()

        # ==========================
        # SELECCIÓN DE VARIABLES
        # ==========================

        if lista_columna_numerica:
            variable_numerica = st.selectbox(
                "Seleccione una columna numérica",
                lista_columna_numerica
            )
        else:
            st.info("No hay columnas numéricas en el dataset")

        if lista_columna_categorica:
            variable_categorica = st.selectbox(
                "Seleccione una columna categórica",
                lista_columna_categorica
            )
        else:
            st.info("No hay columnas categóricas en el dataset")

        st.markdown("---")

        # ==========================
        # SELECCIÓN DEL TIPO DE GRÁFICO
        # ==========================

        tipo_grafico = st.selectbox(
            "Seleccione el tipo de gráfico",
            ["Histograma", "Boxplot", "Gráfico de líneas", "Gráfico de dispersión", "Gráfico de barras"]
        )

        st.markdown("---")

        # ==========================
        # GENERACIÓN DE GRÁFICOS
        # ==========================

        fig, ax = plt.subplots(figsize=(8, 4))

        # HISTOGRAMA
        if tipo_grafico == "Histograma":
            sns.histplot(data[variable_numerica], kde=True, ax=ax)
            ax.set_title(f"Histograma de {variable_numerica}")

        # BOXPLOT
        elif tipo_grafico == "Boxplot":
            sns.boxplot(x=data[variable_numerica], ax=ax)
            ax.set_title(f"Boxplot de {variable_numerica}")

        # GRÁFICO DE LÍNEAS
        elif tipo_grafico == "Gráfico de líneas":
            ax.plot(data[variable_numerica])
            ax.set_title(f"Gráfico de líneas de {variable_numerica}")
            ax.set_xlabel("Índice")
            ax.set_ylabel(variable_numerica)

        # DISPERSIÓN
        elif tipo_grafico == "Gráfico de dispersión":
            otra_numerica = st.selectbox(
                "Seleccione otra columna numérica para el eje Y",
                lista_columna_numerica
            )
            sns.scatterplot(x=data[variable_numerica], y=data[otra_numerica], ax=ax)
            ax.set_title(f"Dispersión: {variable_numerica} vs {otra_numerica}")

        # BARRAS
        elif tipo_grafico == "Gráfico de barras":
            sns.barplot(x=data[variable_categorica], y=data[variable_numerica], ax=ax)
            ax.set_title(f"Barras: {variable_categorica} vs {variable_numerica}")
            plt.xticks(rotation=45)

        st.pyplot(fig)

    else:
        st.warning(
            "Primero debe cargar un dataset en el módulo 'Carga y perfil del dataset'."
        )
c
c
