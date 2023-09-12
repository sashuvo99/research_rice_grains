import cv2
import numpy as np

# Load the input image
input_image = cv2.imread('img/enhanced_image.jpg')

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

# Define the color ranges for yellow, brown, red, and white in HSV format
# Adjust the lower and upper bounds for each color as needed
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

lower_brown = np.array([10, 100, 100])
upper_brown = np.array([20, 255, 255])

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])

# Define the range for white
lower_white = np.array([0, 0, 200])  # Adjust the value threshold as needed
upper_white = np.array([180, 30, 255])  # Adjust the value threshold as needed

# Create masks for each color range
mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)
mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# Create a mask for white
mask_white = cv2.inRange(hsv_image, lower_white, upper_white)

# Combine the masks for red regions
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

# Combine all the masks to detect yellow, brown, red, and white regions
final_mask = cv2.bitwise_or(mask_yellow, cv2.bitwise_or(mask_brown, cv2.bitwise_or(mask_red, mask_white)))

# Find contours in the final mask
contours, _ = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a text file to save the detected color information
with open('result/detected_colors.txt', 'w') as file:
    # Iterate through the detected contours
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)
        
        # Filter out small contours (adjust the area threshold as needed)
        if area > 100:
            # Determine the center of the contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
            else:
                cx, cy = 0, 0

            # Determine the color of the detected region
            color = input_image[cy, cx]

            # Determine the name of the color using a color mapping
            color_name = None
            if color is not None:
                # Define a dictionary mapping BGR values to color names
                color_mapping = {
                    (0, 0, 255): "Red",
                    (0, 128, 128): "Yellow",
                    (42, 42, 165): "Brown",
                    (255, 255, 255): "White"  # Add white color mapping
                    # Add more color mappings as needed
                }

                # Find the closest matching color from the dictionary
                min_distance = float('inf')
                for key, value in color_mapping.items():
                    distance = np.linalg.norm(np.array(key) - np.array(color))
                    if distance < min_distance:
                        min_distance = distance
                        color_name = value

            # Print the color name and draw a bounding box around the detected region
            if color_name:
                detection_info = f"Detected {color_name} at ({cx}, {cy})"
                print(detection_info)
                cv2.drawContours(input_image, [contour], -1, (0, 255, 0), 2)  # Draw a green bounding box

                # Write color information to the text file
                file.write(detection_info + '\n')

# Display the input image with detected regions
cv2.imshow('Color Detection', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
