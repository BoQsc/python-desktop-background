import tkinter

# Function to create a DPI-independent rectangle
def create_dpi_independent_rectangle(canvas, x, y, width_in_inches, height_in_inches, dpi):
    # Convert dimensions from inches to pixels
    width = int(width_in_inches * dpi)
    height = int(height_in_inches * dpi)
    # Draw the rectangle
    canvas.create_rectangle(x, y, x + width, y + height, fill="blue")
    return height

# Function to create a DPI-dependent rectangle
def create_dpi_dependent_rectangle(canvas, x, y, width_in_pixels, height_in_pixels):
    # Draw the rectangle
    canvas.create_rectangle(x, y, x + width_in_pixels, y + height_in_pixels, fill="red")
    return height_in_pixels

# Initialize Tkinter
root = tkinter.Tk()

# Get the DPI
dpi = root.winfo_fpixels('1i')
print(f"DPI: {dpi}")

# Create a canvas
canvas = tkinter.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Dimensions for rectangles
independent_width_in_inches = 2
independent_height_in_inches = 1

dependent_width_in_pixels = 200
dependent_height_in_pixels = 100

# Create DPI-independent rectangle
independent_height = create_dpi_independent_rectangle(
    canvas, 50, 50, independent_width_in_inches, independent_height_in_inches, dpi
)

# Create DPI-dependent rectangle (to the right of the independent one)
dependent_height = create_dpi_dependent_rectangle(
    canvas, 300, 50, dependent_width_in_pixels, dependent_height_in_pixels
)

# Print heights
print(f"DPI-independent rectangle height (pixels): {independent_height}")
print(f"DPI-dependent rectangle height (pixels): {dependent_height}")

# Start the Tkinter main loop
root.mainloop()
