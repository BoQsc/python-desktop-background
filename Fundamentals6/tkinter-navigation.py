import tkinter
from PIL import Image, ImageTk
from ctypes import windll
from types import SimpleNamespace

windll.shcore.SetProcessDpiAwareness(1)

class RectangleNavigator:
    def __init__(self):
        self.current_page = 0
        self.total_rectangles = 50
        self.visible_rectangles = 0
    
    def next_page(self):
        if (self.current_page + 1) * self.visible_rectangles < self.total_rectangles:
            self.current_page += 1
            return True
        return False
    
    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            return True
        return False
    
    def get_visible_range(self):
        start = self.current_page * self.visible_rectangles
        end = min(start + self.visible_rectangles, self.total_rectangles)
        return start, end

navigator = RectangleNavigator()
window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

dpi_scaling = window.tk.call('tk', 'scaling')
canvas.scale("all", 0, 0, dpi_scaling, dpi_scaling)

on_window_resize_event_callbacks = []

background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

taskbar_image = Image.open("taskbar.png")
taskbar_photo = ImageTk.PhotoImage(image=taskbar_image)  
taskbar_height = int(32 * dpi_scaling)  

taskbar_area = canvas.create_rectangle(0, 0, 0, 0, fill="blue", outline="")
taskbar_notification_area = canvas.create_rectangle(0, 0, 0, 0, outline="gray")

# Store current window dimensions
current_dimensions = SimpleNamespace(width=window.winfo_width(), height=window.winfo_height())

def create_nav_buttons(event):
    canvas.delete("nav_buttons")
    
    # Prev button
    prev_button = canvas.create_rectangle(
        6, event.height - taskbar_height + 6,
        6 + nav_button_width, event.height - 6,
        fill="lightgray", tags=("nav_buttons", "prev_button")
    )
    canvas.create_text(
        6 + nav_button_width/2, event.height - taskbar_height/2,
        text="<", tags=("nav_buttons", "prev_button")
    )
    
    # Next button
    next_button = canvas.create_rectangle(
        42, event.height - taskbar_height + 6,
        42 + nav_button_width, event.height - 6,
        fill="lightgray", tags=("nav_buttons", "next_button")
    )
    canvas.create_text(
        42 + nav_button_width/2, event.height - taskbar_height/2,
        text=">", tags=("nav_buttons", "next_button")
    )

nav_button_width = 30
nav_button_height = taskbar_height - 12

def handle_button_click(event):
    clicked_items = canvas.find_withtag("current")
    if not clicked_items:
        return
        
    tags = canvas.gettags(clicked_items[0])
    redraw_needed = False
    
    if "prev_button" in tags:
        redraw_needed = navigator.prev_page()
    elif "next_button" in tags:
        redraw_needed = navigator.next_page()
        
    if redraw_needed:
        # Create a custom event with current window dimensions
        custom_event = SimpleNamespace(
            width=current_dimensions.width,
            height=current_dimensions.height
        )
        resize_taskbar(custom_event)

canvas.tag_bind("prev_button", "<Button-1>", handle_button_click)
canvas.tag_bind("next_button", "<Button-1>", handle_button_click)

def resize_background_image(event, _last=[None, None]):
    if (event.width, event.height) != tuple(_last):
        _last[:] = [event.width, event.height]
        resized_image = background_image.resize((event.width, event.height), Image.Resampling.NEAREST)
        canvas.resized_photo = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

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

    # Number of rectangles and padding
    padding = 6
    rect_width = 50  # Fixed width for each rectangle
    start_x = 80  # Start after the navigation buttons

    # Calculate max number of rectangles that fit within taskbar_area_width
    available_width = taskbar_area_width - start_x - padding
    navigator.visible_rectangles = min(navigator.total_rectangles, available_width // (rect_width + padding))

    # Get the current visible range of rectangles
    start_idx, end_idx = navigator.get_visible_range()

    canvas.delete("rects")  # Delete existing rectangles
    for i in range(start_idx, end_idx):
        idx = i - start_idx  # Use relative index for positioning
        x1 = start_x + idx * (rect_width + padding) + padding
        x2 = x1 + rect_width
        y1 = event.height - taskbar_height + padding
        y2 = event.height - padding
        
        # Create rectangle
        canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="", tags="rects")
        
        # Add number label
        canvas.create_text(
            (x1 + x2) / 2, (y1 + y2) / 2,
            text=str(i + 1),  # Add 1 to make it 1-based numbering
            fill="white",
            tags="rects"
        )
    
    create_nav_buttons(event)

on_window_resize_event_callbacks.extend([resize_background_image, resize_taskbar])

def on_window_resize_event(event, _last=[None, None]):
    if (event.width, event.height) == tuple(_last): return
    _last[:] = [event.width, event.height]
    # Update current dimensions
    current_dimensions.width = event.width
    current_dimensions.height = event.height
    for callback in on_window_resize_event_callbacks:
        callback(event)

window.bind("<Configure>", on_window_resize_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
