import tkinter
# Makes a canvas with a grid that is sticky to the N S E W
# Maybe grid should not be used for background image.
# background image should be a separate widget from Window to allow for modularity and separation from Window.
# background image should be custom canvas widget.


window = tkinter.Tk()
window.attributes('-fullscreen', True)

canvas = tkinter.Canvas(window, highlightthickness=0)
canvas.grid(row=0, column=0, sticky="nsew")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

bg_image = tkinter.PhotoImage(file="background.png")
bg_image = bg_image.subsample(int(bg_image.width() / window.winfo_screenwidth()), 
                              int(bg_image.height() / window.winfo_screenheight()))

canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Load taskbar image
taskbar_image = tkinter.PhotoImage(file="taskbar_transparent.png")
taskbar_width = window.winfo_screenwidth()

print(taskbar_image.height())

screen_height = window.winfo_screenheight()

# Place the taskbar image at the bottom of the screen
canvas.create_image(50, 50, image=taskbar_image)
    
window.mainloop()
