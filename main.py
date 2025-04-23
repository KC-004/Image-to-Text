from PIL import Image, ImageEnhance
import pytesseract

from tkinter import filedialog

# Optional: Specify tesseract executable path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-ocr\tesseract.exe"


def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path).convert('L')

        enhancer = ImageEnhance.Sharpness(image)
        res = enhancer.enhance(3)

        enhancer = ImageEnhance.Contrast(res)
        img = enhancer.enhance(2)
        img.save("modified_img.png")
        text = pytesseract.image_to_string(img, lang="eng")
        return text.strip()
    except Exception as e:
        return f"Error: {e}"


def get_file_path():
    print("....Getting file path.")
    file_path = filedialog.askopenfilename()
    print(file_path)
    return file_path


def img_to_text():
    image_path = get_file_path()
    extracted_text = extract_text_from_image(image_path)
    f = open("Text.txt", 'w')
    print("....writing.")
    f.write(extracted_text)
    f.close()
    print("....Completed!")


img_to_text()
