import tkinter as tk

def draw_centered_text(canvas, x, y, width, height, text):
    # Coordinates for the rectangle
    x1, y1 = x, y
    x2, y2 = x + width, y + height
    
    # Draw the rectangle
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
    
    # Calculate the center for the text
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    # Draw the text
    canvas.create_text(center_x, center_y, text=text, font=("Arial", 12), fill="black")

# Create the main window
root = tk.Tk()
root.geometry("400x400")

# Create a canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Draw a rectangle with centered text
draw_centered_text(canvas, 50, 100, 200, 50, "Hello, World!")

# Run the Tkinter event loop
root.mainloop()
