import tkinter

def load_window():
    window = tkinter.Tk()
    load_window_main(window)
    window.mainloop()

def load_window_main(window):
    canvas = tkinter.Canvas(window)


load_window()