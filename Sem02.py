import streamlit as st

#Inicalizacion de variables

usuarios = []

#Funcion para agregar un usuario
def agregar_usuario(nombre):
    usuarios.append(nombre)
    st.success(f"Usuario {nombre} agregado.")

#Funcion para mostrar usuarios
def mostrar_usuarios():
    if usuarios:
        st.write("Lista de usuarios:")
        for usuario in usuario:
            st.white(f"- {usuario}")
    else:
        st.warning("No hay usuarios registrados.")

#Menu Principal
st.title("Gestion de Usuarios")

opcion = st.selectbox("Selecciona una opcion", ["Agregar Usuario", "Mostrar Usuario"])

if opcion == "Agregar Usuario":
    nombre = st.text_input("Nombre del Usuario")
    if st.button("Agregar"):
        if nombre:
            agregar_usuario(nombre)
        else:
            st.error("El nombre no puede estar vacio")
elif opcion == "Mostrar Usuarios":
    mostar_usuarios()