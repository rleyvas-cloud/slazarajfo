import streamlit as st

# Orden de llenado de orbitales
orbitals = [
    ("1s", 2), ("2s", 2), ("2p", 6),
    ("3s", 2), ("3p", 6), ("4s", 2),
    ("3d", 10), ("4p", 6), ("5s", 2),
    ("4d", 10), ("5p", 6), ("6s", 2),
    ("4f", 14), ("5d", 10), ("6p", 6),
    ("7s", 2), ("5f", 14), ("6d", 10), ("7p", 6)
]

def configuracion_electronica(Z):
    config = ""
    for orbital, capacidad in orbitals:
        if Z <= 0:
            break
        electrones = min(Z, capacidad)
        config += f"{orbital}^{electrones} "
        Z -= electrones
    return config.strip()

# Interfaz Streamlit
st.title("Configuración Electrónica")

Z = st.number_input("Número de protones (Z):", min_value=1, max_value=118)

if st.button("Calcular"):
    resultado = configuracion_electronica(Z)
    st.write(f"Configuración electrónica: {resultado}")
