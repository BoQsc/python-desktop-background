from tkinter import Tk, Canvas, PhotoImage

def resize_background(event):
    # Calculate new dimensions
    new_width = event.width
    new_height = event.height

    # Resize the image using subsample
    resized_image = original_image.subsample(max(1, original_width // new_width), max(1, original_height // new_height))

    # Update the canvas image and position
    canvas.itemconfig(image_id, image=resized_image)
    canvas.image = resized_image  # Prevent garbage collection

    # Set the position to bottom-right
    canvas.coords(image_id, new_width, new_height)

# Create window
root = Tk()
root.geometry("400x400")

# Create canvas
canvas = Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# Load background image
original_image = PhotoImage(file="background.png")
original_width = original_image.width()
original_height = original_image.height()

# Add the image to canvas (bottom-right corner initially)
image_id = canvas.create_image(400, 400, image=original_image, anchor="se")

# Bind window resizing event
root.bind("<Configure>", resize_background)

root.mainloop()
