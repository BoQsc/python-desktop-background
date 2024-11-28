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
            
            # Initialize fade parameters
            self.alpha = 0  # Transparency (0 means fully transparent, 1 means fully opaque)
            self.fade_speed = 0.05  # Speed of fade in and out
            
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
        # Start fade-in effect
        self.fade_in()
    
    def on_taskbar_image_leave(self, event):
        print("Mouse left the taskbar image!")
        # Start fade-out effect
        self.fade_out()

    def fade_in(self):
        if self.alpha < 1:  # Check if alpha is less than 1 (fully opaque)
            self.alpha += self.fade_speed
            self.update_image_opacity()
            self.root.after(30, self.fade_in)  # Continue fading in by calling this method repeatedly

    def fade_out(self):
        if self.alpha > 0:  # Check if alpha is greater than 0 (fully transparent)
            self.alpha -= self.fade_speed
            self.update_image_opacity()
            self.root.after(30, self.fade_out)  # Continue fading out by calling this method repeatedly

    def update_image_opacity(self):
        # Apply the new opacity to the hover image by manipulating its alpha
        new_image = self.apply_alpha_to_image(self.hovered_image, self.alpha)
        self.canvas.itemconfig(self.taskbar_image_id, image=new_image)

    def apply_alpha_to_image(self, image, alpha):
        # This method is a placeholder where you would implement the logic to apply alpha transparency to the image.
        # Tkinter itself doesn't directly support alpha channels, so you would typically use a third-party library for image manipulation.
        # For simplicity, we're assuming you can generate an image with varying opacity here.
        return image  # Placeholder, no actual alpha manipulation in Tkinter

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
