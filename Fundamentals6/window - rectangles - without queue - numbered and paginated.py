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

rectangles = []
current_page = 0

def resize_background_image(event, _last=[None, None]):
    if (event.width, event.height) != tuple(_last):
        _last[:] = [event.width, event.height]
        resized_image = background_image.resize((event.width, event.height), Image.Resampling.NEAREST)
        canvas.resized_photo = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

on_window_event_callbacks.append(resize_background_image)

def update_rectangles(event):
    global taskbar_photo, rectangles

    taskbar_area_width = int(event.width * 0.77 + dpi_scaling)    
    notification_area_width = event.width - taskbar_area_width

    canvas.coords(taskbar_area, 0, event.height - taskbar_height, taskbar_area_width, event.height)
    canvas.coords(taskbar_notification_area, taskbar_area_width, event.height - taskbar_height, event.width, event.height)

    resized_taskbar_image = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.NEAREST)
    taskbar_photo = ImageTk.PhotoImage(resized_taskbar_image)
    taskbar_widget = canvas.create_image(0, event.height - taskbar_height, anchor="nw", image=taskbar_photo)
    canvas.tag_lower(taskbar_widget)

    # Padding and rectangle dimensions
    padding = 6
    rect_width = 50

    # Maximum number of rectangles that fit within taskbar_area_width
    num_visible_rectangles = (taskbar_area_width - padding) // (rect_width + padding)

    # Update rectangle display based on current page
    display_rectangles(num_visible_rectangles, event.height, rect_width, padding)

on_window_event_callbacks.append(update_rectangles)

def display_rectangles(num_visible, height, rect_width, padding):
    canvas.delete("rects")
    canvas.delete("nums")

    start_index = current_page * num_visible
    end_index = min(start_index + num_visible, len(rectangles))

    for i, rect_number in enumerate(range(start_index, end_index)):
        x1 = i * (rect_width + padding) + padding
        x2 = x1 + rect_width
        y1 = height - taskbar_height + padding
        y2 = height - padding
        canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="", tags="rects")
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(rect_number + 1), fill="white", tags="nums")

def on_key_press(event):
    global current_page, last_event
    if last_event is None:
        return  # Ensure there is an event to use for calculations

    taskbar_area_width = int(last_event.width * 0.77 + dpi_scaling)
    padding = 6
    rect_width = 50
    num_visible_rectangles = (taskbar_area_width - padding) // (rect_width + padding)

    if event.keysym == "Up":
        if current_page > 0:
            current_page -= 1
    elif event.keysym == "Down":
        max_pages = (len(rectangles) - 1) // num_visible_rectangles + 1
        if current_page < max_pages - 1:
            current_page += 1

    update_rectangles(last_event)

def initialize_rectangles(count):
    global rectangles
    rectangles = list(range(count))

# Initialize with some rectangles
initialize_rectangles(50)  # Example: 50 rectangles

window.bind("<Configure>", lambda event: on_window_event(event))
window.bind("<Up>", on_key_press)
window.bind("<Down>", on_key_press)

window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

last_event = None
def on_window_event(event):
    global last_event
    last_event = event
    for callback in on_window_event_callbacks:
        callback(event)

window.mainloop()
