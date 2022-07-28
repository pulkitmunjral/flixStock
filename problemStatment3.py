"""
Problem Statement 3 : Create Required Image
● Given the image input.jpg and mask.png create the image result.jpg.
● Link to images:
https://drive.google.com/drive/folders/1DB60KVzGCFe1d1_V2aAIRMSwNOS9939i?usp=sharing
"""

# importing the required library opencv by cv2 and numpy as np
import cv2
import numpy as np


def problem_statment_3():

    # reading the input and masked images
    input_image = cv2.imread('input.jpg')
    mask_image = cv2.imread('mask.jpg')

    # getting the height and width of the input image
    height, width, _ = input_image.shape

    # creating the red colour background image
    red_image = np.zeros((height, width, 3), np.uint8)
    red_image[:] = (0, 0, 255)

    # converting all images to data type float
    input_image = input_image.astype(float)
    red_image = red_image.astype(float)
    mask_image = mask_image.astype(float)

    # dividing max with max colour value(255) to convert it to binary array with 0,1 values only
    positive_mask_image = mask_image/255
    negative_mask_image = 1.0 - mask_image/255

    # multiplying the input image to binary positive mask filter
    # which will multiply input image with 1 at part of pants filter and 0 at all other portion
    forground_image = cv2.multiply(positive_mask_image, input_image)

    # multiplying the red image to binary negative mask filter
    # which will multiply red image with 0 at part of pants filter and 1 at all other portion
    background_image = cv2.multiply(negative_mask_image, red_image)

    # adding both the foreground and background images
    output_image = cv2.add(forground_image, background_image)

    # saving the output file to the directory
    cv2.imwrite("output_from_code.jpg", output_image)

    # showing the same output image
    cv2.imshow("output_from_code", output_image/255)
    cv2.waitKey(10000)


problem_statment_3()



