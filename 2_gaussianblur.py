import cv2
from PIL import Image

# Load the input image
input_image = cv2.imread('img/cropped_image.jpg')

# Define the kernel size (specifies the size of the Gaussian kernel)
kernel_size = (5, 5)  # You can adjust the kernel size as needed

# Apply Gaussian blur to the input image
blurred_image = cv2.GaussianBlur(input_image, kernel_size, sigmaX=0)

# Convert the blurred image from OpenCV format to Pillow format
pil_image = Image.fromarray(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))

# Save the blurred image using Pillow
pil_image.save('img/blurred_image.jpg', format='JPEG')

# Display the original and blurred images
cv2.imshow('Blurred Image', blurred_image)

# Wait for a key press and then close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
