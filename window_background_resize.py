import tkinter as tk

# Function to resize the background image to fit the window
def resize_background(event):
    # Get the current window dimensions
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    
    # Calculate the scaling factors
    scale_x = original_width / new_width
    scale_y = original_height / new_height
    
    # Determine the subsampling factor based on the larger of the two scaling factors
    subsample_factor = max(int(scale_x), int(scale_y))
    
    # Subsample the image to fit the new window size
    if subsample_factor > 1:
        scaled_image = background_image.subsample(subsample_factor, subsample_factor)
    else:
        scaled_image = background_image
    
    # Update the canvas image
    canvas.itemconfig(image_on_canvas, image=scaled_image)
    canvas.image = scaled_image  # Keep a reference to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("Resizable Background Image")

# Load the background image
background_image = tk.PhotoImage(file="background.png")

# Get the original dimensions of the image
original_width = background_image.width()
original_height = background_image.height()

# Create a canvas to hold the background image
canvas = tk.Canvas(root, width=original_width, height=original_height)
canvas.pack(fill=tk.BOTH, expand=True)

# Add the background image to the canvas
image_on_canvas = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Bind the resize function to the window resize event
root.bind("<Configure>", resize_background)

# Start the Tkinter event loop
root.mainloop()