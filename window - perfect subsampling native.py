import tkinter

def resize_image(event):
    # Calculate subsampling factors based on canvas size
    width_factor = max(1, canvas_background.width() // event.width)
    height_factor = max(1, canvas_background.height() // event.height)

    # Rescale the image with the calculated subsampling factors
    resized_image = canvas_background.subsample(width_factor, height_factor)
    canvas.itemconfig(background_image, image=resized_image)
    canvas.image = resized_image  # Maintain a reference to prevent garbage collection

window = tkinter.Tk()
window.title("Window Canvas")

canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load the initial background image
canvas_background = tkinter.PhotoImage(file="background.png")
background_image = canvas.create_image(0, 0, anchor="nw", image=canvas_background)

# Bind the window resize event to the resize function
window.bind("<Configure>", resize_image)

# Toggle fullscreen mode with F11 key
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
