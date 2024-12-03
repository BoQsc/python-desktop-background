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
taskbar_height = 50  
taskbar = canvas.create_rectangle(0, canvas.winfo_height() - taskbar_height, canvas.winfo_width(), canvas.winfo_height(), fill="black", outline="")

#taskbar_image = Image.new("RGBA", (canvas.winfo_width(), taskbar_height), (0, 0, 255, 128))  # (R, G, B, A)
#taskbar_photo = ImageTk.PhotoImage(taskbar_image)

#taskbar = canvas.create_image(0, canvas.winfo_height() - taskbar_height, anchor="nw", image=taskbar_photo)

print("________TK Window Events__________")
def background_image_resize(event):
    resized_image = background_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
    canvas.resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)

def taskbar_image_resize(event):
    taskbar_image_resized = taskbar_image.resize((event.width, taskbar_height), Image.Resampling.LANCZOS)
    canvas.taskbar_photo = ImageTk.PhotoImage(taskbar_image_resized)
    canvas.itemconfig(taskbar, image=canvas.taskbar_photo)

def on_window_event(event):
    canvas.config(width=event.width, height=event.height)
    background_image_resize(event)
    canvas.coords(taskbar, 0, event.height - taskbar_height, event.width, event.height)
    #canvas.coords(taskbar, 0, event.height - taskbar_height)
    taskbar_image_resize(event)

window.bind("<Configure>", on_window_event)
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()
