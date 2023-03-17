import pytesseract
import shutil
import os
import random
import cv2
import numpy as np
from PIL import Image

# import module
from pdf2image import convert_from_path
from tqdm import tqdm
import tempfile

fname = "TU DIEN VIET-BAHNAR.pdf"

# Function to find the maximum value in a list
def find_max(lst):
    max_col = lst[0]
    index_max = 0
    for i in range(len(lst)):
        if lst[i] >= max_col:
            max_col = lst[i]
            index_max = i
    return index_max


# Function to solve a system of two linear equations
def solver_SOE(x1, y1, x2, y2):
    if x1 == x2:
        return [1, x1, 0]
    else:
        a = (y1 - y2) / (x1 - x2)
        b = (x1 * y2 - x2 * y1) / (x1 - x2)
        return [a, b]


# Function to find the x-coordinate (horizontal coordinate) of the white line
def find_Index(vungchon):
    height = vungchon.shape[0]
    width = vungchon.shape[1]
    lst = []
    for i in range(width):
        lst.append(0)

    for i in range(height):
        for j in range(width):
            if (vungchon[i][j] == np.array([255, 255, 255])).all():
                lst[j] += 1

    index = find_max(lst)
    print(index)
    return index


# Function to split the input image into two images
def split_image(input_dir, output_dir):
    # Read input image
    img = cv2.imread(input_dir)

    # Define regions of interest
    y11, y12 = 300, 500
    x11, x12 = 393, 827
    y21, y22 = 1090, 1290
    x21, x22 = 393, 750

    # Extract index of equation from each region
    vungchon1 = img[y11:y12, x11:x12]
    index1 = find_Index(vungchon1)

    vungchon2 = img[y21:y22, x21:x22]
    index2 = find_Index(vungchon2)

    # Solve the system of equations to find the separating line
    result = solver_SOE(index1 + x11, y11, index2 + x21, y22)

    # Extract image with content on the right and delete content on the left
    img1 = img.copy()
    if len(result) == 3:
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if j > result[1]:
                    img1[i][j] = np.array([255, 255, 255])
    elif len(result) == 2:
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                if j > ((i - result[1]) / result[0]):
                    img1[i][j] = np.array([255, 255, 255])
    # Save the resulting image
    output_dir1 = os.path.join(output_dir, dname, input_dir[input_dir.rfind('/') + 1:-4] + '_1.jpg')
    cv2.imwrite(output_dir1, img1)

    # Extract image with content on the left and delete content on the right
    img2 = img.copy()
    if len(result) == 3:
        for i in range(img2.shape[0]):
            for j in range(img2.shape[1]):
                if j <= result[1]:
                    img2[i][j] = np.array([255, 255, 255])
    elif len(result) == 2:
        for i in range(img2.shape[0]):
            for j in range(img2.shape[1]):
                if j <= ((i - result[1]) / result[0]):
                    img2[i][j] = np.array([255, 255, 255])
    # Save the resulting image
    output_dir2 = os.path.join(output_dir, dname, input_dir[input_dir.rfind('/') + 1:-4] + '_2.jpg')
    cv2.imwrite(output_dir2, img2)


dname = fname[:-4]

# Part 1.Convert PDF into Image"-------------------------------------------

if os.path.exists(dname):
    shutil.rmtree(dname)
else : os.mkdir(dname)

# Store Pdf with convert_from_path function
with tempfile.TemporaryDirectory() as path:
    images = convert_from_path(fname, output_folder=path)

    for i in tqdm(range(len(images))):
        # Save pages as images in the pdf
        images[i].save(dname + "/page_%03d.jpg" % i, 'JPEG')
# End 1--------------------------------------------------------------------------------
split_dir = "Split Image"

##2. Split each image into 2 image ------------------------------------------------------------------

list_pages0 = sorted(os.listdir(dname))
print(list_pages0)
# # # # #split_dir = dname + "_split"
if os.path.exists(split_dir):
    shutil.rmtree(split_dir)
else: os.mkdir(split_dir)

for pfile in tqdm(list_pages0):
    split_image(dname + "/" + pfile, split_dir)

##End 2-------------------------------------------------------------------------

#3. Using OCR Tesseract to extract text----------------------------------------
list_pages = sorted(os.listdir(split_dir))
convert_dir = dname + "_converted"
# !rm -rf $convert_dir
# !mkdir $convert_dir
shutil.rmtree(convert_dir)
os.mkdir(convert_dir)

# custom_oem_psm_config = r'-l vie --oem 3 --psm 6 --nice 2'
# custom_oem_psm_config = r'-l vie --oem 1 --psm 4 --nice 2'
# custom_oem_psm_config = '-l vie --oem 3 --psm 6'
custom_oem_psm_config = '-l vie --oem 1 --psm 4'

for pfile in tqdm(list_pages):
  extractedInformation = pytesseract.image_to_string(Image.open(os.path.join(split_dir, pfile)), config=custom_oem_psm_config)
#   extractedInformation = pytesseract.image_to_string(Image.open(os.path.join(dname, pfile)), config=custom_oem_psm_config)
  with open(os.path.join(convert_dir, pfile.replace('jpg', 'txt')), "w", encoding="utf-8") as f:
    f.write(extractedInformation)

## End 3-------------------------------------------------------------------------------------------------------------------------