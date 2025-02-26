import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("potato_disease_model.h5")

# Define class labels
class_labels = ['Early Blight', 'Healthy', 'Late Blight']

# Streamlit UI
st.title("🥔 Potato Disease Classifier")
st.write("Upload an image of a potato leaf to check its health status.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)  
    
    # Preprocess the image
    img = img.resize((150, 150))  # Resize to match model input
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    result = class_labels[class_index]
    confidence = np.max(prediction) * 100

    # Display prediction
    st.success(f"Prediction: {result} ({confidence:.2f}%)")
    st.write("Confidence Level: {:.2f}%".format(confidence))
