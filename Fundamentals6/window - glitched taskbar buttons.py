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

current_taskbar = 1
total_taskbars = 0

def resize_taskbar(event):
    global taskbar_photo, total_taskbars

    if event.width <= 0 or event.height <= 0:
        return  # Skip if invalid dimensions

    taskbar_area_width = int(event.width * 0.77 + dpi_scaling)
    taskbar_height = int(32 * dpi_scaling)

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
    canvas.delete("text")        # Clear previous numbering texts
    canvas.delete("taskbar_text")  # Clear taskbar numbering
    canvas.delete("arrow_up")
    canvas.delete("arrow_down")

    total_taskbars = -(-total_rectangles // num_rectangles)  # Ceiling division

    # Draw rectangles and taskbar number on the main (bottom) taskbar
    taskbar_number = current_taskbar
    canvas.create_text(
        event.width // 2, 
        event.height - taskbar_height - 10,  # Above the main taskbar
        text=f"Taskbar {taskbar_number}", 
        anchor="center", 
        fill="white", 
        tags="taskbar_text"
    )
    for i in range(min(num_rectangles, total_rectangles)):
        x1 = i * (rect_width + padding) + padding
        x2 = x1 + rect_width
        y1 = event.height - taskbar_height + padding
        y2 = event.height - padding
        index = (current_taskbar - 1) * num_rectangles + i + 1
        canvas.create_rectangle(x1, y1, x2, y2, fill="red" if index <= current_taskbar * num_rectangles else "blue", outline="", tags="rects_main")
        # Add numbering inside rectangles
        canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(index), fill="white", tags="text")

    # Draw overflow rectangles and number the taskbars above them
    top_taskbar_height = event.height - taskbar_height * 2
    for i in range(1, total_taskbars):
        num_rectangles_top = min(num_rectangles, total_rectangles - i * num_rectangles)
        canvas.create_text(
            event.width // 2,
            top_taskbar_height - 10,  # Above the overflow taskbar
            text=f"Taskbar {i + 1}",
            anchor="center",
            fill="white",
            tags="taskbar_text"
        )
        for j in range(num_rectangles_top):
            x1 = j * (rect_width + padding) + padding
            x2 = x1 + rect_width
            y1 = top_taskbar_height + padding
            y2 = top_taskbar_height + taskbar_height - padding
            index = i * num_rectangles + j + 1
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue" if index <= current_taskbar * num_rectangles else "red", outline="", tags="rects_top")
            # Add numbering inside rectangles
            canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(index), fill="white", tags="text")
        top_taskbar_height -= taskbar_height  # Move up for the next taskbar

    # Draw arrow buttons
    arrow_size = 20
    arrow_color = "white"
    arrow_up_x = event.width - arrow_size - 10
    arrow_up_y = event.height - taskbar_height - arrow_size - 10
    arrow_down_x = event.width - arrow_size - 10
    arrow_down_y = event.height - arrow_size - 10
    canvas.create_polygon(arrow_up_x, arrow_up_y, arrow_up_x + arrow_size, arrow_up_y, arrow_up_x + arrow_size / 2, arrow_up_y + arrow_size, fill=arrow_color, tags="arrow_up")
    canvas.create_polygon(arrow_down_x, arrow_down_y, arrow_down_x + arrow_size, arrow_down_y, arrow_down_x + arrow_size / 2, arrow_down_y - arrow_size, fill=arrow_color, tags="arrow_down")

    canvas.tag_bind("arrow_up", "<1>", lambda event: navigate_taskbars(-1))
    canvas.tag_bind("arrow_down", "<1>", lambda event: navigate_taskbars(1))


def navigate_taskbars(direction):
    global current_taskbar
    current_taskbar = max(1, min(current_taskbar + direction, total_taskbars))
    window.event_generate("<Configure>")

on_window_event_callbacks.append(resize_taskbar)

def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
