import streamlit as st

# Main title and description
st.title("My Streamlit App")
st.write("This is a description for my application.")

# Function to be executed when an image is clicked
def on_image_click(image_name):
    # Store the clicked image name in the session state
    st.session_state.clicked_image = image_name

    # Redirect to a new page
    st.experimental_rerun()

# Check if we are on the new page
if hasattr(st.session_state, 'clicked_image'):
    # Display the clicked image name in a box
    st.info(f"You clicked on image {st.session_state.clicked_image}!")

else:
    # Grid of images
    col1, col2 = st.columns(2)

    # Image 1
    with col1:
        image1_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_18.jpg?alt=media&token=278d1efd-9e57-4035-8656-8ffbdb28ee4e"
        if st.button("Property 1", use_container_width=True):
            on_image_click("Image 1")
        st.image(image1_url, use_column_width=True)

    # Image 2
    with col2:
        image2_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_10.jpg?alt=media&token=9f7ee55e-a6e2-4e58-b104-56a7e8da6de6"
        if st.button("Property 2", use_container_width=True):
            on_image_click("Image 2")
        st.image(image2_url, use_column_width=True)

    # Image 3
    with col1:
        image3_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_11.jpg?alt=media&token=d5dc1a73-b70e-4065-8db8-0c09b52ef8a0"
        if st.button("Property 3", use_container_width=True):
            on_image_click("Image 3")
        st.image(image3_url, use_column_width=True)

    # Image 4
    with col2:
        image4_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-3.appspot.com/o/house3%2Fimg_12.jpg?alt=media&token=2dca730b-9ea2-4c5c-a3e0-83dec028e37a"
        if st.button("Property 4", use_container_width=True):
            on_image_click("Image 4")
        st.image(image4_url, use_column_width=True)
