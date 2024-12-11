import tkinter

class Window:
    def __init__(self):
        self.widget = tkinter.Tk()
        self.widget.title("Python Desktop")
        self.widget.geometry("800x600")
        self.widget.bind("<Configure>", self.on_window_event)

    def on_window_event(self, event):
        print("Resize test")

class Canvas:
    def __init__(self, window):
        self.widget = tkinter.Canvas(window.widget, bg="gray", highlightthickness=0)
        self.widget.pack(fill="both", expand=True)

# Create the main window
window = Window()

# Add the canvas to the window
canvas = Canvas(window)

# Start the main loop
window.widget.mainloop()
