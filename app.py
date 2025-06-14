from flask import Flask, request, render_template
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('model/cnn_model.h5')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    path = os.path.join('static/uploads', file.filename)
    file.save(path)

    processed = preprocess_image(path)
    prediction = model.predict(processed)[0][0]

    result = "Positive" if prediction > 0.5 else "Negative"
    confidence = round(prediction * 100 if prediction > 0.5 else (1 - prediction) * 100, 2)

    return render_template('result.html', result=result, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
