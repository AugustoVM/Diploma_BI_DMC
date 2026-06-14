import streamlit as st
import pandas as pd

if "data" not in st.session_state:
    st.session_state.data = None

if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None

#Incluir titutlo
st.title("Proyecto final Diploma BI")
#incluir titulo en una barra lateral
st.sidebar.title("Parámetros")

st.image("logophyton.png",width=250)
st.sidebar.image("logoDMC.png",width=120)

st.write("Elaborado por: Cesar Augusto Villarreal")

modulos=st.sidebar.selectbox("Seleccione un modulo",["Home","Carga y perfil del dataset","Procesamiento de datos","Analisis visual"]) #es un modulo que me permitira mostrra un dspliegue de distitas eclecciones a traves de una lista

if modulos == "Home":
       st.write("Bienvenido a la aplicación, esta herramienta es una aplicación interactiva construida en Python con Streamlit. La aplicación permite cargar, validar, procesar y visualizar datos de manera dinámica. En resumen es un herramienta funcional, clara, ordenada y similar a un producto real de análisis exploratorio de datos. Las tecnologias usadas son las librerias Streamlist y Pandas")

       if st.session_state.data is not None:
           st.success(f"Dataset cargado: {st.session_state.nombre_archivo}")
       else:
           st.info("Aun no se ha cargado ningun dataset")

elif modulos == "Carga y perfil del dataset":
         
       archivo = st.file_uploader("Cargue el archivo excel o csv")
            
       if archivo is not None:
              st.session_state.nombre_archivo=archivo.name    
              if archivo.name.endswith(".csv"):
                 data = pd.read_csv(archivo)
                 st.write(data)
              elif archivo.name.endswith(".xlsx"):
                  data = pd.read_excel(archivo)
                  st.write(data)
              else: 
                   st.write("Formato no valido")
            
       else:
                st.write("Por favor cargue su archivo") 

elif modulos == "Procesamiento de datos":

    st.subheader("Procesamiento de datos")


    if st.session_state.data is not None:


        data = st.session_state.data


        st.write("Dataset disponible para procesamiento:")

        st.dataframe(data)


        st.write("Valores nulos por columna:")

        st.write(data.isnull().sum())

    else:
        st.warning("Primero debe cargar un dataset en el módulo 'Carga y perfil del dataset'.")

# ==============================

# MÓDULO ANÁLISIS VISUAL

# ==============================


elif modulos == "Análisis visual":

    st.subheader("Análisis visual")

    if st.session_state.data is not None:

        data = st.session_state.data

        st.write("Dataset disponible para análisis visual:")

        st.dataframe(data)

    else:

        st.warning("Primero debe cargar un dataset en el módulo 'Carga y perfil del dataset'.")
