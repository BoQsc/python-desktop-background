import tkinter
from PIL import Image, ImageTk
from ctypes import windll

# Enable DPI awareness for sharp rendering
windll.shcore.SetProcessDpiAwareness(1)

# Initialize the main window
window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# DPI scaling factor
dpi_scaling = window.tk.call('tk', 'scaling')
canvas.scale("all", 0, 0, dpi_scaling, dpi_scaling)

# Event callback storage
on_window_event_callbacks = []

# Load background image
background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

# Load taskbar image
taskbar_image = Image.open("taskbar.png")
taskbar_photo = ImageTk.PhotoImage(image=taskbar_image)  # Placeholder for the resized taskbar photo
taskbar_height = int(32 * dpi_scaling)  # Taskbar height based on DPI scaling

# Taskbar rectangles
taskbar_area = canvas.create_rectangle(0, 0, 0, 0, fill="blue", outline="")
taskbar_notification_area = canvas.create_rectangle(0, 0, 0, 0, fill="gray", outline="")

# Resize background image
def resize_background_image(event, _last=[None, None]):
    if (event.width, event.height) != tuple(_last):
        _last[:] = [event.width, event.height]
        resized_image = background_image.resize((event.width, event.height), Image.Resampling.NEAREST)
        canvas.resized_photo = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

on_window_event_callbacks.append(resize_background_image)

# Resize taskbar areas and image
def resize_taskbar(event):
    global taskbar_photo

    # Calculate dimensions
    taskbar_area_width = int(event.width * 0.77 + dpi_scaling)    # 77% width for the main area
    notification_area_width = event.width - taskbar_area_width

    # Update taskbar rectangles
    canvas.coords(taskbar_area, 0, event.height - taskbar_height, taskbar_area_width, event.height)
    canvas.coords(taskbar_notification_area, taskbar_area_width, event.height - taskbar_height, event.width, event.height)

    # Resize and update taskbar image
    resized_taskbar_image = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.NEAREST)
    taskbar_photo = ImageTk.PhotoImage(resized_taskbar_image)
    taskbar_widget = canvas.create_image(0, event.height - taskbar_height, anchor="nw", image=taskbar_photo)
    canvas.tag_lower(taskbar_widget)  # Ensure the image is below other widgets
    #canvas.tag_raise(taskbar_widget)  # Ensure the image is above other widgets

on_window_event_callbacks.append(resize_taskbar)

# Handle window events
def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)

# Bind events
window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

# Start the application
window.mainloop()
