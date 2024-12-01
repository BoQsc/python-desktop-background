import tkinter
window = tkinter.Tk()
window.title("Window Canvas")


canvas = tkinter.Canvas(bg="gray", highlightthickness=0)

canvas_background = tkinter.PhotoImage(file="background.png")
canvas_background = canvas_background.subsample(2,2)
canvas_background = canvas_background.subsample(2,2)

canvas.create_image(0, 0, anchor="nw", image=canvas_background)

window.bind("<Configure>", lambda event: canvas.place_configure(width=event.width, height=event.height))
# Implement background image resize based on canvas size.
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()