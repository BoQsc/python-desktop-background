import tkinter as tk
from PIL import Image, ImageTk

# Load an image (replace 'image.jpg' with your image file path)
image_path = "background.png"
image = Image.open(image_path)

# Setup root window
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Variables for animation
scale_factor = 1.0
scaling_direction = 1
subsample_value = 1

# Function to update the image
image_tk = None
def update_image():
    global scale_factor, scaling_direction, subsample_value, image_tk

    # Update scale factor and direction
    if scale_factor > 2.0:
        scaling_direction = -1
    elif scale_factor < 0.5:
        scaling_direction = 1
    
    scale_factor += 0.1 * scaling_direction
    
    # Subsample the image
    resized_image = image.resize((int(image.width * scale_factor),
                                  int(image.height * scale_factor)), Image.Resampling.LANCZOS)

    # Display image on canvas
    image_tk = ImageTk.PhotoImage(resized_image)
    canvas.delete("all")
    canvas.create_image(canvas.winfo_width() // 2, canvas.winfo_height() // 2, anchor="center", image=image_tk)

    # Schedule next frame
    root.after(1000, update_image)

# Start the animation
update_image()
root.mainloop()