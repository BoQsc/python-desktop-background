import tkinter as tk
import subprocess
import time
from ctypes import windll, wintypes, byref
import win32gui
import win32con

def launch_program():
    # Launch an external program (example: Notepad)
    subprocess.Popen(["notepad.exe"])
    root.after(1000, embed_program)  # Allow time for the window to appear

def embed_program():
    # Find the external program's window (example: Notepad)
    hwnd_program = win32gui.FindWindow(None, "Untitled - Notepad")
    if hwnd_program:
        # Get the handle of the Tkinter canvas
        hwnd_canvas = canvas.winfo_id()

        # Remove decorations from the external window
        style = win32gui.GetWindowLong(hwnd_program, win32con.GWL_STYLE)
        style &= ~win32con.WS_OVERLAPPEDWINDOW  # Remove title bar and borders
        win32gui.SetWindowLong(hwnd_program, win32con.GWL_STYLE, style)

        # Embed the external window into the Tkinter canvas
        windll.user32.SetParent(hwnd_program, hwnd_canvas)

        # Resize the program window to fit the canvas
        windll.user32.MoveWindow(hwnd_program, 0, 0, canvas.winfo_width(), canvas.winfo_height(), True)

root = tk.Tk()
root.geometry("800x600")

canvas = tk.Canvas(root, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

button = tk.Button(root, text="Launch Program", command=launch_program)
button.pack()

root.mainloop()
