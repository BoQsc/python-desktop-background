import tkinter
from PIL import Image, ImageTk

# Initialize the window
window = tkinter.Tk()
window.title("Window Canvas")

# Print statements for diagnostics
print("Python Desktop [Version 0.0.0]".replace("0.0.0", version:="0.0.1"))
print("Public Domain. No rights reserved.")
print("_______PIP Auto install Dependencies__________")
print("________TK Window Widget______________________")

# List to handle window event callbacks
on_window_event_callbacks = []

def on_window_event(event):
    canvas.config(width=event.width, height=event.height)
    for callback in on_window_event_callbacks:
        callback(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

# Create the canvas widget
print("________TK Loading canvas widget______________")
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load and display the background image
print("_______PIL Loading background PhotoImage______")
background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

def background_image_resize(event):
    resized_image = background_image.resize((event.width, event.height), Image.Resampling.NEAREST)
    canvas.resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

on_window_event_callbacks.append(background_image_resize)

# Taskbar image settings
print("________Canvas Taskbar__________")
taskbar_height = 40
print("________Canvas Taskbar Image__________")
taskbar_image = Image.open("taskbar.png")
taskbar_photo = ImageTk.PhotoImage(taskbar_image)
image_taskbar = canvas.create_image(0, 0, anchor="nw", image=taskbar_photo)

def taskbar_image_resize(event):
    resized_image = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.LANCZOS)
    canvas.tresized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(image_taskbar, image=canvas.tresized_photo)
    canvas.coords(image_taskbar, 0, event.height - taskbar_height)

on_window_event_callbacks.append(taskbar_image_resize)

# Function to create rectangles on the taskbar
def create_taskbar_rectangle(x, width, color="red"):
    rect = canvas.create_rectangle(x, canvas.winfo_height() - taskbar_height,
                                   x + width, canvas.winfo_height(), fill=color, outline="")
    return rect

# Create and manage rectangles on the taskbar
print("________Adding Rectangles to the Taskbar__________")
rectangles = []
rect_colors = ["red", "green", "blue", "yellow"]  # Example colors

# Add rectangles with varying positions and widths
for i, color in enumerate(rect_colors):
    rect = create_taskbar_rectangle(10 + i * 60, 50, color)  # Example spacing and width
    rectangles.append(rect)

# Update rectangle positions when the window resizes
def update_rectangles_position(event):
    for i, rect in enumerate(rectangles):
        canvas.coords(rect, 10 + i * 60, event.height - taskbar_height,
                      60 + i * 60, event.height)

on_window_event_callbacks.append(update_rectangles_position)

# Start the main event loop
window.mainloop()
