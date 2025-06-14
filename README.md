# codeclauseintership_AiMedical_diagnosis
AI-Driven Medical Diagnosis Web App

# 🧠 AI-Driven Medical Diagnosis Web App

This is a Flask-based AI project that uses a **Convolutional Neural Network (CNN)** to diagnose diseases from medical images (like X-rays or MRIs). It's built to demonstrate the power of deep learning in medical image classification through a clean and user-friendly web interface.

## 🚀 Features

- Upload medical images for analysis (e.g., X-ray, CT, MRI)
- CNN model predicts presence of disease
- Returns result with confidence percentage
- Web interface using Flask, HTML, and CSS
- Trained using TensorFlow/Keras
- Dummy and real datasets supported

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **TensorFlow / Keras**
- **Flask**
- **NumPy**
- **Pillow (PIL)**
- HTML/CSS (basic frontend styling)

---

## 📁 Project Structure

AI-Medical-Diagnosis/
├── backend/
│ ├── app.py # Main Flask App
│ ├── model/
│ │ └── cnn_model.h5 # Trained CNN Model
│ ├── static/
│ │ └── uploads/ # Uploaded Images
│ └── templates/
│ ├── index.html # Upload Page
│ └── result.html # Result Display
│
├── dataset/ # (Optional) Training images
│
├── train_model.py # CNN model training script
├── requirements.txt # Required Python packages
