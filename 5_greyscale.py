import cv2
import matplotlib.pyplot as plt

# Load the input image
input_image = cv2.imread('img/enhanced_image.jpg')

# Convert the input image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Display the input and grayscale images
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
plt.title('Input Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Optionally, save the enhanced image
cv2.imwrite('img/grey_scale_image.jpg', gray_image)

plt.show()
