import tkinter as tk
from PIL import Image, ImageTk
import win32gui
import win32process
import psutil


def get_active_window_name():
    """Get the name of the active window."""
    hwnd = win32gui.GetForegroundWindow()  # Handle to the active window
    _, pid = win32process.GetWindowThreadProcessId(hwnd)  # Get PID of the process owning the window
    try:
        process = psutil.Process(pid)
        return process.name()
    except psutil.Error:
        return "Unknown"


def create_taskbar_window():
    root = tk.Tk()
    root.title("Fullscreen with Taskbar")
    root.attributes('-fullscreen', True)

    # Load the background image
    image = Image.open("background.jfif")
    bg_image = ImageTk.PhotoImage(image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))

    # Create a canvas to display the background
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

    # Create the taskbar at the bottom
    taskbar = tk.Frame(root, bg="gray", height=40)
    canvas.create_window(0, root.winfo_screenheight() - 40, anchor=tk.NW, window=taskbar, height=40, width=root.winfo_screenwidth())

    # Frame for programs in the taskbar
    programs_frame = tk.Frame(taskbar, bg="gray")
    programs_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

    pinned_programs = ["File Explorer", "Browser", "Notepad"]  # Example pinned programs

    def update_taskbar():
        for widget in programs_frame.winfo_children():
            widget.destroy()

        for program in pinned_programs:
            tk.Button(programs_frame, text=program, command=lambda p=program: print(f"{p} clicked")).pack(side=tk.LEFT, padx=5)

        active_program = get_active_window_name()
        if active_program and active_program not in pinned_programs:
            tk.Button(programs_frame, text=f"* {active_program}", command=lambda: print(f"{active_program} activated")).pack(side=tk.LEFT, padx=5)

    def periodic_update():
        update_taskbar()
        root.after(1000, periodic_update)

    periodic_update()

    tk.Button(taskbar, text="Exit", command=root.destroy).pack(side=tk.RIGHT, padx=10)

    root.mainloop()


create_taskbar_window()
