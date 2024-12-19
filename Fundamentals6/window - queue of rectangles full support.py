import tkinter
from PIL import Image, ImageTk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

dpi_scaling = window.tk.call('tk', 'scaling')
canvas.scale("all", 0, 0, dpi_scaling, dpi_scaling)

on_window_event_callbacks = []

background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

taskbar_image = Image.open("taskbar.png")
taskbar_photo = ImageTk.PhotoImage(image=taskbar_image)  
taskbar_height = int(32 * dpi_scaling)  

taskbar_area = canvas.create_rectangle(0, 0, 0, 0, fill="blue", outline="")
taskbar_notification_area = canvas.create_rectangle(0, 0, 0, 0, fill="gray", outline="")

def resize_background_image(event, _last=[None, None]):
    if (event.width, event.height) != tuple(_last):
        _last[:] = [event.width, event.height]
        resized_image = background_image.resize((event.width, event.height), Image.Resampling.NEAREST)
        canvas.resized_photo = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

on_window_event_callbacks.append(resize_background_image)

def resize_taskbar(event):
    global taskbar_photo

    taskbar_area_width = int(event.width * 0.77 + dpi_scaling)    
    notification_area_width = event.width - taskbar_area_width

    canvas.coords(taskbar_area, 0, event.height - taskbar_height, taskbar_area_width, event.height)
    canvas.coords(taskbar_notification_area, taskbar_area_width, event.height - taskbar_height, event.width, event.height)

    resized_taskbar_image = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.NEAREST)
    taskbar_photo = ImageTk.PhotoImage(resized_taskbar_image)
    taskbar_widget = canvas.create_image(0, event.height - taskbar_height, anchor="nw", image=taskbar_photo)
    canvas.tag_lower(taskbar_widget)

    # Rectangle dimensions and padding
    padding = 6
    rect_width = 40  # Fixed width for each rectangle

    # Calculate the max number of rectangles that fit in the bottom taskbar
    num_rectangles = (taskbar_area_width - padding) // (rect_width + padding)
    total_rectangles = 40  # Total number of rectangles to display (adjust as needed)
    overflow_rectangles = max(0, total_rectangles - num_rectangles)

    canvas.delete("rects_main")  # Clear previous main taskbar rectangles
    canvas.delete("rects_top")   # Clear previous top taskbar rectangles

    # Draw rectangles on the main (bottom) taskbar
    for i in range(min(num_rectangles, total_rectangles)):
        x1 = i * (rect_width + padding) + padding
        x2 = x1 + rect_width
        y1 = event.height - taskbar_height + padding
        y2 = event.height - padding
        canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="", tags="rects_main")

    # Draw overflow rectangles on the top taskbar as needed
    top_taskbar_height = taskbar_height
    while overflow_rectangles > 0:
        num_rectangles_top = min(overflow_rectangles, num_rectangles)
        for i in range(num_rectangles_top):
            x1 = i * (rect_width + padding) + padding
            x2 = x1 + rect_width
            y1 = top_taskbar_height + padding
            y2 = top_taskbar_height + taskbar_height - padding
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="", tags="rects_top")

        overflow_rectangles -= num_rectangles_top
        top_taskbar_height += taskbar_height  # Increase the height of the next taskbar

on_window_event_callbacks.append(resize_taskbar)

def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
