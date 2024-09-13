# Computer Vision Starter Projects

Welcome! This readme will serve as an introduction to computer vision. Through these two tutorial projects, you'll have the opportunity to learn basic image processing techniques using common Python libraries such as OpenCV.

Please don't hesitate to ask any questions you may have along the way!  
Shoot me a message on slack, or via my email: marcusvc@umich.edu.


## Overview

Below is an overview of the files included in this repository.

`cv_tutorial_1_key.py`: The first tutorial, covering image processing techniques such as blurring, sharpening, and grayscaling.  
`cv_tutorial_2_key.py`: The second tutorial, covering image thresholding in the HSV color space.  
`README.md`: the file that you are currently reading.  
`mfly.png`: the photo we will be using through our tutorials.

Both `*_key.py` files are the answer keys to these projects. This tutorial will guide you through each, so please make an honest attempt at each one! Simply copying the code won't benefit anyone. I recommend writing out each line manually instead of just copying the code blocks - if you haven't already, this will get you used to writing code in Python, and you'll likely remember a little bit more! I also recommend trying to understand each line of code you write to the best of your ability. You're not expected to remember everything, but the honest effort will pay off in the long run!

The tutorial includes helpful resources, such as links to short tutorials using OpenCV functions. We will cover many of these concepts more in depth throughout our meetings, so don't worry if you feel overwhelmed! I encourage you to ask any questions you may have.

## Getting started

Before getting started on the tutorials, we need to go through the setup process. Some of the steps in the links below are extra, but you will use them if you plan on taking any main CS courses such as EECS280 and EECS281.


### WSL

If you don't have WSL 2 installed already, please follow these instructions: https://eecs280staff.github.io/tutorials/setup_wsl.html  

> [!TIP]
> This link is from the EECS280 website (https://eecs280staff.github.io/tutorials/), which contains a lot of great information beyond what we'll be referencing here.

From this point onwards, you should be doing everything in your Ubuntu bash shell. Your terminal should end with `$`. The code blocks in this tutorial will have my uniqname `marcusvc`, but yours will be different. It should look something like this:

```console
marcusvc:~$
```

### Python

Check that you have Python installed:

```console
marcusvc:~$ python3 --version
Python 3.10.12
```

If you don't see a version, run the following to install Python, pip, and venv.

```console
marcusvc:~$ sudo apt update && upgrade
marcusvc:~$ sudo apt install python3 python3-pip python3-venv
```

### Git

Git is a version control system for managing your source code. Check that you have Git installed:

```console
marcusvc:~$ git --version
git version 2.34.1
```

If you don't see a version, follow the instructions to install Git at this link: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

### VS Code
You are welcome to use any editor or IDE, but we recommend VS Code. Note that certain commands in this tutorial assume you are using VS Code. Install VS Code from the web: https://code.visualstudio.com/.

Next, install the WSL extension, which allows the VS Code backend to run in WSL.
1. Open the extensions panel form the left sidebar.
2. Search for 'WSL'.
3. Click 'Install'.

We also recommend installing the Python extension, by searching for Python in the extensions panel. This provides many useful features when developing in Python.


## Project setup

At this point, we should be ready to setup our environment. Start by creating a new directory. This will contain all of your computer vision code for the year.

```console
marcusvc:~$ mkdir -p ~/mfly_cv
marcusvc:~$ cd ~/mfly_cv
marcusvc:~/mfly_cv$ 
```
Next, clone this repository using git. You can check if the files have pulled successfully using `ls`.

```console
marcusvc:~/mfly_cv$ git clone https://github.com/M-Fly-Aero-Design/cv-starter-projects.git
marcusvc:~/mfly_cv$ cd cv-starter-projects
marcusvc:~/mfly_cv/cv-starter-projects$ 
marcusvc:~/mfly_cv/cv-starter-projects$ ls
README.md  cv_tutorial_1_key.py  cv_tutorial_2_key.py  mfly.png
```
Change to a new branch and name it your uniqname:

```console
marcusvc:~/mfly_cv/cv-starter-projects$ git checkout -b <your-uniqname>
```

### Creating a virtual environment

Using virtual environments is a recommended practice when working on Python projects. You can use a virtual environment to isolate your project tools and packages and avoid version conflicts with other projects. 

Verify that you are in your `cv-starter-projects` directory:

```console
marcusvc:~/mfly_cv/cv-starter-projects$ pwd
.../mfly_cv/cv-starter-projects
```

Then, create your virtual environment. This will create a directory called `env` that will store all of the packages and dependencies for your project.

```console
marcusvc:~/mfly_cv/cv-starter-projects$ python3 -m venv env
```

Then, activate your virtual environment. 

> [!IMPORTANT]
> **Make sure your virtual environment is activated whenever you are executing your Python scripts or installing new packages.**

You know if the virtual environment is activated if you see an `(env)` in front of each line in your terminal.

```console
marcusvc:~/mfly_cv/cv-starter-projects$ source env/bin/activate
(env) marcusvc:~/mfly_cv/cv-starter-projects$
```

It is good practice to deactivate your virtual environment once you are done working on your project. Deactivating should remove the `(env)` in your terminal. **For the remainder of this tutorial, make sure your virtual environment remains activated.**

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ deactivate
marcusvc:~/mfly_cv/cv-starter-projects$

// Make sure you are in your virtual environment for the remainder of this tutorial!
marcusvc:~/mfly_cv/cv-starter-projects$ source env/bin/activate
(env) marcusvc:~/mfly_cv/cv-starter-projects$
```

### Installing Python libraries

Throughout our projects, we may use packages that are not part of the standard Python library. These tutorials will use two common packages: `OpenCV` and `numpy`. To use these packages, we need to install them using `pip`, which is a package management system.

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ pip install opencv-python
(env) marcusvc:~/mfly_cv/cv-starter-projects$ pip install numpy
```

### Creating files

Let's create the two files that will contain our code for the tutorials. You can create a file using the `touch` command. You can check that these files have been created using `ls`.

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ touch cv_tutorial_1.py
(env) marcusvc:~/mfly_cv/cv-starter-projects$ touch cv_tutorial_2.py
(env) marcusvc:~/mfly_cv/cv-starter-projects$ ls
README.md  cv_tutorial_1.py  cv_tutorial_1_key.py  cv_tutorial_2.py  cv_tutorial_2_key.py  env  mfly.png
```

We're ready to open VS Code. We can open it directly from our terminal, which will automatically open VS Code in WSL in our current directory.

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ code .
```

You can open a terminal directly in VS Code. To open a terminal, use the shortcut `` ctrl + ` `` or access it from the top menu by going to `View > Terminal`. **If you do open a new terminal, make sure your virtual environment is activated.**

### *:Zone.Identifier files

Lastly, you might be seeing some *:Zone.Identifier files. These files are auto generated by the Windows system and only show up when you move files into the WSL subsystem. We can remove these files by running the command below:

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ find . -name "*:Zone.Identifier" -type f -delete
```

Some users don't see these files, I'm not entirely sure why. Either way, we don't need them.


## Auton Computer Vision Tutorial 1: Image Filters

That was a lot of setup, but we're finally ready to start programming! This project will introduce you to OpenCV, which is a popular computer vision library. You will use some of its functions to apply basic image processing such as blurring, sharpening, and grayscaling.

First, let's preview what you'll be writing. We can run our Python script in our terminal as shown below.

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ python3 cv_tutorial_1_key.py
```

This will open an OpenCV window, where we see our original `mfly.png` photo on the left, and a filtered version on the right. Below the photos are 3 sliders that let you control the blurring, sharpening, and grayscaling. Play around with the sliders to see how this changes our filtered photo on the right.

To close the OpenCV window and terminate the program, focus it then press `q`. 

> [!TIP]
> In general, you can terminate any program in the terminal by using `ctrl + c`.

Now that we know what the final product looks like, let's try to program this ourselves. Start by opening up `cv_tutorial_1.py` in your editor.

To use OpenCV's functions, we need to import its module. In Python, we do this with `import` statements. If you have already learned C++, this is similar to using `#include`. Any lines prefixed with `#` are comments, which are not executed. You may include them for your own reference, but they are optional. Note that these comments are also available in `cv_tutorial_1_key.py`.

```python
# Import OpenCV and numpy modules
import cv2
import numpy as np
```

Next, let's define some variables that we'll use later on. `MAX_VALUE` establishes the maximum value for each image effect. `blur`, `sharpen`, and `grayscale` will be updated using the sliders, which controls the strength of each effect. Lastly, we establish several name variables that we'll use to distinguish between our sliders.

```python
# Define variables
MAX_VALUE = 20

blur = 0
sharpen = 0
grayscale = 0

blur_name = "blur"
sharpen_name = "Sharpen"
grayscale_name = "Grayscale"

window_name = "Auton CV Tutorial 1: Image Filters"
```

Let's write a function called `on_trackbar_update`. This function will be called everytime we move one of the sliders, and will update our `blur`, `sharpen`, and `grayscale` variables we just created.

```python
def on_trackbar_update(_):
    global blur, sharpen, grayscale
    blur = cv2.getTrackbarPos(blur_name, window_name)
    sharpen = cv2.getTrackbarPos(sharpen_name, window_name)
    grayscale = cv2.getTrackbarPos(grayscale_name, window_name)
```

We'll also write a function called `standard_scale`. Don't worry too much about this function, this will just scale any image we use so that it's a reasonable size.

```python
# Limits image size
def standard_scale(img):
    max_H, max_W = 720 // 2, 1280 // 2
    H, W, _ = img.shape
    if H > max_H and H * 16 / 9 >= W:
        img = cv2.resize(img, (int(max_H * W / H), max_H))
    elif W > max_W and W * 9 / 16 >= H:
        img = cv2.resize(img, (max_W, int(max_W * H / W)))
    return img
```

Next, let's create our OpenCV window. This will create the actual window that you saw when you ran `cv_tutorial_1_key.py`, including the sliders you used to apply our effects to the image.  
> More on windows and trackbars: https://docs.opencv.org/4.x/da/d6a/tutorial_trackbar.html.

```python
# Create window and trackbars
cv2.namedWindow(window_name)
cv2.createTrackbar(blur_name, window_name, blur, MAX_VALUE, on_trackbar_update)
cv2.createTrackbar(sharpen_name, window_name, sharpen, MAX_VALUE, on_trackbar_update)
cv2.createTrackbar(grayscale_name, window_name, grayscale, MAX_VALUE, on_trackbar_update)
```

Let's read our `mfly.png` image using `cv2.imread`. This will open our image and store it as a NxMx3 BGR color space matrix in `img`. We'll also use our `standard_scale` function from earlier to resize our image if necessary.  
> Color spaces: https://en.wikipedia.org/wiki/Color_space.  
> OpenCV color spaces: https://www.geeksforgeeks.org/color-spaces-in-opencv-python/.

```python
# Read image
filename = "mfly.png"
img = cv2.imread(filename)
img = standard_scale(img)
```

Now we'll move on to our main `while` loop. This loop will run forever until the user terminates the program, allowing us to play around with the different image effects.

We'll start with the blur filter. There are several methods of blurring an image. We'll utilize the commonly used Gaussian filter with OpenCV's `cv2.GaussianBlur` function. The main focus here is the second parameter of the function, which is an `(N, N)` tuple. The larger the tuple, the stronger our blur strength.  
> Different methods of blurring images: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html.

```python
# Runs until the user quits
while True:
    """
    BLUR
    """
    img_copy = img
    kernel = blur * 2 + 1
    
    # Blur the image
    img_modified = cv2.GaussianBlur(img_copy, (kernel, kernel), 0)
```

Next, we'll work on image sharpening. A simple way of doing so is by creating a 3x3 sharpening kernel, then using OpenCV's `cv2.filter2D` to apply this kernel throughout the image. Note that we are still in the `while` loop.
> More on this method: https://www.opencvhelp.org/tutorials/image-processing/how-to-sharpen-image/.

```python
while True:
    """
    BLUR
    """
    # ...

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
```

Last but not least, we'll implement the grayscaling effect. OpenCV's `cv2.cvtColor` allows you to convert between different color spaces. In this case, we are converting from the `BGR` color space to the `GRAY` color space, which returns a grayscaled image. Then, we'll use `cv2.addWeighted` to blend this grayscaled image with our colored image based on our `grayscale` slider value.

```python
while True:
    """
    BLUR
    ...
    """

    """
    SHARPEN
    ...
    """

    """
    GRAYSCALE
    """
    # Grayscale
    gray = cv2.cvtColor(img_modified, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    # Blend gray with original
    blend = grayscale / MAX_VALUE
    img_modified = cv2.addWeighted(gray, blend, img_modified, 1 - blend, 0)
```

Finally, all that's left is to show our images in the OpenCV window we created earlier, so that we can visualize what is happening. We'll use `np.hstack` to stack our original and filtered images side by side, then `cv2.imshow` to show our image in the window. `cv2.waitKey` allows us to check for user input. In this case, we will break out of our `while` loop if the user presses `q`, and save our filtered image to `final_image.jpg` if the user presses `s`. Lastly, `cv2.destroyAllWindows` ensures that our window is closed.
> More on `cv2.imshow`: https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/.

```python
while True:
    """
    BLUR
    ...
    """

    """
    SHARPEN
    ...
    """

    """
    GRAYSCALE
    ...
    """

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
```

We're ready to run our script! We can run it just like we ran `cv_tutorial_1_key.py`. We should see the exact same window appear.

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ python3 cv_tutorial_1.py
```

Congratulations, you completed *Auton Computer Vision Tutorial 1: Image Filters*!


## Auton Computer Vision Tutorial 2: Image Thresholding

This project will introduce you to image thresholding. This is a very common task in computer vision, and it involves the process filtering out only certain parts of an image. For example, we might use image thresholding to filter out only the yellow parts of our plane in `mfly.png`.

As before, let's preview what you'll be writing first.

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ python3 cv_tutorial_2_key.py
```

This will open an OpenCV window similar to the first project, where we see our original `mfly.png` photo on the left, and a thresholded image on the right. Below the photos are 6 sliders that let you control which parts of your image you want to threshold using the HSV (Hue, Saturation, Value) color space. The areas in black are the parts of the image you are filtering out, while the areas in white are the parts you are keeping. Play around with the sliders to see if you can filter out only the yellow parts of the plane.
> Visualization of the HSV color space: https://web.cs.uni-paderborn.de/cgvb/colormaster/web/color-systems/hsv.html.

Let's try to program this ourselves. Start by opening up `cv_tutorial_2.py` in your editor. We'll be using the same modules that we used in the first project, so our `import` statements will be the same.

```python
# Import OpenCV and numpy modules
import cv2
import numpy as np
```

Next, let's declare some variables. In the HSV color space, saturation and value range from [0, 255], so we'll use `MAX_VALUE` as the upper bounds. However, hue ranges from [0, 360], so we'll create a separate `MAX_VALUE_H` variable to constrain it (OpenCV's hue only ranges from [0, 179], which is why we divide by 2).

The `*_low` and `*_high` variables will be controlled by our sliders. We'll use these to threshold our image, so that we only keep colors that are within (H_low, S_low, V_low) and (H_high, S_high, V_high). For example, if we wanted to detect the yellow sections of our plane, we might only choose colors with a hue value within [10, 20].

Lastly, we have some `*_name` variables similar to project 1 that correspond to our OpenCV window and the sliders.

```python
# Constants
MAX_VALUE = 255
MAX_VALUE_H = 360 // 2 - 1
MAX_VALUE_BLUR = 20

# Declare H, S, V starting values
# H: (0, 179)  S: (0, 255)  V: (0, 255)
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
```

Now we'll define our update functions, which update our HSV variables whenever we move the sliders.

```python
# Functions to read trackbar values on update
def on_H_update(_):
    global H_low, H_high
    
    H_low = cv2.getTrackbarPos(H_low_name, window_name)
    H_low = min(H_low, H_high - 1)
    cv2.setTrackbarPos(H_low_name, window_name, H_low)
    
    H_high = cv2.getTrackbarPos(H_high_name, window_name)
    H_high = max(H_high, H_low + 1)
    cv2.setTrackbarPos(H_high_name, window_name, H_high)


def on_S_update(_):
    global S_low, S_high
    
    S_low = cv2.getTrackbarPos(S_low_name, window_name)
    S_low = min(S_low, S_high - 1)
    cv2.setTrackbarPos(S_low_name, window_name, S_low)
    
    S_high = cv2.getTrackbarPos(S_high_name, window_name)
    S_high = max(S_high, S_low + 1)
    cv2.setTrackbarPos(S_high_name, window_name, S_high)


def on_V_update(_):
    global V_low, V_high
    
    V_low = cv2.getTrackbarPos(V_low_name, window_name)
    V_low = min(V_low, V_high - 1)
    cv2.setTrackbarPos(V_low_name, window_name, V_low)
    
    V_high = cv2.getTrackbarPos(V_high_name, window_name)
    V_high = max(V_high, V_low + 1)
    cv2.setTrackbarPos(V_high_name, window_name, V_high)


def on_blur_update(val):
    global blur_strength
    blur_strength = val
```

We'll also keep the same `standard_scale` function from project 1, as well as create our OpenCV window and the sliders.

```python
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
cv2.createTrackbar(H_low_name, window_name, H_low, MAX_VALUE_H, on_H_update)
cv2.createTrackbar(H_high_name, window_name, H_high, MAX_VALUE_H, on_H_update)
cv2.createTrackbar(S_low_name, window_name, S_low, MAX_VALUE, on_S_update)
cv2.createTrackbar(S_high_name, window_name, S_high, MAX_VALUE, on_S_update)
cv2.createTrackbar(V_low_name, window_name, V_low, MAX_VALUE, on_V_update)
cv2.createTrackbar(V_high_name, window_name, V_high, MAX_VALUE, on_V_update)
cv2.createTrackbar(blur_name, window_name, blur_strength, MAX_VALUE_BLUR, on_blur_update)
```

Now we're ready to read our image. Note that this time we use `cv2.cvtColor` to convert our image from BGR (default) to HSV.

```python
# Read image
filename = "mfly.png"
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = standard_scale(img)
```

Time to write our `while` loop, starting with image blurring. A common obstacle we face when thresholding images is noise. Image noise is often grainy and consists of random variations in brightness or color within an image. There are many factors that can contribute to image noise such as camera quality and film grain. As you can imagine, color variation during a process where we rely on color can make it difficult for us to accurately threshold. One method of reducing noise is by blurring our image. By blurring our image, we sacrifice detail for color consistency. Often times this loss in detail is acceptable, especially if we are mainly trying to isolate a target from the background, like the SUAS ODLCs.

We will control the strength of the blur in the same way as in project 1, using OpenCV's `cv2.GaussianBlur` to apply a Gaussian kernel throughout the image.

```python
# Runs until the user quits
while True:
    img_copy = img
    kernel = blur_strength * 2 + 1
    
    # Blur the image
    img_blur = cv2.GaussianBlur(img_copy, (kernel, kernel), 0)
```

After blurring, we're ready to apply our image threshold. We can use OpenCV's `cv2.inRange` function and our `*_low` and `*_high` values to create an image mask that filters out colors in this range.
> More on `cv2.inRange`: https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html.

 ```python
 while True:
    # code...

    # Threshold images based on H, S, V
    img_threshold = cv2.inRange(img_blur, (H_low, S_low, V_low), (H_high, S_high, V_high))
 ```
 
 Lastly, we'll display our images in our OpenCV window, so we can see how the image changes live as we move the HSV sliders. We'll use `np.hstack` again to put our original image on the left and our threshold mask on the right.

 ```python
 while True:
    # code...

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
 ```

We're ready to test our code using the terminal!

```console
(env) marcusvc:~/mfly_cv/cv-starter-projects$ python3 cv_tutorial_2.py
```

Congratulations, you completed *Auton Computer Vision Tutorial 2: Image Filters*!


## Conclusion

Congratulations, this concludes your introduction to computer vision!

We are always looking to make improvements to our material! This tutorial is very new, so any feedback you have is greatly appreciated. Please don't hesitate to message me on slack or via email (marcusvc@umich.edu). 
