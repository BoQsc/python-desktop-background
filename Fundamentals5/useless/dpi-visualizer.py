import tkinter as tk
from tkinter import messagebox

def create_fullscreen_window():
    root = tk.Tk()
    root.attributes("-fullscreen", True)

    # Calculate number of dots based on screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    dot_size = 10  # Size of each dot
    rows = screen_height // dot_size
    columns = screen_width // dot_size

    # Function to create a grid of dots
    def draw_grid():
        for i in range(rows):
            for j in range(columns):
                x = j * dot_size
                y = i * dot_size
                canvas.create_rectangle(x, y, x + dot_size, y + dot_size, fill="blue")

    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()
    
    draw_grid()

    root.mainloop()

create_fullscreen_window()
