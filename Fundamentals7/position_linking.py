import tkinter as tk

def link_positions(canvas, container_id, dependent_id, offset=(0, 0)):
    """Links the position of a dependent canvas item to a container canvas item.
    
    Args:
        canvas: The tkinter canvas where both items are drawn.
        container_id: The ID of the container item.
        dependent_id: The ID of the dependent item.
        offset: A tuple (x_offset, y_offset) for the relative position.
    """
    def update_position(event=None):
        # Get the current position of the container
        container_coords = canvas.coords(container_id)
        if container_coords:
            # Update the dependent item based on the container's position
            x_offset, y_offset = offset
            new_coords = (container_coords[0] + x_offset, container_coords[1] + y_offset)
            canvas.coords(dependent_id, *new_coords)
    
    # Bind motion events to the update function
    canvas.tag_bind(container_id, "<B1-Motion>", update_position)
    canvas.tag_bind(container_id, "<ButtonRelease-1>", update_position)

# Example usage
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create a container rectangle
container = canvas.create_rectangle(50, 50, 150, 150, fill="blue", tags="container")
# Create a dependent rectangle
dependent = canvas.create_rectangle(0, 0, 50, 50, fill="red", tags="dependent")

# Link the dependent rectangle to the container rectangle
link_positions(canvas, container, dependent, offset=(100, 0))

root.mainloop()
