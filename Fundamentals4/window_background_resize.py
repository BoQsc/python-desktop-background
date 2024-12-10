from PIL import Image, ImageTk
import tkinter

window = tkinter.Tk()
window.geometry("800x600")

canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

background_file = "background.png"
background_image = Image.open(background_file)

# Initial display of the background
background_photo = ImageTk.PhotoImage(background_image)
canvas_background_widget = canvas.create_image(0, 0, anchor="nw", image=background_photo)

# Delay mechanism for resize optimization
resize_delay = 100  # milliseconds
resize_job = None


def resize_background():
    resized_image = background_image.resize((canvas.winfo_width(), canvas.winfo_height()), Image.Resampling.NEAREST)
    canvas.resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(canvas_background_widget, image=canvas.resized_photo)


def background_image_resize(event):
    global resize_job
    if resize_job:
        window.after_cancel(resize_job)
    resize_job = window.after(resize_delay, resize_background)


window.bind("<Configure>", background_image_resize)

window.mainloop()
