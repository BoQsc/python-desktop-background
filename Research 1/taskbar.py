import tkinter

# Create the main window
window = tkinter.Tk()

# Load the taskbar image
taskbar_image = tkinter.PhotoImage(file="taskbar_transparent.png")

# Create a Canvas to place the taskbar image
canvas = tkinter.Canvas(window, highlightthickness=0)
canvas.grid(row=0, column=0, sticky="nsew")

# Stretch the canvas to fill the entire window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Function to update the image to match the window width
def update_image(event):
    canvas.delete("all")  # Clear the canvas
    # Create the image with the new width, keeping the height proportionate
    image_width = event.width
    image_height = int(taskbar_image.height() * image_width / taskbar_image.width())
    canvas.create_image(0, 0, anchor="nw", image=taskbar_image)
    canvas.config(width=image_width, height=image_height)

# Bind the <Configure> event to update the image when the window is resized
window.bind("<Configure>", update_image)

# Run the application
window.mainloop()
