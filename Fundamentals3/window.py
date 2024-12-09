print(program:="Python Desktop [Version 0.0.0]".replace("0.0.0", version:="0.0.1"))
print(credits:="Public Domain. No rights reserved.")
print(description:=
"""
This is Canvas only project. Tkinter Canvas is used to render entire User Interface.
The Image object PhotoImage is used as a way to provide transparent widget elements 
and to make up most parts of this project. For more information visit the website.
""")
print("The current work consist of keeping consistent original code style.")
print("_______PIP Auto install Dependencies__________")
print("________TK Window Widget______________________")
__import__('os').system('title ' + program + "(Console)")
import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title(program + " - " + __import__('time').strftime("%Y-%m-%d"))

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

 # Make Taskbar update function that does initialization and updates to the taskbar. Use init to do first init function before updating further.
print("________Canvas Taskbar_________")  # Taskbar update function to handle initialization and updates.

class Taskbar:
    initialized = False  # Track whether the taskbar is initialized

    def update_image(Taskbar, canvas, window_event=None):
        if not Taskbar.initialized:
            # Initialization logic
            Taskbar.height = 40
            Taskbar.width = canvas.winfo_width()
            print("________Canvas Taskbar Image__________")
            Taskbar.image = Image.open("taskbar.png")
            Taskbar.photo = ImageTk.PhotoImage(Taskbar.image)
            Taskbar.image_placed = canvas.create_image(0, 0, anchor="nw", image=Taskbar.photo)
            Taskbar.initialized = True

        # Update logic
        new_width = window_event.width if window_event else canvas.winfo_width()
        resized_image = Taskbar.image.resize((new_width, Taskbar.height), Image.Resampling.LANCZOS)
        Taskbar.resized_photo = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(Taskbar.image_placed, image=Taskbar.resized_photo)
        canvas.coords(Taskbar.image_placed, 0, canvas.winfo_height() - Taskbar.height)

taskbar = Taskbar()
on_window_event_callbacks.append(lambda event: taskbar.update_image(canvas, event))







# Create a simple button widget
def increment_height():
    taskbar.height += 1
    taskbar.image_resize()
    print(f"New Taskbar height: {taskbar.height}")

button = tkinter.Button(canvas, text="Click Me", command=increment_height)
canvas.create_window((10, 10), window=button, anchor="nw")

window.mainloop()
