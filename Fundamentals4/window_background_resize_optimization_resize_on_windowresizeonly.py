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
window.geometry("800x600")

print("________TK Window Events Init______________________")
on_window_event_callbacks = []
previous_size = (0, 0)  # Initialize previous window size

print("________TK Loading canvas widget______________")
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

print("_______PIL Loading background PhotoImage______")
background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

def background_image_resize(event):
    resized_image = background_image.resize((canvas.winfo_width(), canvas.winfo_height()), Image.Resampling.NEAREST)
    canvas.resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

on_window_event_callbacks.append(background_image_resize)

print("________TK Window Events______________________")

def on_window_event(event):
    global previous_size
    current_size = (event.width, event.height)
    
    # Trigger callbacks only if the size has changed
    if current_size != previous_size:
        canvas.config(width=event.width, height=event.height)
        for callback in on_window_event_callbacks:
            callback(event)
        previous_size = current_size  # Update previous size

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))
window.after(100, lambda: window.geometry(f"{window.winfo_width()-1}x{window.winfo_height()-1}")) # This Quickfix: Reduces overall window size -1px but triggers <Configure> on application start.

window.mainloop()
