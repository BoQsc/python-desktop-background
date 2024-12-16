import tkinter as tk

def create_fullscreen_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    
    # Create a canvas
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # DPI correction function
    def dpi_corrected_width(percentage):
        return int(root.winfo_screenwidth() * (percentage / 100))
    
    # Red image
    red_height = 20
    red_width = dpi_corrected_width(80)  # Apply DPI correction
    canvas.create_rectangle(0, 0, red_width, red_height, fill="red", outline="")
    
    # Blue image
    blue_height = 10
    blue_width = int(root.winfo_screenwidth() * 0.8)  # No DPI correction for blue
    canvas.create_rectangle(0, red_height, blue_width, red_height + blue_height, fill="blue", outline="")
    
    root.mainloop()

create_fullscreen_window()
