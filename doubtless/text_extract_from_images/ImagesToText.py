import os
import pytesseract
import csv
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    
    image = Image.open(image_path)

    
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text

def process_image_folder(folder_path):
    
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    extracted_texts = []
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        extracted_text = extract_text_from_image(image_path)
        extracted_texts.append(extracted_text)

    return extracted_texts

def save_to_csv(data, csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Extracted Text'])
        writer.writerows([[text] for text in data])


folder_path = r"C:\Users\sanch\confessionmsit_"


csv_path = r"C:\Users\sanch\coding,tech,development\projects\doubtless\text_extract_from_images\confessionText.csv"

extracted_texts = process_image_folder(folder_path)
save_to_csv(extracted_texts, csv_path)
