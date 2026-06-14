import streamlit as st
#Incluir titutlo
st.title("Proyecto final Diploma BI")
#incluir titulo en una barra lateral
st.sidebar.title("Parámetros")

st.image("logophyton.png",width=250)
st.sidebar.image("logoDMC.png",width=120)

st.write("Elaborado por: Cesar Augusto Villarreal")

archivo=st.file_uploader("Cargue el archivo CSV o Excel")

if archivo is not None :
  if archivo.name.endswith(".CSV"):
        data=pd.read_csv(archivo)
        st.write(data)
  elif archivo.name.endswith(".xlsx"):
        data=pd.read_excel(archivo)
        st.writw(data)
  else :
  st.write("formato no valido")
