import numpy as np
import cv2
import math

def distortion_kb4(params, x, y):
    # Unpack parameters
    fx, fy, cu, cv, k1, k2, k3, k4 = params
    
    # Calculate normalized coordinates
    nx = (x - cu) / fx
    ny = (y - cv) / fy
    
    # Calculate radial distortion factor
    r = (nx * nx + ny * ny)**0.5
    theta = math.atan(r)**0.5
    radial_distortion = theta*(1 + k1*theta**2 + k2*theta**4 + k3*theta**6 + k4*theta**8)
    
    if r == 0:
        xp = 0
        yp = 0
    else:   
        xp = radial_distortion/r*nx
        yp = radial_distortion/r*ny

    # Distort coordinates
    x_distorted = cu + fx * xp
    y_distorted = cv + fy * yp
    
    return x_distorted, y_distorted

def apply_distortion(distortion_model, params, image):
    # Initialize distorted_image with zeros of the same size as input_photo
    distorted_image = np.zeros_like(image)

    # Now you can assign values to distorted_image
    for y in range(img_height):
        for x in range(img_width):
            x_distorted, y_distorted = distortion_model(params, x, y)
            x_distorted = int(np.round(x_distorted))
            y_distorted = int(np.round(y_distorted))
            if 0 <= x_distorted < img_width and 0 <= y_distorted < img_height:
                distorted_image[y_distorted, x_distorted] = image[y, x]
    return distorted_image

# Load the input photo
input_photo = cv2.imread("figs/input_image.jpg")
# print(type(input_photo))
# cv2.imshow('...', input_photo)
params_kb4 = [622, 622, 965, 631, -0.256, -0.0015, 0.0007, -0.0002]

# Image resolution
img_width = 2201
img_height = 1467

# Apply distortion transformation
distorted_image_kb4 = apply_distortion(distortion_kb4, params_kb4, input_photo)

# Visualize the distorted images
cv2.imshow('Distorted Image (KB4)', distorted_image_kb4)
cv2.waitKey(0)
cv2.destroyAllWindows()
