import tkinter as tk

def on_hover(event):
    canvas.itemconfig(rect, fill="blue")

def off_hover(event):
    canvas.itemconfig(rect, fill="red")

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Create a rectangle
rect = canvas.create_rectangle(50, 50, 150, 150, fill="red")

# Bind hover events
canvas.tag_bind(rect, "<Enter>", on_hover)
canvas.tag_bind(rect, "<Leave>", off_hover)

root.mainloop()
