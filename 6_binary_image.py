import cv2

# Load the grayscale image (replace 'input_image.jpg' with your image file)
gray_image = cv2.imread('img/grey_scale_image.jpg', cv2.IMREAD_GRAYSCALE)

# Set a threshold value (adjust this value as needed)
threshold_value = 128

# Apply binary thresholding
ret, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the binary image (optional)
cv2.imwrite('img/binary_image.jpg', binary_image)
