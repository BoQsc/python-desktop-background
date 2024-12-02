import tkinter as tk

def on_mouse_wheel(event):
    global scale_factor, direction

    if event.delta > 0:  # Zoom in
        direction = 1
    else:  # Zoom out
        direction = -1

    # Adjust scaling factor
    scale_factor += 0.2 * direction
    scale_factor = max(min_scale, min(max_scale, scale_factor))  # Clamp scale factor

    # Calculate zoom and subsample factors
    zoom_factor = int(max(1, scale_factor))
    subsample_factor = int(max(1, max_scale / scale_factor))

    # Apply zoom and subsample to create the scaled image
    scaled_image = image.zoom(zoom_factor).subsample(subsample_factor)

    # Update canvas with the scaled image
    canvas.itemconfig(image_id, image=scaled_image)
    canvas.image = scaled_image  # Prevent garbage collection

# Create the main Tkinter window
root = tk.Tk()
root.title("Smooth Scaling with Mouse Wheel")

# Load the image
image = tk.PhotoImage(file="background.png")  # Replace with your image file

# Initialize scale variables
scale_factor = 1
max_scale = 5
min_scale = 1

# Create a canvas to display the image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Display the initial image
image_id = canvas.create_image(400, 300, image=image)

# Bind the mouse wheel event
root.bind("<MouseWheel>", on_mouse_wheel)

root.mainloop()
