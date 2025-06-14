import numpy as np
from tensorflow.keras.preprocessing.image import array_to_img
import os

# Create folders if not exist
folders = ['train/positive', 'train/negative', 'test/positive', 'test/negative']
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Generate dummy images for each folder
for folder in folders:
    for i in range(5):  # 5 images per folder
        dummy_img = np.random.rand(224, 224, 3) * 255
        img = array_to_img(dummy_img.astype('uint8'))
        img.save(f'{folder}/img{i}.jpg')

print("✅ Dummy images generated successfully.")
