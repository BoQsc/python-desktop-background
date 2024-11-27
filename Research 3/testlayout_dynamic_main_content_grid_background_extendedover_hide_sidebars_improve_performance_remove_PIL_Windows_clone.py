import tkinter as tk

def create_desktop(canvas):
    # Get canvas dimensions
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Toolbar dimensions (taskbar)
    toolbar_height = 50
    
    # Main content (desktop area) dimensions
    content_width = canvas_width
    content_height = canvas_height - toolbar_height
    
    # Clear previous drawings
    canvas.delete("all")
    
    # Load and display the background image to fill the entire canvas
    try:
        bg_photo = tk.PhotoImage(file="background.png")
        canvas.create_image(0, 0, anchor="nw", image=bg_photo)
        canvas.bg_photo = bg_photo  # Keep a reference to avoid garbage collection
    except tk.TclError:
        print("background.png not found or unsupported format.")
    
    # Create the main desktop area
    canvas.create_rectangle(0, 0, content_width, content_height, outline="black")
    
    # Add desktop icons (simulated)
    icon_size = 64  # Icon size (width and height)
    icon_spacing = 100  # Spacing between icons
    icons_per_row = content_width // icon_spacing
    icons = ["Computer", "Recycle Bin", "Network", "Folder"]
    for i, icon in enumerate(icons):
        col = i % icons_per_row
        row = i // icons_per_row
        x = col * icon_spacing + icon_spacing // 2
        y = row * icon_spacing + icon_spacing // 2
        canvas.create_rectangle(x - icon_size // 2, y - icon_size // 2, 
                                x + icon_size // 2, y + icon_size // 2, 
                                fill="lightblue", outline="black")
        canvas.create_text(x, y + icon_size // 2 + 10, text=icon, font=("Arial", 10))
    
    # Create the taskbar (toolbar at the bottom)
    canvas.create_rectangle(0, canvas_height - toolbar_height, canvas_width, canvas_height, fill="darkgray", outline="black")
    canvas.create_text(canvas_width // 2, canvas_height - toolbar_height // 2, text="Taskbar", font=("Arial", 16))

# Create the main window
root = tk.Tk()
root.title("Windows Shell Simulation")

# Create the canvas widget
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the resizing event to update the layout
canvas.bind("<Configure>", lambda event: create_desktop(canvas))

# Run the application
root.mainloop()
