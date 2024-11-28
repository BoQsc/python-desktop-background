import tkinter
window = tkinter.Tk()
window.title("Window Canvas")

canvas = tkinter.Canvas(bg="gray", bd=0, highlightthickness=0)



window.bind("<Configure>", lambda event: canvas.place_configure(width=event.width, height=event.height))
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()