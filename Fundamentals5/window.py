import tkinter
from PIL import Image, ImageTk

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

print("Loading Window Canvas")
window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)
scaling_factor = window.tk.call('tk', 'scaling')
canvas.scale("all", 0, 0, scaling_factor, scaling_factor)


on_window_event_callbacks = []

def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))


background_file = "background.png"
background_image = Image.open(background_file)

background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

def resize_background_image(event, _last=[None, None]):
    if (event.width, event.height) != tuple(_last):
        _last[:] = [event.width, event.height]
        resized_image = background_image.resize((event.width, event.height), Image.Resampling.NEAREST)
        canvas.resized_photo = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

on_window_event_callbacks.append(resize_background_image)

canvas.taskbar_image = Image.open("taskbar.png")
canvas.taskbar_photo = ImageTk.PhotoImage(canvas.taskbar_image)
canvas.taskbar_image_placed = canvas.create_image(0, 0, anchor="nw", image=canvas.taskbar_photo)
def update_taskbar(event):
    canvas_height = canvas.winfo_height()
    print(canvas_height)
    taskbar_height = 47 

    resized_image = canvas.taskbar_image.resize((canvas.winfo_width(), taskbar_height), Image.Resampling.NEAREST)
    canvas.taskbar_photo_resized = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas.taskbar_image_placed, image=canvas.taskbar_photo)
    canvas.coords(canvas.taskbar_image_placed, 0, canvas.winfo_height() - taskbar_height)

on_window_event_callbacks.append(update_taskbar)




window.mainloop()
