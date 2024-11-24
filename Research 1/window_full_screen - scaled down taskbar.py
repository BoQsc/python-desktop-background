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
screen_height = window.winfo_screenheight()

# Calculate scale factors - fixing the math here
width_scale = taskbar_image.width() // taskbar_width  # 1920 // 1536 should be 2
height_scale = taskbar_image.height() // 40  # 70 // 40 should be 2

# Take the larger scale to ensure proper downsizing
scale_factor = max(2, width_scale, height_scale)  # Force minimum scale of 2

# Resize the taskbar image
taskbar_image_resized = taskbar_image.subsample(scale_factor)

# Place the taskbar image at the bottom of the screen
canvas.create_image(taskbar_width // 2, screen_height, image=taskbar_image_resized, anchor="s")

# Print debug information
print(f"Screen width: {taskbar_width}")
print(f"Screen height: {screen_height}")
print(f"Original taskbar width: {taskbar_image.width()}")
print(f"Original taskbar height: {taskbar_image.height()}")
print(f"Resized taskbar width: {taskbar_image_resized.width()}")
print(f"Resized taskbar height: {taskbar_image_resized.height()}")
print(f"Width scale: {width_scale}")
print(f"Height scale: {height_scale}")
print(f"Final scale factor: {scale_factor}")

window.mainloop()