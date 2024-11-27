import tkinter as tk

def create_layout_with_sidebar(canvas):
    # Get current canvas dimensions
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Toolbar and sidebar dimensions
    topbar_height = 50
    toolbar_height = 50
    
    # Main content area dimensions
    content_width = canvas_width  # Full width of the canvas
    content_height = canvas_height - topbar_height - toolbar_height  # Subtract space for top and bottom bars
    
    # Clear previous drawings
    canvas.delete("all")
    
    # Load and display the background image to fill the entire canvas
    try:
        bg_photo = tk.PhotoImage(file="background.png")
        canvas.create_image(0, 0, anchor="nw", image=bg_photo)
        canvas.bg_photo = bg_photo  # Keep a reference to avoid garbage collection
    except tk.TclError:
        print("background.png not found or unsupported format.")
    
    # Create the top bar
    canvas.create_rectangle(0, 0, canvas_width, topbar_height, fill="darkblue", outline="black")
    canvas.create_text(canvas_width//2, topbar_height//2, text="Top Bar", font=("Arial", 16), fill="white")
    
    # Create the main content area (occupying the full width of the canvas)
    canvas.create_rectangle(0, topbar_height, canvas_width, topbar_height + content_height, outline="black")
    canvas.create_text(canvas_width//2, topbar_height + content_height//2, text="Main Content", font=("Arial", 16))
    
    # Overlay grid on top of the main content area
    grid_spacing = 50  # Space between grid lines
    for x in range(0, canvas_width, grid_spacing):
        canvas.create_line(x, topbar_height, x, topbar_height + content_height, fill="black")
    for y in range(topbar_height, topbar_height + content_height, grid_spacing):
        canvas.create_line(0, y, canvas_width, y, fill="black")
    
    # Create the toolbar at the bottom
    canvas.create_rectangle(0, canvas_height - toolbar_height, canvas_width, canvas_height, fill="darkgray", outline="black")
    canvas.create_text(canvas_width//2, canvas_height - toolbar_height + toolbar_height//2, text="Toolbar", font=("Arial", 16))

# Create the main window
root = tk.Tk()
root.title("Layout with Background, Top Bar, and Grid")

# Create the canvas widget
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the resizing event to update the layout
canvas.bind("<Configure>", lambda event: create_layout_with_sidebar(canvas))

# Run the application
root.mainloop()
