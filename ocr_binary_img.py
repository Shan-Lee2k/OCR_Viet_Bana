import pytesseract
import shutil
import os
import cv2
from tqdm import tqdm
import xlsxwriter
try:
    from PIL import Image
except ImportError:
    import Image

# PHẦN 1: CHẠY OCR TRÊN FOLDER Binary_Image
binary_img_dir = 'Binary Image'
outputFolder = 'Final'
img = sorted(os.listdir(binary_img_dir))
# Config for OCR tesseract
custom_oem_psm_config = '-l vie --oem 1 --psm 4'

for image in tqdm(img):
    extractedInformation = pytesseract.image_to_string(Image.open(os.path.join(binary_img_dir, image)),
                                                       config=custom_oem_psm_config)
    with open(os.path.join(outputFolder, image.replace('jpg', 'txt')), "w", encoding="utf-8") as f:
        f.write(extractedInformation)

# PHẦN 2: CHẠY FILE correction.py ĐỂ SỬA LỖI:
inputDir = 'Final'
path = os.listdir(inputDir)
print(path)

dict = {'ð': 'ơ̆', 'ẽ': 'ĕ', '¡': 'i', 'mĩ': 'mĭ', 'ợ': 'ơ', 'ồ': 'ŏ', 'ố': 'ơ̆', 'ỗ': 'ô̆', 'ơi': 'ơĭ', 'ổi': 'ôĭ',
        'š': 'ĕ', 'Š': 'ê̆', 'ủ': 'ŭ', 'Ủ': 'Ŭ', 'ũ': 'ŭ', 'Ũ': 'Ŭ'}

for txt in path:
    txtFile = open(inputDir + '/' + txt, encoding='utf-8', errors='ignore').read()
    print(txtFile)
    for original, replace in dict.items():
        txtFile = txtFile.replace(original, replace)
    with open(inputDir + '/' + 'corrected' + txt, 'w', encoding='utf-8') as f:
        f.write(txtFile)
# PHẦN 3: XUẤT KẾT QUẢ SANG FILE EXCEL:
# Sửa file excel.py với inputdir = "Output_OCR_BinaryImg" và sửa xuất file excel "Output_BinaryImg.xlsx"


