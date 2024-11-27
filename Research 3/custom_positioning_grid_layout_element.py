import tkinter as tk

class CanvasGrid:
    def __init__(self, parent, rows, cols, cell_width, cell_height):
        self.canvas = tk.Canvas(parent, width=cols * cell_width, height=rows * cell_height)
        self.rows = rows
        self.cols = cols
        self.cell_width = cell_width
        self.cell_height = cell_height

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.cell_width
                y1 = row * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

    def place_element(self, element, row, col):
        x = col * self.cell_width + self.cell_width // 2
        y = row * self.cell_height + self.cell_height // 2
        self.canvas.create_window(x, y, window=element)

    def pack(self, **kwargs):
        self.canvas.pack(**kwargs)


# Example Usage
root = tk.Tk()
root.geometry("400x400")

grid = CanvasGrid(root, rows=5, cols=5, cell_width=80, cell_height=80)
grid.draw_grid()

# Add elements to specific grid cells
btn1 = tk.Button(root, text="Button 1")
grid.place_element(btn1, row=1, col=1)

btn2 = tk.Button(root, text="Button 2")
grid.place_element(btn2, row=3, col=2)

grid.pack()

root.mainloop()
