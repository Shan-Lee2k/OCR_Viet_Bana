import cv2
import os
from tqdm import tqdm

inputDir = "Split Image"
outputDir = "Binary Image"
arr = os.listdir(inputDir)  # list image

# Function gray scale
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


for i in tqdm(range(len(arr))):
    file = arr[i]
    im_gray = cv2.imread(inputDir + '/' + file, cv2.IMREAD_GRAYSCALE)
    # Binarisation
    thresh, im_bw = cv2.threshold(im_gray, 125, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(outputDir, file), im_bw)