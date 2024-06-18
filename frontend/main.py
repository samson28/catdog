import streamlit as st
from PIL import Image
import requests

# Streamlit App
st.title('Cat vs Dog Image Classifier')

uploaded_image = st.file_uploader("Upload Cat or Dog image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((200, 200))
        st.image(resized_img)

    with col2:
        if st.button('Classify'):
            # Reset the file pointer position to the start
            uploaded_image.seek(0)

            # Send POST request to the API using FormData
            response = requests.post("http://localhost:5000/classify", files={"image": uploaded_image})

            if response.status_code == 200:
                # Parse the JSON response
                resultat = response.json()
                st.success(f'Prediction: {resultat["message"]}')
            else:
                st.error(f'Error: {response.text}')
