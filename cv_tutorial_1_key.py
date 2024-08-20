# Auton Computer Vision Tutorial 1: Image Filters
# Marcus Chung (marcusvc@umich.edu)
# 2024-06

# Import OpenCV and numpy modules
import cv2
import numpy as np

# Define variables
MAX_VALUE = 20

blur = 0
sharpen = 0
grayscale = 0

blur_name = "blur"
sharpen_name = "Sharpen"
grayscale_name = "Grayscale"

window_name = "Auton CV Tutorial 1: Image Filters"


def on_trackbar_update(_):
    global blur, sharpen, grayscale
    blur = cv2.getTrackbarPos(blur_name, window_name)
    sharpen = cv2.getTrackbarPos(sharpen_name, window_name)
    grayscale = cv2.getTrackbarPos(grayscale_name, window_name)


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
cv2.createTrackbar(blur_name, window_name, blur, MAX_VALUE, on_trackbar_update)
cv2.createTrackbar(sharpen_name, window_name, sharpen, MAX_VALUE, on_trackbar_update)
cv2.createTrackbar(grayscale_name, window_name, grayscale, MAX_VALUE, on_trackbar_update)

# Read image
filename = "mfly.png"
img = cv2.imread(filename)
img = standard_scale(img)

# Runs until the user quits
while True:
    """
    BLUR
    """
    img_copy = img
    kernel = blur * 2 + 1
    
    # Blur the image
    img_modified = cv2.GaussianBlur(img_copy, (kernel, kernel), 0)
    
    """
    SHARPEN
    """
    # Create the sharpening kernel
    center = sharpen + 1
    edge = (1 - center) / 8
    kernel = np.array([[edge, edge, edge],
                       [edge, center, edge],
                       [edge, edge, edge]])
    
    # Sharpen the image
    img_modified = cv2.filter2D(img_modified, -1, kernel)
    
    """
    GRAYSCALE
    """
    # Grayscale
    gray = cv2.cvtColor(img_modified, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    # Blend gray with original
    blend = grayscale / MAX_VALUE
    img_modified = cv2.addWeighted(gray, blend, img_modified, 1 - blend, 0)
    
    """
    IMAGE PREVIEW
    """
    # Show image and mask side-by-side
    img_stack = np.hstack((img, img_modified))
    cv2.imshow(window_name, img_stack)
    
    # Close window with 'q', save mask with s'
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite("final_image.jpg", img_modified)

cv2.destroyAllWindows()
