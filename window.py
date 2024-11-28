import tkinter
window = tkinter.Tk()
window.title("Window Canvas")

canvas = tkinter.Canvas(bg="gray")
canvas.place(x=0, y=0)


window.bind("<Configure>", lambda event: canvas.place_configure(width=event.width, height=event.height))


tkinter.mainloop()