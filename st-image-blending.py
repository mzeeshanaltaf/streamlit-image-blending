import streamlit as st
import numpy as np
from PIL import Image
import cv2

page_title = "Image Blending"
page_icon = "🖼️"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

st.title(page_title)
st.write("This web app 🖥️ allows users to upload two images 🖼️🖼️ and blend them seamlessly. Users can adjust blending "
         "parameters like the alpha value 🎚️ to control the intensity of the blend. It provides an interactive way to "
         "combine images and visualize the results in real-time ⏱️")
st.subheader("Upload First Image")
uploaded_image_1 = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed",
                                    key="image_one")
st.subheader("Upload Second Image")
uploaded_image_2 = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed",
                                    key="image_two")

if uploaded_image_1 and uploaded_image_2 is not None:

    # Open the uploaded images and resize it
    image_1 = np.array(Image.open(uploaded_image_1))
    image_1 = cv2.resize(image_1, (512, 512))
    image_2 = np.array(Image.open(uploaded_image_2))
    image_2 = cv2.resize(image_2, (512, 512))

    st.subheader("Configuration")
    value = st.slider("Blending Ratio", 0, 100, 0, 5)
    beta = float(value/100)

    st.subheader("Result")
    col1, col2, col3 = st.columns(3, vertical_alignment="bottom")
    with col1:
        st.write(':blue[***Image 1***]')
        st.image(image_1)

    with col2:
        st.write(':blue[***Image 2***]')
        st.image(image_2)

    with col3:
        st.write(':blue[***Blended Image***]')
        blend_image = cv2.addWeighted(image_1, 1-beta, image_2, beta, 0)
        st.image(blend_image)
