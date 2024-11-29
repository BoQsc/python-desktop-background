from tkinter import Tk, Canvas, PhotoImage, NW
from PIL import Image, ImageTk

def resize_image(event):
    # Calculate scale factors
    width_scale = event.width / original_width
    height_scale = event.height / original_height

    # Choose the larger scale to ensure full window coverage
    scale = max(width_scale, height_scale)

    # Calculate the new image size
    new_img_width = int(original_width * scale)
    new_img_height = int(original_height * scale)

    # Resize image maintaining aspect ratio
    resized_pil_image = pil_image.resize((new_img_width, new_img_height), Image.LANCZOS)
    
    # Convert to PhotoImage
    resized_image = ImageTk.PhotoImage(resized_pil_image)

    # Update the canvas image
    canvas.itemconfig(image_id, image=resized_image)
    canvas.image = resized_image  # Keep a reference to avoid garbage collection

    # Center the image in the canvas
    x = (event.width - new_img_width) // 2
    y = (event.height - new_img_height) // 2
    canvas.coords(image_id, x, y)

# Create window
root = Tk()
root.geometry("400x400")

# Create canvas
canvas = Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# Load original image using PIL
pil_image = Image.open("background.png")
original_width = pil_image.width
original_height = pil_image.height

# Add image to canvas
original_image = ImageTk.PhotoImage(pil_image)
image_id = canvas.create_image(0, 0, image=original_image, anchor=NW)

# Bind window resizing event
root.bind("<Configure>", resize_image)

root.mainloop()