import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

window = tk.Tk()
canvas = tk.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

on_window_event_callbacks = []
def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)
window.bind("<Configure>", on_window_event)

background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

def resize_background_image(event, _last=[None, None]):
    if (event.width, event.height) != tuple(_last):
        _last[:] = [event.width, event.height]

        def resize_with_delay():
            
            resized_image = background_image.resize((event.width, event.height), Image.Resampling.NEAREST)
            new_photo = ImageTk.PhotoImage(resized_image)
            canvas.itemconfig(canvas_background_widget, image=new_photo)
            canvas.photo = new_photo  # Prevent garbage collection

        threading.Thread(target=resize_with_delay).start()

on_window_event_callbacks.append(resize_background_image)

window.mainloop()
