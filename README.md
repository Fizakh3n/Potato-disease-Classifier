# Potato Disease Classifier

An end-to-end deep learning project to classify potato leaf diseases using a Convolutional Neural Network (CNN), with Streamlit-ready interface..

---

## ➤ Project Summary

- Built a CNN-based image classifier to detect three categories of potato leaf status:
  - Early Blight
  - Late Blight
  - Healthy
- Achieved 92.5% training accuracy and 94.6% validation accuracy
- Streamlit app interface created for easy deployment (not yet deployed).
---

## ➤ Dataset

- Image dataset with three labeled classes: Early Blight, Late Blight, and Healthy
- Sourced from Kaggle
- [Dataset] (https://www.kaggle.com/datasets/hafiznouman786/potato-plant-diseases-data)
---

## ➤ Model Architecture

- 3 Convolutional layers with ReLU activation
- MaxPooling after each Conv layer
- Flatten + Dense layers with dropout
- Final Softmax layer for classification

---

## ➤ Preprocessing

- Images resized to 150x150
- Normalized pixel values
- Applied data augmentation using ImageDataGenerator

---

## ➤ Results

- Training Accuracy: 92.5%
- Validation Accuracy: 94.6%
- Model tested on unseen images via UI

---
## ➤ Streamlit Integration

- Streamlit interface includes:
  - Image upload feature
  - Real-time prediction with confidence score
- Can be run using:
  ```bash
  streamlit run app.py
  ```
  *(Model is not hosted yet, but ready for deployment)*


  
## ➤ How to Use
Clone the repository

Install dependencies:
<pre>
pip install -r requirements.txt
</pre>

Launch the app:
<pre>streamlit run app.py</pre>

## ➤ Key Learnings

End-to-end image classification pipeline.<br>

CNN architecture tuning and overfitting control.<br>

Dealing with real-world debugging (input shape mismatch, model compatibility).<br>

Preparing and testing Streamlit-based UI.<br>


Let me know if you'd like to include a `requirements.txt` too or add any specific project folder structure.

