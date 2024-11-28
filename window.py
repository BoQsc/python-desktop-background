import tkinter
window = tkinter.Tk()
window.title("Window Canvas")

canvas = tkinter.Canvas(bg="gray")



window.bind("<Configure>", lambda event: canvas.place_configure(width=event.width, height=event.height))
window.mainloop()