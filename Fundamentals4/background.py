import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

on_window_event_callbacks = []
def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)
window.bind("<Configure>", on_window_event)

from PIL import Image, ImageTk
background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

def testz(event):
    print("teeest")

on_window_event_callbacks.append(testz)

window.mainloop()