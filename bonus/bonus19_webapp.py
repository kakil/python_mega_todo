import streamlit as st
from PIL import Image


with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input('camera')
    # print(camera_image)

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)

st.write("<br>", unsafe_allow_html=True)
st.text("Upload Image")
upload_image = st.file_uploader("Upload Image")

if upload_image:

    img = Image.open(upload_image)
    gray_img = img.convert("L")
    st.image(gray_img)

