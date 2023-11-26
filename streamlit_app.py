import streamlit as st
import firebase_storage
import house_evaluation
import house_damage

client_key = '79de00b7cd11c23d476c3a14567cb218edaf0c742f8b3946a993afaec1c33ea3'
multianalyze_model = 'https://property.restb.ai/v1/multianalyze'
multipredict_model = 'https://api-us.restb.ai/vision/v2/multipredict'

# Main title and description
st.title("Property Improver")


# Function to be executed when an image is clicked
def on_image_click(image_name):

    house_number = image_name.split(" ")[1]

    firebase_blob = firebase_storage.obtain_firebase_blob()
    # given house selected obtain images urls
    input_images = firebase_storage.obtain_images_path(firebase_blob, house_number)

    # Given images urls obtain json data (API use)
    house_data_json = house_evaluation.evaluate_images_using_API(multianalyze_model, client_key, input_images,
                                                                 save=True)
    # type = exterior, interior, bathroom, kitchen
    # Given json extract worst type
    score_dict, worst_type = house_evaluation.obtain_min_room_score(house_data_json)

    st.sidebar.write("Our software has scored your property's four room types as follows: ")
    for item in score_dict:
        st.sidebar.write("    - " + item + ": " + str(score_dict[item]))
    st.sidebar.write("The worst room type is: " + worst_type)

    # Given worst type extract images with this type
    worst_images = house_evaluation.obtain_worst_type_imgs(worst_type, house_data_json, input_images)
    # Evaluate each worst type image and obtain the three worst
    top_worst_images = house_evaluation.evaluate_worst_imgs(multianalyze_model, client_key, worst_images)

    st.sidebar.write("We have analyzed all the images of the " + worst_type + " type and the ones with the lowest"
                                                                                " scores are the following:")
    for image in top_worst_images:
        image_url = image
        st.sidebar.image(image_url, use_column_width=True)

    # Obtain damage state from worst images
    damage_state = house_damage.evaluate_damage(multipredict_model, client_key, top_worst_images)

    if damage_state == 0: st.sidebar.write("We haven't found relevant damages in the lowest scores images.")
    else:
        st.sidebar.write("We have found this relevant damages in the lowest scores images: ")
        for value in damage_state:
            st.sidebar.write("    - " + value)


# Grid of images
col1, col2 = st.columns(2)

# Image 1
with col1:
    image1_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-4.appspot.com/o/house1%2Fimg_1.jpg?alt=media&token=fa3f4d84-a2a9-42e0-83a2-9115b3d5e564"
    st.image(image1_url, use_column_width=True)
    if st.button("Property 1", use_container_width=True):
        on_image_click("Image 1")

# Image 2
with col2:
    image2_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-4.appspot.com/o/house1%2Fimg_10.jpg?alt=media&token=133093e1-8ffd-4770-b105-72865992ff89"
    st.image(image2_url, use_column_width=True)
    if st.button("Property 2", use_container_width=True):
        on_image_click("Image 2")

# Image 3
with col1:
    image3_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-4.appspot.com/o/house1%2Fimg_11.jpg?alt=media&token=eb261841-807c-4fb8-af78-50f92a2bc2aa"
    st.image(image3_url, use_column_width=True)
    if st.button("Property 3", use_container_width=True):
        on_image_click("Image 3")

# Image 4
with col2:
    image4_url = "https://firebasestorage.googleapis.com/v0/b/property-improver-4.appspot.com/o/house1%2Fimg_12.jpg?alt=media&token=e8ba2a63-f9b2-4bde-afe1-8ed4e067341e"
    st.image(image4_url, use_column_width=True)
    if st.button("Property 4", use_container_width=True):
        on_image_click("Image 4")
