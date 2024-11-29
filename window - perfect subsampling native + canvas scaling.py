import tkinter

def resize_canvas(event):
    # Update the canvas size to match the window
    canvas.config(width=event.width, height=event.height)

    # Calculate the scaling factor based on canvas size
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    image_width = canvas_background.width()
    image_height = canvas_background.height()

    # Maintain aspect ratio
    scale = min(canvas_width / image_width, canvas_height / image_height)

    # Resize the image proportionally
    resized_width = max(1, int(image_width * scale))
    resized_height = max(1, int(image_height * scale))

    resized_image = canvas_background.subsample(
        max(1, image_width // resized_width),
        max(1, image_height // resized_height)
    )

    # Update the canvas background
    canvas.itemconfig(background_image, image=resized_image)
    canvas.image = resized_image  # Save a reference to prevent garbage collection

    # Center the image on the canvas
    canvas.coords(background_image, canvas_width / 2, canvas_height / 2)

# Initialize the main window
window = tkinter.Tk()
window.title("Window Canvas")

# Create a canvas
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load the background image
canvas_background = tkinter.PhotoImage(file="background.png")
background_image = canvas.create_image(0, 0, anchor="center", image=canvas_background)

# Bind the window resize event to dynamically resize the canvas and image
window.bind("<Configure>", resize_canvas)

# Enable fullscreen toggle
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
