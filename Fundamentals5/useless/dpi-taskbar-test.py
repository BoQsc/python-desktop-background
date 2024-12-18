import tkinter as tk

# Create the main window
root = tk.Tk()
root.attributes('-fullscreen', True)

# Get screen dimensions
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# DPI scaling
dpi_scaling = root.tk.call('tk', 'scaling')

# Create canvas
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Function to update canvas dimensions and images
def update_canvas(event=None):
    canvas_width = int(event.width * 0.8)  # 80% of canvas width
    canvas_height = event.height

    # Apply DPI scaling
    canvas.config(width=canvas_width * dpi_scaling, height=canvas_height * dpi_scaling)

    # Clear previous drawings
    canvas.delete('all')

    # First image without DPI scaling
    canvas.create_rectangle(10, 10, canvas_width, 50, fill='red')

    # Second image with DPI scaling
    canvas.create_rectangle(10, 70, canvas_width, 50 * dpi_scaling, fill='red')

# Bind window resize event to update_canvas function
root.bind('<Configure>', update_canvas)

# Initial call to set canvas size
update_canvas()

# Run the application
root.mainloop()
