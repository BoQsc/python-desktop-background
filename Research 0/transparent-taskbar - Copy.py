import tkinter as tk
import win32gui
import win32process
import psutil

def get_active_window_name():
    """Get the name of the active window."""
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    try:
        process = psutil.Process(pid)
        return process.name()
    except psutil.Error:
        return "Unknown"

def create_taskbar_window():
    root = tk.Tk()
    root.title("Fullscreen with Transparent Taskbar")
    root.attributes('-fullscreen', True)

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Load the background image
    bg_image = tk.PhotoImage(file="background.png")
    
    # Load the transparent taskbar image
    taskbar_image = tk.PhotoImage(file="taskbar_transparent.png")
    
    # Create a canvas to display the background
    canvas = tk.Canvas(
        root, 
        width=screen_width, 
        height=screen_height,
        highlightthickness=0
    )
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # Display the background image
    canvas.create_image(
        screen_width//2,
        screen_height//2,
        image=bg_image
    )

    # Calculate taskbar position
    taskbar_height = 40
    taskbar_y = screen_height - taskbar_height

    # Display the transparent taskbar image
    taskbar_bg = canvas.create_image(
        screen_width//2,  # center horizontally
        screen_height - taskbar_height//2,  # align to bottom
        image=taskbar_image
    )

    # Create a frame for taskbar content with semi-transparent background
    taskbar = tk.Frame(
        canvas, 
        bg='#2b2b2b',  # Dark background
        height=taskbar_height
    )
    
    # Place the taskbar frame
    taskbar_window = canvas.create_window(
        0, 
        taskbar_y, 
        anchor=tk.NW, 
        window=taskbar, 
        width=screen_width,
        height=taskbar_height
    )

    # Frame for programs in the taskbar
    programs_frame = tk.Frame(taskbar, bg='#2b2b2b')  # Match taskbar background
    programs_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

    pinned_programs = ["File Explorer", "Browser", "Notepad"]

    def create_transparent_button(parent, text, command):
        """Create a button with semi-transparent styling"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bd=0,  # no border
            relief='flat',
            bg='#2b2b2b',  # Match taskbar background
            fg='white',  # white text
            activebackground='#3d3d3d',  # slightly lighter on hover
            activeforeground='white',
            highlightthickness=0,
            padx=10,
            pady=5
        )
        return btn

    def update_taskbar():
        for widget in programs_frame.winfo_children():
            widget.destroy()

        for program in pinned_programs:
            create_transparent_button(
                programs_frame,
                program,
                lambda p=program: print(f"{p} clicked")
            ).pack(side=tk.LEFT, padx=5)

        active_program = get_active_window_name()
        if active_program and active_program not in pinned_programs:
            create_transparent_button(
                programs_frame,
                f"* {active_program}",
                lambda: print(f"{active_program} activated")
            ).pack(side=tk.LEFT, padx=5)

    def periodic_update():
        update_taskbar()
        root.after(1000, periodic_update)

    periodic_update()

    # Create exit button
    exit_btn = create_transparent_button(taskbar, "Exit", root.destroy)
    exit_btn.pack(side=tk.RIGHT, padx=10)

    # Store references to prevent garbage collection
    root.bg_image = bg_image
    root.taskbar_image = taskbar_image

    root.mainloop()

if __name__ == "__main__":
    create_taskbar_window()