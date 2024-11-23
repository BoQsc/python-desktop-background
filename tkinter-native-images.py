import tkinter as tk
from tkinter import ttk

class ImageWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Window")
        
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Set window size
        window_width = 800
        window_height = 600
        
        # Calculate center position
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        
        # Set window size and position
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        
        try:
            # Create and load background image
            self.bg_image = tk.PhotoImage(file="background.png")
            
            # Create canvas for background
            self.canvas = tk.Canvas(
                root, 
                width=window_width, 
                height=window_height,
                highlightthickness=0
            )
            self.canvas.pack(fill='both', expand=True)
            
            # Set background image
            # We'll scale the image to fit the window
            self.canvas.create_image(
                window_width//2,  # center x
                window_height//2, # center y
                image=self.bg_image
            )
            
            # Load taskbar image
            self.taskbar_image = tk.PhotoImage(file="taskbar_transparent.png")
            
            # Add taskbar image to center
            self.canvas.create_image(
                window_width//2,  # center x
                window_height//2, # center y
                image=self.taskbar_image
            )
            
        except tk.TclError as e:
            print(f"Error loading images: {e}")
            error_label = ttk.Label(
                root, 
                text="Error: Could not load image files!\nMake sure both PNG files exist in the correct location."
            )
            error_label.pack(pady=20)

def main():
    root = tk.Tk()
    app = ImageWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
