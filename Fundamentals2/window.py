import tkinter
from PIL import Image, ImageTk
on_window_event_callbacks = []

window = tkinter.Tk()
window.title("Window Canvas")

print("_______PIP Auto install Dependencies__________")
print("________TK Loading canvas widget__________")
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

print("_______PIL Loading background PhotoImage__________")
background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

def background_image_resize(event):
    resized_image = background_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
    canvas.resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

on_window_event_callbacks.append(background_image_resize)

print("________Canvas Taskbar__________")
taskbar_height = 40

taskbar_rectangle = canvas.create_rectangle(
    0, canvas.winfo_height() - taskbar_height, canvas.winfo_width(), canvas.winfo_height(), 
    fill="black", outline=""
)

def taskbar_resize(event):
    canvas.coords(taskbar_rectangle, 0, event.height - taskbar_height, event.width, event.height)

on_window_event_callbacks.append(taskbar_resize)

print("________Canvas Taskbar Image__________")
taskbar_image = Image.new("RGBA", (1, taskbar_height), (0, 0, 255, 128))  # Initial size of 1px
taskbar_image = Image.open("taskbar.png")
taskbar_photo = ImageTk.PhotoImage(taskbar_image)
image_taskbar = canvas.create_image(0, 0, anchor="nw", image=taskbar_photo)

def taskbar_image_resize(event):
    resized_image = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.LANCZOS)
    canvas.tresized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(image_taskbar, image=canvas.tresized_photo)
    canvas.coords(image_taskbar, 0, event.height - taskbar_height)  

on_window_event_callbacks.append(taskbar_image_resize)

print("________TK Window Events__________")
def on_window_event(event):
    canvas.config(width=event.width, height=event.height)
    for callback in on_window_event_callbacks:
        callback(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
