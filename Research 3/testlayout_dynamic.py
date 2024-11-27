import tkinter as tk

def create_layout_with_sidebar(canvas):
    # Get current canvas dimensions
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Toolbar and sidebar dimensions
    topbar_height = 50
    sidebar_width = 100
    toolbar_height = 50
    
    # Main content area dimensions
    content_width = canvas_width - sidebar_width * 2  # Subtract space for both sidebars
    content_height = canvas_height - topbar_height - toolbar_height  # Subtract space for top and bottom bars
    
    # Clear previous drawings
    canvas.delete("all")
    
    # Create the top bar
    canvas.create_rectangle(0, 0, canvas_width, topbar_height, fill="darkblue", outline="black")
    canvas.create_text(canvas_width//2, topbar_height//2, text="Top Bar", font=("Arial", 16), fill="white")
    
    # Create the left sidebar
    canvas.create_rectangle(0, topbar_height, sidebar_width, canvas_height - toolbar_height, fill="lightblue", outline="black")
    canvas.create_text(sidebar_width//2, (topbar_height + (canvas_height - toolbar_height))//2, text="Left Sidebar", font=("Arial", 12))
    
    # Create the right sidebar
    canvas.create_rectangle(canvas_width - sidebar_width, topbar_height, canvas_width, canvas_height - toolbar_height, fill="lightgreen", outline="black")
    canvas.create_text(canvas_width - sidebar_width + sidebar_width//2, (topbar_height + (canvas_height - toolbar_height))//2, text="Right Sidebar", font=("Arial", 12))
    
    # Create the main content area
    canvas.create_rectangle(sidebar_width, topbar_height, sidebar_width + content_width, topbar_height + content_height, fill="lightgray", outline="black")
    canvas.create_text(sidebar_width + content_width//2, topbar_height + content_height//2, text="Main Content", font=("Arial", 16))
    
    # Create the toolbar at the bottom
    canvas.create_rectangle(0, canvas_height - toolbar_height, canvas_width, canvas_height, fill="darkgray", outline="black")
    canvas.create_text(canvas_width//2, canvas_height - toolbar_height + toolbar_height//2, text="Toolbar", font=("Arial", 16))

# Create the main window
root = tk.Tk()
root.title("Dynamic Layout with Top Bar and Sidebars")

# Create the canvas widget
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the resizing event to update the layout
canvas.bind("<Configure>", lambda event: create_layout_with_sidebar(canvas))

# Run the application
root.mainloop()
