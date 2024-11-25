import tkinter as tk

def update_canvas_grid(event=None):
    """Update the canvas grid to cover the entire window."""
    canvas.delete("grid_line")  # Clear existing grid lines

    width = canvas.winfo_width()
    height = canvas.winfo_height()

    rows = height // cell_size
    cols = width // cell_size

    # Draw horizontal lines
    for i in range(rows + 1):
        y = i * cell_size
        canvas.create_line(0, y, width, y, fill="gray", tags="grid_line")

    # Draw vertical lines
    for j in range(cols + 1):
        x = j * cell_size
        canvas.create_line(x, 0, x, height, fill="gray", tags="grid_line")

root = tk.Tk()
cell_size = 50  # Size of each grid cell

# Create a resizable canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", update_canvas_grid)  # Redraw grid on resize

root.geometry("500x500")
root.mainloop()
