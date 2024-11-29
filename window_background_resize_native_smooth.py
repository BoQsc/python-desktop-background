from tkinter import Tk, Canvas, PhotoImage, NW

def precompute_subsamples(image):
    """Precompute subsampled images for various scales."""
    scales = [1 / i for i in range(1, 11)]  # Generate scale factors (1x to 0.1x)
    subsampled_images = {}
    for scale in scales:
        subsample_factor = int(1 / scale)
        subsampled_images[scale] = image.subsample(subsample_factor, subsample_factor)
    return subsampled_images

def resize_image(event):
    new_width = event.width
    new_height = event.height

    # Calculate scale factors
    width_scale = new_width / original_width
    height_scale = new_height / original_height

    # Choose the smaller scale to maintain aspect ratio
    scale = min(width_scale, height_scale)

    # Find the closest available scale
    closest_scale = min(precomputed_images.keys(), key=lambda x: abs(x - scale))

    # Get the precomputed subsampled image
    resized_image = precomputed_images[closest_scale]

    # Update the canvas image
    canvas.itemconfig(image_id, image=resized_image)
    canvas.image = resized_image  # Keep a reference to avoid garbage collection

    # Position the image in the top-left corner
    canvas.coords(image_id, 0, 0)

# Create window
root = Tk()
root.geometry("400x400")

# Create canvas
canvas = Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# Load image
original_image = PhotoImage(file="background.png")
original_width = original_image.width()
original_height = original_image.height()

# Precompute subsampled images
precomputed_images = precompute_subsamples(original_image)

# Add image to canvas
image_id = canvas.create_image(0, 0, image=original_image, anchor=NW)

# Bind window resizing event
root.bind("<Configure>", resize_image)

root.mainloop()
