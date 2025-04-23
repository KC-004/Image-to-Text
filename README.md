# Image-to-Text
Extract the Text form an image file and  write it into a text file

Modules Used:

1. Tkinter  - for file dialog
2. pillow   - for image enhancing

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-ocr\tesseract.exe"  // Here we need to download the Tesseract-ocr file
                                                                              Give the the path were the tesseract.exe is in the 
                                                                              computer.


Working:
1. Get the file path (Image file)
2. Convert into grayscale and increase the sharpness and contrast using PIL Image and ImageEnhace.
3. Give the image to the pytesseract.image_to_string() method, it converts the imaage to text(string)
4. open an file in write mode and write the generated text to the file

Link: https://github.com/KC-004/Image-to-Text


