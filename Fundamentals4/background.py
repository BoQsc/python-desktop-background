import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

on_window_event_callbacks = []
def on_window_event(event):
    for callback in on_window_event_callbacks:
        callback(event)
window.bind("<Configure>", on_window_event)



def testz(event):
    print("teeest")

on_window_event_callbacks.append(testz)

window.mainloop()