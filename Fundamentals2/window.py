import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("Window Canvas")

print("_______PIP Auto install Dependencies__________")
print("_______PIL Loading background PhotoImage__________")

background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)

print("________TK Loading canvas widget__________")
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True) 
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

def background_image_resize(event):
    resized_image = background_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
    canvas.resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)
    

def on_window_event(event):
    canvas.config(width=event.width, height=event.height)
    background_image_resize(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
