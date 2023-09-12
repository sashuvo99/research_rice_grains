import cv2
import numpy as np

# Load the input image
input_image = cv2.imread('img/cropped_image.jpg')

# Convert the image to the HSV color space for better color manipulation
hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

# Increase the saturation of the image (adjust the factor as needed)
saturation_factor = 1.5
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255)

# Convert the modified image back to BGR color space
enhanced_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Optionally, save the enhanced image
cv2.imwrite('img/enhanced_image.jpg', enhanced_image)
