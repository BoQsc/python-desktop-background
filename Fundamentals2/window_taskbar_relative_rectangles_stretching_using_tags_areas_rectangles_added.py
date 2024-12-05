print(program := "Python Desktop [Version 0.0.0]".replace("0.0.0", version := "0.0.1"))
print(credits := "Public Domain. No rights reserved.")
print("_______PIP Auto install Dependencies__________")
print("________TK Window Widget______________________")
__import__('os').system('title ' + program + "(Console)")

import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title(program)

print("________TK Window Events______________________")
on_window_event_callbacks = []

def on_window_event(event):
    canvas.config(width=event.width, height=event.height)
    for callback in on_window_event_callbacks:
        callback(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

print("________TK Loading canvas widget______________")
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

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

print("________Canvas Taskbar__________")
taskbar_height = 40

print("________Canvas Taskbar Image__________")
taskbar_image = Image.new("RGBA", (1, taskbar_height), (0, 0, 255, 128))
taskbar_photo = ImageTk.PhotoImage(taskbar_image)
image_taskbar = canvas.create_image(0, 0, anchor="nw", image=taskbar_photo)

def taskbar_image_resize(event):
    resized_image = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.LANCZOS)
    canvas.tresized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(image_taskbar, image=canvas.tresized_photo)
    canvas.coords(image_taskbar, 0, event.height - taskbar_height)

on_window_event_callbacks.append(taskbar_image_resize)

print("________Canvas Taskbar Image Rectangles_______")
# Create two rectangles: taskbar_area and taskbar_notification_area
taskbar_area = canvas.create_rectangle(0, 0, 0, 0, fill="blue", outline="", tags="taskbar_area")
taskbar_notification_area = canvas.create_rectangle(0, 0, 0, 0, fill="gray", outline="", tags="taskbar_notification_area")

def taskbar_image_rectangles_resize(event):
    # Define the width for the main taskbar area
    taskbar_area_width = event.width * 0.80 # 68% width for main area

    # Update coordinates for the main taskbar area
    canvas.coords(taskbar_area, 0, event.height - taskbar_height, taskbar_area_width, event.height)

    # Calculate the notification area width based on the remaining space
    notification_area_width = event.width - taskbar_area_width

    # Update coordinates for the notification area
    canvas.coords(taskbar_notification_area, taskbar_area_width, event.height - taskbar_height, event.width, event.height)

on_window_event_callbacks.append(taskbar_image_rectangles_resize)

print("________Adding Rectangles to the Taskbar__________")
def create_taskbar_rectangle(x, width, color="red"):
    rect = canvas.create_rectangle(x, canvas.winfo_height() - taskbar_height,
                                   x + width, canvas.winfo_height(), fill=color, outline="")
    return rect

rectangles = []
rect_colors = ["red", "green", "blue", "yellow"]  # Example colors

# Add rectangles with varying positions and widths
for i, color in enumerate(rect_colors):
    rect = create_taskbar_rectangle(10 + i * 60, 50, color)  # Example spacing and width
    rectangles.append(rect)

def update_rectangles_position(event):
    for i, rect in enumerate(rectangles):
        canvas.coords(rect, 10 + i * 60, event.height - taskbar_height,
                      60 + i * 60, event.height)

on_window_event_callbacks.append(update_rectangles_position)

window.mainloop()
