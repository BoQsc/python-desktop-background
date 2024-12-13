import tkinter

# Function to create a DPI-independent rectangle
def create_dpi_independent_rectangle(canvas, x, y, width_in_inches, height_in_inches, dpi):
    # Convert dimensions from inches to pixels
    width = int(width_in_inches * dpi)
    height = int(height_in_inches * dpi)
    # Draw the rectangle
    canvas.create_rectangle(x, y, x + width, y + height, fill="blue")

# Initialize Tkinter
root = tkinter.Tk()

# Get the DPI
dpi = root.winfo_fpixels('1i')
print(f"DPI: {dpi}")

# Create a canvas
canvas = tkinter.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create a rectangle of 2x1 inches at position (50, 50)
create_dpi_independent_rectangle(canvas, 50, 50, 2, 1, dpi)

# Start the Tkinter main loop
root.mainloop()
