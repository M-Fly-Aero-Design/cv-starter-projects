# Auton Computer Vision Tutorial 2: Image Thresholding
# Marcus Chung (marcusvc@umich.edu)
# 2024-06

import cv2
import numpy as np

# Constants
MAX_VALUE = 255
MAX_VALUE_H = 360 // 2 - 1
MAX_VALUE_BLUR = 20

# Declare H, S, V starting values
# H: (0, 180)  S: (0, 255)  V: (0, 255)
H_low = 0
S_low = 0
V_low = 0
H_high = MAX_VALUE_H
S_high = MAX_VALUE
V_high = MAX_VALUE
blur_strength = 0

# Trackbar names
H_low_name = "Low H"
S_low_name = "Low S"
V_low_name = "Low V"
H_high_name = "High H"
S_high_name = "High S"
V_high_name = "High V"
blur_name = "Blur"

window_name = "Auton CV Tutorial 2: Image Thresholding"

# Functions to read trackbar values on update
def on_H_low_update(val):
    global H_low
    H_low = min(val, H_high - 1)
    cv2.setTrackbarPos(H_low_name, window_name, H_low)


def on_H_high_update(val):
    global H_high
    H_high = max(val, H_low + 1)
    cv2.setTrackbarPos(H_high_name, window_name, H_high)
    

def on_S_low_update(val):
    global S_low
    S_low = min(val, S_high - 1)
    cv2.setTrackbarPos(S_low_name, window_name, S_low)


def on_S_high_update(val):
    global S_high
    S_high = max(val, S_low + 1)
    cv2.setTrackbarPos(S_high_name, window_name, S_high)
    
    
def on_V_low_update(val):
    global V_low
    V_low = min(val, V_high - 1)
    cv2.setTrackbarPos(V_low_name, window_name, V_low)


def on_V_high_update(val):
    global V_high
    V_high = max(val, V_low + 1)
    cv2.setTrackbarPos(V_high_name, window_name, V_high)
    
    
def on_blur_update(val):
    global blur_strength
    blur_strength = val
    

# Limits image size
def standard_scale(img):
    max_H, max_W = 720 // 2, 1280 // 2
    H, W, _ = img.shape
    if H > max_H and H * 16 / 9 >= W:
        img = cv2.resize(img, (int(max_H * W / H), max_H))
    elif W > max_W and W * 9 / 16 >= H:
        img = cv2.resize(img, (max_W, int(max_W * H / W)))
    return img


# Create window and trackbars
cv2.namedWindow(window_name)
cv2.createTrackbar(H_low_name, window_name, H_low, MAX_VALUE_H, on_H_low_update)
cv2.createTrackbar(H_high_name, window_name, H_high, MAX_VALUE_H, on_H_high_update)
cv2.createTrackbar(S_low_name, window_name, S_low, MAX_VALUE, on_S_low_update)
cv2.createTrackbar(S_high_name, window_name, S_high, MAX_VALUE, on_S_high_update)
cv2.createTrackbar(V_low_name, window_name, V_low, MAX_VALUE, on_V_low_update)
cv2.createTrackbar(V_high_name, window_name, V_high, MAX_VALUE, on_V_high_update)
cv2.createTrackbar(blur_name, window_name, blur_strength, MAX_VALUE_BLUR, on_blur_update)

# Read image
filename = "umich.jpg"
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = standard_scale(img)

# Runs until the user quits
while True:
    img_copy = img
    kernel = blur_strength * 2 + 1
    
    # Blur the image
    img_blur = cv2.GaussianBlur(img_copy, (kernel, kernel), 0)
    
    # Threshold images based on H, S, V
    img_threshold = cv2.inRange(img_blur, (H_low, S_low, V_low), (H_high, S_high, V_high))
    
    # Show image and mask side-by-side
    img_blur = cv2.cvtColor(img_blur, cv2.COLOR_HSV2BGR)
    img_threshold_3_channels = cv2.cvtColor(img_threshold, cv2.COLOR_GRAY2BGR)
    img_stack = np.hstack((img_blur, img_threshold_3_channels))
    cv2.imshow(window_name, img_stack)
    
    # Close window with 'q', save mask with 's'
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite("final_threshold.jpg", img_threshold)
    
cv2.destroyAllWindows()    
