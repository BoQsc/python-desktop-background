import tkinter
from PIL import Image, ImageTk
import threading
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
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

        def resize_async():
            resized_width = event.width
            resized_height = int(background_image.height * (event.width / background_image.width))
            resized_image = background_image.resize((resized_width, resized_height), Image.Resampling.NEAREST)
            time.sleep(0.05)  # Shorter delay for smoother transition
            resized_photo = ImageTk.PhotoImage(resized_image)

            # Using a try-except block to handle updates in case of flickering
            try:
                canvas.itemconfig(canvas_background_widget, image=resized_photo)
                canvas.resized_photo = resized_photo
            except tkinter.TclError:
                pass  # Handle cases where the widget might have been destroyed

        threading.Thread(target=resize_async).start()

on_window_event_callbacks.append(resize_background_image)

window.mainloop()
