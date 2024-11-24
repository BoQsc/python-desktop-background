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
            self.hovered_image = tk.PhotoImage(file="taskbar_notransparency.png")
            
            # Get taskbar image dimensions
            taskbar_width = self.taskbar_image.width()
            taskbar_height = self.taskbar_image.height()
            
            # Calculate taskbar position (centered horizontally, exactly at bottom)
            taskbar_x = window_width // 2
            taskbar_y = window_height  # Position exactly at bottom edge
            
            # Add taskbar image at the bottom with no gap
            self.taskbar_image_id = self.canvas.create_image(
                taskbar_x,
                taskbar_y,
                image=self.taskbar_image,
                anchor='s'  # 's' anchor means the bottom center of the image is at the specified position
            )
            
            # Bind window resize event to update taskbar position
            self.root.bind('<Configure>', self.on_window_resize)
            
            # Bind click events to taskbar image
            self.canvas.tag_bind(self.taskbar_image_id, "<Button-1>", self.on_taskbar_image_click)
            self.canvas.tag_bind(self.taskbar_image_id, "<Button-3>", self.on_taskbar_image_right_click)
            
            # Bind hover events for mouse enter and leave
            self.canvas.tag_bind(self.taskbar_image_id, "<Enter>", self.on_taskbar_image_hover)
            self.canvas.tag_bind(self.taskbar_image_id, "<Leave>", self.on_taskbar_image_leave)
            
            # Initialize fade parameters
            self.alpha = 0
            self.fade_speed = 0.05
            
        except tk.TclError as e:
            print(f"Error loading images: {e}")
            error_label = ttk.Label(
                root, 
                text="Error: Could not load image files!\nMake sure both PNG files exist in the correct location."
            )
            error_label.pack(pady=20)
    
    def on_window_resize(self, event):
        """Update taskbar position when window is resized"""
        if hasattr(self, 'taskbar_image'):
            window_width = event.width
            window_height = event.height
            
            # Recalculate taskbar position - exactly at bottom
            taskbar_x = window_width // 2
            taskbar_y = window_height  # Exact bottom position
            
            # Update taskbar position
            self.canvas.coords(self.taskbar_image_id, taskbar_x, taskbar_y)
    
    def on_taskbar_image_click(self, event):
        print("Taskbar image left-clicked!")
        # Additional logic when image is left-clicked can go here
    
    def on_taskbar_image_right_click(self, event):
        print("Taskbar image right-clicked!")
        self.show_right_click_menu(event)
    
    def on_taskbar_image_hover(self, event):
        print("Mouse hovered over taskbar image!")
        self.fade_in()
    
    def on_taskbar_image_leave(self, event):
        print("Mouse left the taskbar image!")
        self.fade_out()

    def fade_in(self):
        if self.alpha < 1:
            self.alpha += self.fade_speed
            self.update_image_opacity()
            self.root.after(30, self.fade_in)

    def fade_out(self):
        if self.alpha > 0:
            self.alpha -= self.fade_speed
            self.update_image_opacity()
            self.root.after(30, self.fade_out)

    def update_image_opacity(self):
        new_image = self.apply_alpha_to_image(self.hovered_image, self.alpha)
        self.canvas.itemconfig(self.taskbar_image_id, image=new_image)

    def apply_alpha_to_image(self, image, alpha):
        return image

    def show_right_click_menu(self, event):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
        menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.quit)
        menu.post(event.x_root, event.y_root)

def main():
    root = tk.Tk()
    app = ImageWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()