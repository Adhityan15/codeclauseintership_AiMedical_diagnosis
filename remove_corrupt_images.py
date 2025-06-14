from PIL import Image
import os

# Set folders to scan
folders = ['train/positive', 'train/negative', 'test/positive', 'test/negative']

for folder in folders:
    folder_path = os.path.join(os.getcwd(), folder)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            img = Image.open(file_path)
            img.verify()
        except Exception as e:
            print(f"❌ Removing corrupt file: {file_path} — {e}")
            os.remove(file_path)
