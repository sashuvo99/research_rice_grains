import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

# Load the input image
input_image_path = 'rice3.jpg'
input_image = mpimg.imread(input_image_path)

# Create a figure and axis for displaying the image
fig, ax = plt.subplots()

# Display the input image
ax.imshow(input_image)

# Define variables to store the cropping region
cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0

# Function to handle mouse button press events
def on_press(event):
    global x_start, y_start, x_end, y_end, cropping

    # Capture the starting coordinates when the left mouse button is pressed
    if event.button == 1:
        x_start, y_start = event.xdata, event.ydata
        x_end, y_end = event.xdata, event.ydata
        cropping = True

# Function to handle mouse motion events
def on_motion(event):
    global x_end, y_end

    # Update the ending coordinates as the mouse is moved
    if cropping:
        x_end, y_end = event.xdata, event.ydata

# Function to handle mouse button release events
def on_release(event):
    global x_start, y_start, x_end, y_end, cropping

    # Capture the ending coordinates when the left mouse button is released
    if event.button == 1:
        x_end, y_end = event.xdata, event.ydata
        cropping = False

        # Create a rectangle patch to visually represent the cropping region
        rect = patches.Rectangle(
            (x_start, y_start), x_end - x_start, y_end - y_start,
            linewidth=1, edgecolor='r', facecolor='none')

        # Add the rectangle to the plot
        ax.add_patch(rect)
        plt.draw()

# Connect the mouse event handlers
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

# Show the image and allow the user to interactively crop it
plt.show()

# Crop the selected region from the original image
x_start, x_end = int(x_start), int(x_end)
y_start, y_end = int(y_start), int(y_end)
cropped_image = input_image[y_start:y_end, x_start:x_end]

# Save the cropped image
output_image_path = 'img/cropped_image.jpg'
mpimg.imsave(output_image_path, cropped_image)

# Close the figure
plt.close(fig)

print(f'Cropped image saved as {output_image_path}')
