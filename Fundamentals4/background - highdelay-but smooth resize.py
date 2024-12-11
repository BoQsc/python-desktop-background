import tkinter
from PIL import Image, ImageTk
import threading

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

# Mutex to control concurrent image resizing
resize_lock = threading.Lock()

def resize_background_image(event, _last=[None, None]):
    if (event.width, event.height) != tuple(_last):
        _last[:] = [event.width, event.height]

        def resize_async():
            with resize_lock:
                new_width = event.width
                new_height = event.height

                if event.x < new_width // 1:  # Left side resize
                    resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    offset_x = 0
                else:  # Right side resize
                    resized_image = background_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    offset_x = -new_width + new_width

                resized_photo = ImageTk.PhotoImage(resized_image)

                # Safely update the canvas
                try:
                    canvas.itemconfig(canvas_background_widget, image=resized_photo)
                    canvas.resized_photo = resized_photo
                except tkinter.TclError:
                    pass

        threading.Thread(target=resize_async).start()

on_window_event_callbacks.append(resize_background_image)

window.mainloop()
