from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

def resize_image_with_pillow(image_path, new_width, new_height):
    print(f"Resizing {image_path} to {new_width}x{new_height} using Pillow...")
    original_image = Image.open(image_path)
    resized_image = original_image.resize((new_width, new_height), Image.BILINEAR)
    return ImageTk.PhotoImage(resized_image)

# Example usage
root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

# Load and resize "background.png"
resized_image = resize_image_with_pillow("background.png", 600, 600)

# Display resized image
canvas.create_image(0, 0, anchor='nw', image=resized_image)
root.mainloop()
