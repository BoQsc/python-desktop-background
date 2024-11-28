import tkinter as tk

def create_taskbar_window():
    root = tk.Tk()
    root.title("Fullscreen with Taskbar")

    # Set fullscreen window
    root.attributes('-fullscreen', True)
    
    # Background color
    root.configure(bg="black")
    
    # Create a taskbar frame at the bottom
    taskbar = tk.Frame(root, bg="gray", height=40)
    taskbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Add a few buttons to the taskbar for demonstration
    tk.Button(taskbar, text="Start", command=lambda: print("Start clicked")).pack(side=tk.LEFT, padx=10)
    tk.Button(taskbar, text="Search", command=lambda: print("Search clicked")).pack(side=tk.LEFT, padx=10)
    tk.Button(taskbar, text="Settings", command=lambda: print("Settings clicked")).pack(side=tk.RIGHT, padx=10)
    
    # Exit button for testing
    tk.Button(taskbar, text="Exit", command=root.destroy).pack(side=tk.RIGHT, padx=10)

    root.mainloop()

create_taskbar_window()
