import streamlit as st
#Incluir titutlo
st.title("Proyecto final Diploma BI")
#incluir titulo en una barra lateral
st.sidebar.title("Parámetros")

st.image("logophyton.png",width=250)
st.sidebar.image("logoDMC.png",width=150)

st.write("Elaborado por: Cesar Augusto Villarreal")

archivo=st.file_uploader("Cargué el archivo CSV o excel"
