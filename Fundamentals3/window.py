print(program:="Python Desktop [Version 0.0.0]".replace("0.0.0", version:="0.0.1"))
print(credits:="Public Domain. No rights reserved.")
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

print("________Canvas Taskbar._________") # Make Taskbar update function that does initialization and updates to the taskbar. Use init to do first init function before updating further.
class Taskbar:
    def __init__(self):
        Taskbar.height = 40

        print("________Canvas Taskbar Image__________")
        Taskbar.image = Image.new("RGBA", (1, Taskbar.height), (0, 0, 255, 128))  # Initial size of 1px
        Taskbar.image = Image.open("taskbar.png")
        Taskbar.photo = ImageTk.PhotoImage(Taskbar.image)
        Taskbar.image_taskbar = canvas.create_image(0, 0, anchor="nw", image=Taskbar.photo)
        
    def image_resize(self, event):
        resized_image = Taskbar.image.resize((event.width, Taskbar.height), Image.Resampling.LANCZOS)
        canvas.tresized_photo = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(Taskbar.image_taskbar, image=canvas.tresized_photo)
        canvas.coords(Taskbar.image_taskbar, 0, event.height - Taskbar.height)  

on_window_event_callbacks.append(Taskbar().image_resize)






window.mainloop()
