import tkinter as tk
from tkinter import filedialog
import time

# Load the BMP image
def load_bmp(filename):
    with open(filename, 'rb') as f:
        # Read the BMP file header
        header = f.read(54)
        # Extract the image dimensions
        width = int.from_bytes(header[18:22], 'little')
        height = int.from_bytes(header[22:26], 'little')
        # Read the pixel data
        pixels = f.read()
        return width, height, pixels

# Resize the image using nearest neighbor algorithm
def resize_image(width, height, pixels, new_width, new_height):
    new_pixels = bytearray(new_width * new_height * 3)
    for y in range(new_height):
        for x in range(new_width):
            # Calculate the corresponding pixel in the original image
            orig_x = int(x * width / new_width)
            orig_y = int(y * height / new_height)
            # Calculate the index of the pixel in the original image
            orig_index = (orig_y * width * 3) + (orig_x * 3)
            # Copy the pixel data
            new_index = (y * new_width * 3) + (x * 3)
            if orig_index + 3 <= len(pixels):
                new_pixels[new_index:new_index+3] = pixels[orig_index:orig_index+3]
            else:
                new_pixels[new_index:new_index+3] = pixels[orig_index:]
    return new_pixels

# Create the Tkinter window
root = tk.Tk()
root.geometry("500x500")

# Load the BMP image
width, height, pixels = load_bmp("background.bmp")

# Create a PhotoImage object
photo = tk.PhotoImage(width=width, height=height)
for y in range(height):
    for x in range(width):
        # Calculate the index of the pixel
        index = (height - 1 - y) * width * 3 + x * 3
        if index + 3 <= len(pixels):
            # Get the RGB values
            b = pixels[index]
            g = pixels[index+1]
            r = pixels[index+2]
            # Set the pixel color
            photo.put(f"#{r:02x}{g:02x}{b:02x}", (x, y))
        else:
            # If the pixel data is not enough, use the last pixel's color
            if index < len(pixels):
                # Get the RGB values
                b = pixels[index]
                g = pixels[index]
                r = pixels[index]
                # Set the pixel color
                photo.put(f"#{r:02x}{g:02x}{b:02x}", (x, y))
            else:
                # If the pixel data is empty, use black color
                photo.put("#000000", (x, y))

# Create a Label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Resize the image to 400x400 pixels
def resize_to_400():
    global width, height, pixels, photo, label
    new_width = 400
    new_height = 400
    new_pixels = resize_image(width, height, pixels, new_width, new_height)
    # Create a new PhotoImage object
    new_photo = tk.PhotoImage(width=new_width, height=new_height)
    for y in range(new_height):
        for x in range(new_width):
            # Calculate the index of the pixel
            index = (y * new_width * 3) + (x * 3)
            if index + 3 <= len(new_pixels):
                # Get the RGB values
                b = new_pixels[index]
                g = new_pixels[index+1]
                r = new_pixels[index+2]
                # Set the pixel color
                new_photo.put(f"#{r:02x}{g:02x}{b:02x}", (x, new_height - y - 1))
            else:
                # If the pixel data is not enough, use the last pixel's color
                if index < len(new_pixels):
                    # Get the RGB values
                    b = new_pixels[index]
                    g = new_pixels[index]
                    r = new_pixels[index]
                    # Set the pixel color
                    new_photo.put(f"#{r:02x}{g:02x}{b:02x}", (x, new_height - y - 1))
                else:
                    # If the pixel data is empty, use black color
                    new_photo.put("#000000", (x, new_height - y - 1))
    # Update the Label
    label.config(image=new_photo)
    label.image = new_photo  # Keep a reference to prevent garbage collection
    # Schedule the next resize
    root.after(2000, resize_to_500)

# Resize the image to 500x500 pixels
def resize_to_500():
    global width, height, pixels, photo, label
    new_width = 500
    new_height = 500
    new_pixels = resize_image(width, height, pixels, new_width, new_height)
    # Create a new PhotoImage object
    new_photo = tk.PhotoImage(width=new_width, height=new_height)
    for y in range(new_height):
        for x in range(new_width):
            # Calculate the index of the pixel
            index = (y * new_width * 3) + (x * 3)
            if index + 3 <= len(new_pixels):
                # Get the RGB values
                b = new_pixels[index]
                g = new_pixels[index+1]
                r = new_pixels[index+2]
                # Set the pixel color
                new_photo.put(f"#{r:02x}{g:02x}{b:02x}", (x, new_height - y - 1))
            else:
                # If the pixel data is not enough, use the last pixel's color
                if index < len(new_pixels):
                    # Get the RGB values
                    b = new_pixels[index]
                    g = new_pixels[index]
                    r = new_pixels[index]
                    # Set the pixel color
                    new_photo.put(f"#{r:02x}{g:02x}{b:02x}", (x, new_height - y - 1))
                else:
                    # If the pixel data is empty, use black color
                    new_photo.put("#000000", (x, new_height - y - 1))
    # Update the Label
    label.config(image=new_photo)
    label.image = new_photo  # Keep a reference to prevent garbage collection

# Start the resizing process
resize_to_400()

root.mainloop()