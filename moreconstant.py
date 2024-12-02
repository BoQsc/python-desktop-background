import tkinter
from PIL import Image, ImageTk

def resize_image(event):
    # Get the size of the canvas
    canvas_width, canvas_height = event.width, event.height

    # Resize the original image to fit the canvas
    resized_image = original_image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
    canvas_resized_image = ImageTk.PhotoImage(resized_image)

    # Update the canvas with the resized image
    canvas.itemconfig(background_image, image=canvas_resized_image)
    canvas.image = canvas_resized_image  # Keep a reference to prevent garbage collection

window = tkinter.Tk()
window.title("Window Canvas")

canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load the initial background image with Pillow
original_image = Image.open("background.png")
background_image = ImageTk.PhotoImage(original_image)

# Add the image to the canvas
background_image = canvas.create_image(0, 0, anchor="nw", image=background_image)

# Bind the window resize event to the resize function
window.bind("<Configure>", resize_image)

# Toggle fullscreen mode with F11 key
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
