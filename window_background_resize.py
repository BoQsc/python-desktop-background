from tkinter import Tk, Canvas, PhotoImage

def resize_image(event):
    # Calculate new dimensions
    new_width = event.width
    new_height = event.height

    # Resize the image using subsample
    resized_image = original_image.subsample(original_width // new_width, original_height // new_height)

    # Update the canvas image
    canvas.itemconfig(image_id, image=resized_image)
    canvas.image = resized_image  # Keep a reference to avoid garbage collection

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
image_id = canvas.create_image(200, 200, image=original_image)

# Bind window resizing event
root.bind("<Configure>", resize_image)

root.mainloop()
