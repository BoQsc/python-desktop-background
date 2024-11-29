from tkinter import Tk, Canvas, PhotoImage

def resize_image(event):
    new_width = event.width
    new_height = event.height

    # Calculate scale factors
    width_scale = new_width / original_width
    height_scale = new_height / original_height

    # Choose the smaller scale to maintain aspect ratio
    scale = min(width_scale, height_scale)

    # Calculate subsample factors
    if scale >= 1:
        subsample_width = 1
        subsample_height = 1
    else:
        subsample_width = int(1 / scale)
        subsample_height = int(1 / scale)

    # Resize the image
    resized_image = original_image.subsample(subsample_width, subsample_height)

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

# Add image to canvas
image_id = canvas.create_image(0, 0, image=original_image, anchor='nw')

# Bind window resizing event
root.bind("<Configure>", resize_image)

root.mainloop()