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

def on_resize(event):
    global canvas_width, canvas_height

    # Update canvas dimensions
    canvas_width = event.width
    canvas_height = event.height

    # Calculate zoom and subsample factors for new canvas size
    zoom_factor = int(max(1, scale_factor))
    subsample_factor = int(max(1, max_scale / scale_factor))

    # Apply zoom and subsample to create the scaled image
    scaled_image = image.zoom(zoom_factor).subsample(subsample_factor)

    # Update canvas with the scaled image
    canvas.itemconfig(image_id, image=scaled_image)
    canvas.image = scaled_image  # Prevent garbage collection

# Create the main Tkinter window
root = tk.Tk()
root.title("Smooth Scaling with Mouse Wheel and Resizing")

# Load the image
image = tk.PhotoImage(file="background.png")  # Replace with your image file

# Initialize scale variables
scale_factor = 1
max_scale = 5
min_scale = 1
canvas_width = 800
canvas_height = 600

# Create a canvas to display the image
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(fill=tk.BOTH, expand=True)

# Display the initial image
image_id = canvas.create_image(canvas_width // 2, canvas_height // 2, image=image)

# Bind the mouse wheel event and canvas resizing
root.bind("<MouseWheel>", on_mouse_wheel)
canvas.bind("<Configure>", on_resize)

root.mainloop()