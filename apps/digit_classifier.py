import streamlit as st
from utils.image_utils import preprocess_image
from utils.model_utils import load_model, make_prediction
from PIL import Image

def display_digit_classifier():

    st.title('MNIST Digit Classifier')
    col1, col2, col3 = st.columns([1,2,1])

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        model = load_model('model/digit_classifier_model.keras')
        preprocessed_image = preprocess_image(image)
        predicted_class, confidence = make_prediction(model, preprocessed_image)
        st.success(f'The digit predicted is: {predicted_class} with a confidence of {confidence:.2f}')
        
        with col2:
            st.image(image, caption='Uploaded Image', width=400)
