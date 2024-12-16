import tkinter
from PIL import Image, ImageTk
from ctypes import windll

# Enable DPI awareness
windll.shcore.SetProcessDpiAwareness(1)

# Initialize the main window
window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# DPI scaling factor
dpi_scaling = window.tk.call('tk', 'scaling')
print(f"Initial DPI Scaling: {dpi_scaling}")

# Load background image
background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

# Load taskbar image
taskbar_image = Image.open("taskbar.png")
taskbar_photo = None  # Placeholder for resized taskbar image
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

# Resize taskbar and notification area
def resize_taskbar(event):
    global taskbar_photo

    # Base width percentage adjusted dynamically based on DPI scaling
    base_taskbar_area_width_percentage = 0.84 if dpi_scaling < 1.334 else 0.81  # 84% for desktop, 81% for laptop

    current_dpi_scaling = window.tk.call('tk', 'scaling')
    print(f"Current DPI Scaling: {current_dpi_scaling}")

    taskbar_area_width = int(event.width * base_taskbar_area_width_percentage)
    taskbar_area_width_scaled = int(taskbar_area_width / current_dpi_scaling)
    notification_area_width = event.width - taskbar_area_width_scaled
    notification_area_width = max(notification_area_width, 0)

    # Update taskbar rectangles
    canvas.coords(taskbar_area, 0, event.height - taskbar_height, taskbar_area_width_scaled, event.height)
    canvas.coords(taskbar_notification_area, taskbar_area_width_scaled, event.height - taskbar_height, event.width, event.height)

    # Resize taskbar image
    resized_taskbar_image = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.NEAREST)
    taskbar_photo = ImageTk.PhotoImage(resized_taskbar_image)
    taskbar_widget = canvas.create_image(0, event.height - taskbar_height, anchor="nw", image=taskbar_photo)
    canvas.tag_lower(taskbar_widget)  # Ensure the image is below other widgets

    print(f"Taskbar Area Width: {taskbar_area_width_scaled}, Notification Area Width: {notification_area_width}")

# Event callback storage
on_window_event_callbacks = [resize_background_image, resize_taskbar]

# Handle window events
def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)

# Bind events
window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

# Start the application
window.mainloop()
