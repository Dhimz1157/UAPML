import streamlit as st
import tensorflow as tf
import os
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import cv2

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Cache model loading to optimize performance
@st.cache_resource
def load_models():
    resnet_model = load_model("ResNet50V2_cv_gender_classification.h5", compile=False)
    vgg16_model = load_model("VGG16_cv_gender_classification.h5", compile=False)
    return resnet_model, vgg16_model

resnet_model, vgg16_model = load_models()

def preprocess_image(image):
    """Preprocess the input image to the required size and normalize it."""
    image = image.resize((224, 224))  # Resize image
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def predict_gender(model, image_array):
    """Make a prediction using the model and interpret the result."""
    prediction = model.predict(image_array)
    if prediction[0][0] >= 0.5:
        return "Male", prediction[0][0]
    else:
        return "Female", 1 - prediction[0][0]

# Initialize the Streamlit app
st.title("🌟 Gender Classification App")

# Main page design
st.markdown(
    """
    <style>
        .main {background-color: #f8f9fa;}
        .css-18e3th9 {padding: 2rem 1rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.write("## 📷 Take a photo or upload an image to classify gender.")

# Add model selection
st.write("### 🧠 Select a Model")
selected_model_name = st.radio("Choose a model for prediction:", ["ResNet50V2", "VGG16"], index=0)
selected_model = resnet_model if selected_model_name == "ResNet50V2" else vgg16_model

col1, col2 = st.columns(2)

with col1:
    st.write("### 📷 Capture from Camera")
    camera_image = st.camera_input("Take a photo")

    if camera_image is not None:
        image = Image.open(camera_image).convert('RGB')
        st.image(image, caption="Captured Image", use_container_width=True)

        if st.button("Predict from Camera Image"):
            with st.spinner("Processing..."):
                image_array = preprocess_image(image)
                label, confidence = predict_gender(selected_model, image_array)
                st.success(f"Predicted Gender: {label} (Confidence: {confidence:.2f}%)")

with col2:
    st.write("### 📤 Upload an Image")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Predict from Uploaded Image"):
            with st.spinner("Processing..."):
                image_array = preprocess_image(image)
                label, confidence = predict_gender(selected_model, image_array)
                st.success(f"Predicted Gender: {label} (Confidence: {confidence:.2f}%)")

# Footer
st.markdown("""---
Created with ❤️ by [DHIMZ1157]""")
