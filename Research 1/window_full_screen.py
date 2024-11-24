import tkinter

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

# Stretch the taskbar image to the width of the window
print(taskbar_image.height())
taskbar_image_resized = taskbar_image.subsample(1, int(taskbar_image.height() / taskbar_image.height()))

# Get the window's screen height after fullscreen
screen_height = window.winfo_screenheight()

# Place the taskbar image at the bottom of the screen
canvas.create_image(taskbar_width // 2, screen_height, image=taskbar_image_resized, anchor="s")

window.mainloop()
