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
            self.canvas.create_image(
                window_width//2,  # center x
                window_height//2, # center y
                image=self.bg_image
            )
            
            # Load taskbar image
            self.taskbar_image = tk.PhotoImage(file="taskbar_transparent.png")
            self.hovered_image = tk.PhotoImage(file="taskbar_notransparency.png")  # Assuming you have a different image for hover
            
            # Add taskbar image to center and bind click and hover events
            self.taskbar_image_id = self.canvas.create_image(
                window_width//2,  # center x
                window_height//2, # center y
                image=self.taskbar_image
            )
            
            # Bind click events to taskbar image
            self.canvas.tag_bind(self.taskbar_image_id, "<Button-1>", self.on_taskbar_image_click)  # Left-click
            self.canvas.tag_bind(self.taskbar_image_id, "<Button-3>", self.on_taskbar_image_right_click)  # Right-click
            
            # Bind hover events for mouse enter and leave
            self.canvas.tag_bind(self.taskbar_image_id, "<Enter>", self.on_taskbar_image_hover)
            self.canvas.tag_bind(self.taskbar_image_id, "<Leave>", self.on_taskbar_image_leave)
            
        except tk.TclError as e:
            print(f"Error loading images: {e}")
            error_label = ttk.Label(
                root, 
                text="Error: Could not load image files!\nMake sure both PNG files exist in the correct location."
            )
            error_label.pack(pady=20)
    
    def on_taskbar_image_click(self, event):
        print("Taskbar image left-clicked!")
        # Additional logic when image is left-clicked can go here
    
    def on_taskbar_image_right_click(self, event):
        print("Taskbar image right-clicked!")
        # Additional logic for right-click can go here, like showing a menu or performing an action
        self.show_right_click_menu(event)
    
    def on_taskbar_image_hover(self, event):
        print("Mouse hovered over taskbar image!")
        # Change the image to the hovered version
        self.canvas.itemconfig(self.taskbar_image_id, image=self.hovered_image)
    
    def on_taskbar_image_leave(self, event):
        print("Mouse left the taskbar image!")
        # Revert the image back to the original
        self.canvas.itemconfig(self.taskbar_image_id, image=self.taskbar_image)

    def show_right_click_menu(self, event):
        # Example right-click menu that appears at the mouse position
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
        menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.quit)
        
        # Position the menu at the mouse click location
        menu.post(event.x_root, event.y_root)

def main():
    root = tk.Tk()
    app = ImageWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
