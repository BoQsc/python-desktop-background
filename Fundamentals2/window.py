import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("Window Canvas")

print("_______PIP Auto install Dependencies__________")
print("________TK Loading canvas widget__________")
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

print("_______PIL Loading background PhotoImage__________")
background_file = "background.png"
background_image = Image.open(background_file)
background_photo = ImageTk.PhotoImage(image=background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

print("________Canvas Taskbar__________")
taskbar_height = 40

#rectangle_taskbar = canvas.create_rectangle(
#    0, canvas.winfo_height() - taskbar_height, canvas.winfo_width(), canvas.winfo_height(), 
#    fill="black", outline=""
#)

taskbar_image = Image.new("RGBA", (1, taskbar_height), (0, 0, 255, 128))  # Initial size of 1px
taskbar_image = Image.open("taskbar.png")
taskbar_photo = ImageTk.PhotoImage(taskbar_image)
image_taskbar = canvas.create_image(0, 0, anchor="nw", image=taskbar_photo)

print("________TK Window Events__________")
def background_image_resize(event):
    resized_image = background_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
    canvas.resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

def taskbar_image_resize(event):
    # 40 is hardcoded for now.
    resized_image = taskbar_image.resize((event.width, 40), Image.Resampling.LANCZOS)
    canvas.tresized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(image_taskbar, image=canvas.tresized_photo)



def on_window_event(event):
    canvas.config(width=event.width, height=event.height)
    background_image_resize(event)
    
    taskbar_image_resize(event)
    canvas.coords(image_taskbar, 0, event.height - taskbar_height)  
    try:  
        canvas.coords(rectangle_taskbar, 0, event.height - taskbar_height, event.width, event.height)
    except: pass
window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
