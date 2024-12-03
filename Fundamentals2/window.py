import tkinter
window = tkinter.Tk()
window.title("Window Canvas")

print("_______PIP Auto install Dependencies__________")
print("_______PIL Loading background PhotoImage__________")
background_file = "background.png"
from PIL import Image, ImageTk
background_ImageFile = Image.open(background_file)
background_PhotoImage = ImageTk.PhotoImage(image=background_ImageFile)


print("________TK Loading canvas widget__________")
canvas = tkinter.Canvas(bg="gray", highlightthickness=0)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_PhotoImage)

def background_image_resize(event):
    print(event.width, event.height)
    pass

def on_window_event(event):
    canvas.place_configure(width=event.width, height=event.height)
    background_image_resize(event)
window.bind("<Configure>", on_window_event)

# Implement background image resize based on canvas size.
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()