import streamlit as st

# Título principal y descripción
st.title("Mi Streamlit App")
st.write("Esta es una descripción para mi aplicación.")

# Función que se ejecutará al pulsar una imagen
def on_image_click(image_name):
    st.write(f"¡Has pulsado la imagen {image_name}!")

# Grid de imágenes
col1, col2 = st.columns(2)

# Imagen 1
with col1:
    image1 = st.image("https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_18.jpg?alt=media&token=278d1efd-9e57-4035-8656-8ffbdb28ee4e", caption="Imagen 1", use_column_width=True)
    if image1.button("Pulsa para ejecutar"):
        on_image_click("Imagen 1")

# Imagen 2
with col2:
    image2 = st.image("https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_18.jpg?alt=media&token=278d1efd-9e57-4035-8656-8ffbdb28ee4e", caption="Imagen 2", use_column_width=True)
    if image2.button("Pulsa para ejecutar"):
        on_image_click("Imagen 2")

# Imagen 3
with col1:
    image3 = st.image("https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_18.jpg?alt=media&token=278d1efd-9e57-4035-8656-8ffbdb28ee4e", caption="Imagen 3", use_column_width=True)
    if image3.button("Pulsa para ejecutar"):
        on_image_click("Imagen 3")

# Imagen 4
with col2:
    image4 = st.image("https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_18.jpg?alt=media&token=278d1efd-9e57-4035-8656-8ffbdb28ee4e", caption="Imagen 4", use_column_width=True)
    if image4.button("Pulsa para ejecutar"):
        on_image_click("Imagen 4")