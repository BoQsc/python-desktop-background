import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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
            
            # Load taskbar image and create hover image
            self.taskbar_image = Image.open("taskbar_transparent.png")
            self.hovered_image = Image.open("taskbar_notransparency.png")
            
            # Convert images to PhotoImage objects
            self.taskbar_image_tk = ImageTk.PhotoImage(self.taskbar_image)
            self.hovered_image_tk = ImageTk.PhotoImage(self.hovered_image)
            
            # Add taskbar image to center and bind click and hover events
            self.taskbar_image_id = self.canvas.create_image(
                window_width//2,  # center x
                window_height//2, # center y
                image=self.taskbar_image_tk
            )
            
            # Bind click events to taskbar image
            self.canvas.tag_bind(self.taskbar_image_id, "<Button-1>", self.on_taskbar_image_click)  # Left-click
            self.canvas.tag_bind(self.taskbar_image_id, "<Button-3>", self.on_taskbar_image_right_click)  # Right-click
            
            # Bind hover events for mouse enter and leave
            self.canvas.tag_bind(self.taskbar_image_id, "<Enter>", self.on_taskbar_image_hover)
            self.canvas.tag_bind(self.taskbar_image_id, "<Leave>", self.on_taskbar_image_leave)
            
            # Initialize fade parameters
            self.fade_in = False
            self.fade_out = False
            self.alpha = 0

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
        self.fade_in = True
        self.fade_out = False
        self.alpha = 0  # Reset alpha to 0 for fade-in
        self.animate_fade()

    def on_taskbar_image_leave(self, event):
        print("Mouse left the taskbar image!")
        # Start fade-out effect
        self.fade_out = True
        self.fade_in = False
        self.alpha = 255  # Reset alpha to 255 for fade-out
        self.animate_fade()

    def animate_fade(self):
        if self.fade_in and self.alpha < 255:
            self.alpha += 5  # Increase alpha value for fade-in
        elif self.fade_out and self.alpha > 0:
            self.alpha -= 5  # Decrease alpha value for fade-out
        
        # Update image opacity using the alpha value
        self.update_image_opacity()
        
        # Continue the animation
        if self.fade_in and self.alpha < 255 or self.fade_out and self.alpha > 0:
            self.root.after(50, self.animate_fade)

    def update_image_opacity(self):
        # Create a new image with the adjusted alpha channel
        image = self.hovered_image if self.fade_in else self.taskbar_image
        image = image.convert("RGBA")
        
        # Modify the alpha channel of the image
        new_data = []
        for item in image.getdata():
            # Change the alpha value based on self.alpha
            new_data.append(item[:3] + (self.alpha,))
        
        image.putdata(new_data)
        
        # Convert back to PhotoImage and update canvas
        image_tk = ImageTk.PhotoImage(image)
        self.canvas.itemconfig(self.taskbar_image_id, image=image_tk)
        
        # Keep a reference to avoid garbage collection
        self.canvas.image = image_tk

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
