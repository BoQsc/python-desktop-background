print(program:="Python Desktop [Version 0.0.0]".replace("0.0.0", version:="0.0.1"))
print(credits:="Public Domain. No rights reserved.")
print(description:=
"""
This is Canvas only project. Tkinter Canvas is used to render entire User Interface.
The Image object PhotoImage is used as a way to provide transparent widget elements 
and to make up most parts of this project. For more information visit the website.
""")
print("The current work consist of keeping consistent original code style.")
print("_______PIP Auto install Dependencies__________")
print("________TK Window Widget______________________")
__import__('os').system('title ' + program + "(Console)")
import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title(program + " - " + __import__('time').strftime("%Y-%m-%d"))
window.geometry("800x600")

print("________TK Window Events Init______________________")
on_window_event_callbacks = []

print("________TK Loading canvas widget______________")
canvas = tkinter.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill="both", expand=True)

window.mainloop()