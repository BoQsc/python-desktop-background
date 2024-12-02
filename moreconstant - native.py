import tkinter

def resize_image(event):
    canvas_width = event.width
    canvas_height = event.height

    # Calculate subsampling factors
    width_factor = max(1, canvas_background.width() // canvas_width)
    height_factor = max(1, canvas_background.height() // canvas_height)

    # Apply subsample for major downscaling
    resized_image = canvas_background.subsample(width_factor, height_factor)

    # If further adjustments are needed for smoothness, apply zoom
    adjusted_width = canvas_background.width() // width_factor
    adjusted_height = canvas_background.height() // height_factor
    zoom_x = canvas_width / adjusted_width
    zoom_y = canvas_height / adjusted_height

    # Apply zoom only if minor adjustment is necessary
    if zoom_x > 1 or zoom_y > 1:
        zoom_factor_x = int(max(1, zoom_x))
        zoom_factor_y = int(max(1, zoom_y))
        resized_image = resized_image.zoom(zoom_factor_x, zoom_factor_y)

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
