# OCR_Viet_Bana
Convert image from pdf file to text using OCR Tesseract and some technique to improve quality OCR.
Perform Text Detection và Extraction based on Viet_Bana Dictionary
Skills:

- Python
- Tesseract
- OpenCV
- and some other Python libraries
## HOW TO USE THIS PROJECT
Run command:
```
python split_image.py
```
- After run split_image.py file, We will have three folder:
    + Folder "TU DIEN VIET-BAHNAR" perform task 1: Convert file PDF into every single image.
    ![page_006](https://user-images.githubusercontent.com/120365693/225835125-830f57ad-671c-4535-9137-278c75ba6917.jpg)
    + Folder "Split Image" perform task 2: Split image into 2 image contains text. Because OCR is not good enough when perfroming on dictionary.
    ![page_006_1](https://user-images.githubusercontent.com/120365693/225852152-6d2af0b6-089b-41d0-9e6c-7700966555f5.jpg)

    + Folder TU DIEN VIET-BAHNAR_converted : Extract text from folder "Split Image"

# BINARIZATION IMAGE TO REMOVE NOISE TO IMPROVE QUALITY OCR
- Create an empty folder "Binary Image"
Run command:
```
python binary_image.py
```    
After run this file, We should have a folder with all image are converted into binary.
This helps remove noise from image and improve OCR quality.

# FINAL : USING OCR TESSERACT TOOL AND POST-PROCESSING
- Create two empty folder "Final" and "Final corrected"
+ Folder Final : Contains result OCR on folder Binary Image.
+ Folder "Final corrected": This folder contains the final result. The task is to find and replace all common mistakes.
+ Run command:
```
python ocr_binary_img.py
``` 
