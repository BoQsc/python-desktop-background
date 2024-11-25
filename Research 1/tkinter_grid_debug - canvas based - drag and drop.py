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

def start_drag(event):
    """Store the initial mouse position when dragging starts."""
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def drag_square(event):
    """Move the square as the mouse is dragged."""
    global start_x, start_y, square
    delta_x = event.x - start_x
    delta_y = event.y - start_y

    # Move the square by the difference between the initial position and the new position
    canvas.move(square, delta_x, delta_y)

    # Update the start position for the next drag event
    start_x = event.x
    start_y = event.y

def drop_square(event):
    """Snap the square to the nearest grid cell when dropped."""
    global square
    # Get the current position of the square
    square_coords = canvas.coords(square)
    new_x = round(square_coords[0] / cell_size) * cell_size
    new_y = round(square_coords[1] / cell_size) * cell_size

    # Move the square to the new grid position
    canvas.coords(square, new_x, new_y, new_x + cell_size, new_y + cell_size)

root = tk.Tk()
cell_size = 50  # Size of each grid cell

# Create a resizable canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", update_canvas_grid)  # Redraw grid on resize

# Create a square inside the first grid cell
square = canvas.create_rectangle(cell_size, cell_size, 2 * cell_size, 2 * cell_size, fill="blue")

# Bind drag events to the square
canvas.tag_bind(square, "<ButtonPress-1>", start_drag)
canvas.tag_bind(square, "<B1-Motion>", drag_square)
canvas.tag_bind(square, "<ButtonRelease-1>", drop_square)

root.geometry("500x500")
root.mainloop()
