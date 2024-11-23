import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class ImageWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Window")
        
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Set window size (you can adjust these values)
        window_width = 800
        window_height = 600
        
        # Calculate center position
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        
        # Set window size and position
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)
        
        try:
            # Load background image
            bg_image = Image.open("background.png")
            # Resize background image to window size
            bg_image = bg_image.resize((window_width, window_height), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            
            # Create canvas for background
            self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height)
            self.canvas.pack(fill='both', expand=True)
            
            # Set background image
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
            
            # Load taskbar image
            taskbar_image = Image.open("taskbar_transparent.png")
            # You can adjust the size of the taskbar image if needed
            taskbar_width = 400  # Example size
            taskbar_height = 60  # Example size
            taskbar_image = taskbar_image.resize((taskbar_width, taskbar_height), Image.Resampling.LANCZOS)
            self.taskbar_photo = ImageTk.PhotoImage(taskbar_image)
            
            # Calculate center position for taskbar
            taskbar_x = (window_width - taskbar_width) // 2
            taskbar_y = (window_height - taskbar_height) // 2
            
            # Add taskbar image to center
            self.canvas.create_image(taskbar_x, taskbar_y, image=self.taskbar_photo, anchor='nw')
            
        except FileNotFoundError as e:
            print(f"Error: Could not find image file - {e}")
            error_label = ttk.Label(self.main_frame, text="Error: Image files not found!")
            error_label.pack(pady=20)

def main():
    root = tk.Tk()
    app = ImageWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()