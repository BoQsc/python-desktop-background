import tkinter
#import background
window = tkinter.Tk()
window.title("Window Canvas")


# Image_loader
background_file = "background.png"

background_PhotoImage = tkinter.PhotoImage(file=background_file)

from PIL import Image, ImageTk
background_ImageFile = Image.open(background_file)
background_PhotoImage = ImageTk.PhotoImage(background_ImageFile)

    

canvas = tkinter.Canvas(bg="gray", highlightthickness=0)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_PhotoImage)

def resize_image(event):


    #canvas_background.resize()
    pass

def window_configure(event):
    canvas.place_configure(width=event.width, height=event.height)
window.bind("<Configure>", window_configure)


# Implement background image resize based on canvas size.
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()