import tkinter

class Window:
    def load_window(window):
        window.widget = tkinter.Tk()
        window.widget.title("Python Desktop")
        window.widget.geometry("800x600")
        window.widget.bind("<Configure>", Window.on_window_event)
        window.widget.mainloop()

    def on_window_event(event):
        print("Resize test")

    def __init__(window):
        window.load_window()
window = Window()

class Canvas:
    def load_canvas(canvas, window):
        canvas.widget = tkinter.Canvas(window, bg="gray", highlightthickness=0)
        canvas.widget.pack(fill="both", expand=True)
    def __init__(canvas):
        canvas.load_canvas()
        
canvas = Canvas(window)


class Background():
    def update_background(self):
        pass

