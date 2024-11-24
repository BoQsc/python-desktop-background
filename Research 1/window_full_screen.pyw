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

window.mainloop()