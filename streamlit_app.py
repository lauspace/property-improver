import streamlit as st

# Título principal y descripción
st.title("Mi Streamlit App")
st.write("Esta es una descripción para mi aplicación.")

# Función que se ejecutará al pulsar una imagen
def on_image_click(image_name):
    st.write(f"¡Has pulsado la imagen {image_name}!")

# Grid de imágenes
col1, col2 = st.beta_columns(2)

# Imagen 1
with col1:
    image1 = st.image("path/to/image1.jpg", caption="Imagen 1", use_column_width=True)
    if image1.button("Pulsa para ejecutar"):
        on_image_click("Imagen 1")

# Imagen 2
with col2:
    image2 = st.image("path/to/image2.jpg", caption="Imagen 2", use_column_width=True)
    if image2.button("Pulsa para ejecutar"):
        on_image_click("Imagen 2")

# Imagen 3
with col1:
    image3 = st.image("path/to/image3.jpg", caption="Imagen 3", use_column_width=True)
    if image3.button("Pulsa para ejecutar"):
        on_image_click("Imagen 3")

# Imagen 4
with col2:
    image4 = st.image("path/to/image4.jpg", caption="Imagen 4", use_column_width=True)
    if image4.button("Pulsa para ejecutar"):
        on_image_click("Imagen 4")