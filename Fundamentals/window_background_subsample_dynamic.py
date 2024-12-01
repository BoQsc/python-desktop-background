import tkinter
window = tkinter.Tk()
window.title("Window Canvas")


canvas = tkinter.Canvas(bg="gray", highlightthickness=0)
canvas_background = tkinter.PhotoImage(file="background.png")




def handle_configure(event):
    canvas.place_configure(width=event.width, height=event.height)
    print(event.width %2)
    global canvas_background
    if event.width %2 == 1:
        canvas_background = canvas_background.subsample(500,500)
        canvas.create_image(0, 0, anchor="nw", image=canvas_background)
        print(event.width, event.height)

window.bind("<Configure>", lambda event: handle_configure(event))
# Implement background image resize based on canvas size.
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

window.mainloop()