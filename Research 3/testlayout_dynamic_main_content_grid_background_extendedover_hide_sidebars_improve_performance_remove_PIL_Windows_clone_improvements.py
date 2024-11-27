import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import datetime

class DesktopIcon:
    def __init__(self, canvas, x, y, name, icon_size=64):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.name = name
        self.icon_size = icon_size
        
        # Create icon rectangle
        self.rect = canvas.create_rectangle(
            x - icon_size // 2, y - icon_size // 2, 
            x + icon_size // 2, y + icon_size // 2, 
            fill="lightblue", outline="black"
        )
        
        # Create icon label
        self.label = canvas.create_text(
            x, y + icon_size // 2 + 10, 
            text=name, font=("Arial", 10)
        )
        
        # Context menu
        self.context_menu = None
        
        # Bind events
        canvas.tag_bind(self.rect, "<Button-1>", self.on_click)
        canvas.tag_bind(self.rect, "<Double-1>", self.on_double_click)
        canvas.tag_bind(self.rect, "<Button-3>", self.show_context_menu)
        
        # Drag and drop
        canvas.tag_bind(self.rect, "<ButtonPress-1>", self.start_drag)
        canvas.tag_bind(self.rect, "<B1-Motion>", self.drag)
        
    def start_drag(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y
        
    def drag(self, event):
        dx = event.x - self._drag_start_x
        dy = event.y - self._drag_start_y
        
        # Move both rectangle and label
        self.canvas.move(self.rect, dx, dy)
        self.canvas.move(self.label, dx, dy)
        
        # Update current position
        self.x += dx
        self.y += dy
        
        # Update drag start
        self._drag_start_x = event.x
        self._drag_start_y = event.y
    
    def on_click(self, event):
        # Implement single click behavior
        pass
    
    def on_double_click(self, event):
        # Open folder or application
        if self.name == "Computer":
            messagebox.showinfo("Computer", "Opening Computer")
        elif self.name == "Recycle Bin":
            messagebox.showinfo("Recycle Bin", "Opening Recycle Bin")
        elif self.name == "Network":
            messagebox.showinfo("Network", "Opening Network")
        elif self.name == "Folder":
            messagebox.showinfo("Folder", "Opening Folder")
    
    def show_context_menu(self, event):
        # Destroy existing context menu if any
        if self.context_menu:
            self.context_menu.destroy()
        
        # Create context menu
        self.context_menu = tk.Menu(self.canvas, tearoff=0)
        self.context_menu.add_command(label="Open", command=self.on_double_click)
        self.context_menu.add_command(label="Rename", command=self.rename)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Properties", command=self.show_properties)
        
        # Display context menu
        self.context_menu.post(event.x_root, event.y_root)
    
    def rename(self):
        new_name = simpledialog.askstring("Rename", f"Rename {self.name}:", 
                                          initialvalue=self.name)
        if new_name:
            self.name = new_name
            self.canvas.itemconfig(self.label, text=new_name)
    
    def show_properties(self):
        messagebox.showinfo("Properties", 
                            f"Name: {self.name}\n"
                            f"Location: Desktop\n"
                            f"Position: ({self.x}, {self.y})")

class StartMenu:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.menu_rect = None
        self.is_open = False
    
    def toggle(self):
        if self.is_open:
            self.close()
        else:
            self.open()
    
    def open(self):
        if not self.is_open:
            self.menu_rect = self.canvas.create_rectangle(
                self.x, self.y - self.height, 
                self.x + self.width, self.y, 
                fill='white', outline='gray'
            )
            # Add start menu items here
            self.canvas.create_text(
                self.x + self.width // 2, 
                self.y - self.height // 2, 
                text="Start Menu", 
                font=("Arial", 12)
            )
            self.is_open = True
    
    def close(self):
        if self.is_open and self.menu_rect:
            self.canvas.delete(self.menu_rect)
            self.is_open = False

class DesktopShell:
    def __init__(self, root):
        self.root = root
        root.title("Windows Shell Simulation")
        
        # Create canvas
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind resize event
        self.canvas.bind("<Configure>", self.on_resize)
        
        # Bind global click to close start menu
        self.canvas.bind("<Button-1>", self.handle_global_click)
        
        # Taskbar details
        self.toolbar_height = 50
        self.start_menu = None
        self.time_label = None
        
        # Icons
        self.desktop_icons = []
        
        # Defer desktop creation until after initial layout
        self.root.after(100, self.create_desktop)
        
        # Start clock update
        self.update_clock()
    
    def handle_global_click(self, event):
        # Close start menu if it's open and click is outside
        if self.start_menu and self.start_menu.is_open:
            start_button_coords = self.canvas.bbox("start_button")
            if not start_button_coords or not self.is_point_in_rect(event.x, event.y, start_button_coords):
                self.start_menu.close()
    
    def is_point_in_rect(self, x, y, rect_coords):
        return (rect_coords[0] <= x <= rect_coords[2] and 
                rect_coords[1] <= y <= rect_coords[3])
    
    def update_clock(self):
        # Update time and date
        current_time = datetime.datetime.now().strftime("%I:%M %p\n%m/%d/%Y")
        if self.time_label:
            self.canvas.delete(self.time_label)
        
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        self.time_label = self.canvas.create_text(
            canvas_width - 50, 
            canvas_height - self.toolbar_height // 2, 
            text=current_time, 
            font=("Arial", 10)
        )
        
        # Schedule next update
        self.root.after(1000, self.update_clock)
    
    def create_desktop(self):
        # Get canvas dimensions
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Prevent division by zero
        if canvas_width <= 0:
            # Retry after a short delay if width is invalid
            self.root.after(100, self.create_desktop)
            return
        
        # Clear previous drawings
        self.canvas.delete("all")
        
        # Load background (with error handling)
        try:
            bg_photo = tk.PhotoImage(file="background.png")
            self.canvas.create_image(0, 0, anchor="nw", image=bg_photo)
            self.canvas.bg_photo = bg_photo  # Keep reference
        except tk.TclError:
            print("Background image not found. Using default.")
        
        # Create main desktop area
        content_height = canvas_height - self.toolbar_height
        self.canvas.create_rectangle(0, 0, canvas_width, content_height, outline="black")
        
        # Create desktop icons
        icon_size = 64
        icon_spacing_x = icon_size + 20  # Horizontal spacing
        icon_spacing_y = icon_size + 40  # Vertical spacing (include label height)
        
        # Calculate max rows based on content height
        max_rows = (content_height - icon_spacing_y) // icon_spacing_y
        
        icons = ["Computer", "Recycle Bin", "Network", "Folder"]
        
        self.desktop_icons = []
        for i, icon_name in enumerate(icons):
            # Calculate column and row
            row = i % max_rows
            col = i // max_rows
            
            # Calculate icon position
            x = col * icon_spacing_x + icon_spacing_x // 2
            y = row * icon_spacing_y + icon_spacing_y // 2
            
            # Create icon
            icon = DesktopIcon(self.canvas, x, y, icon_name)
            self.desktop_icons.append(icon)
        
        # Create taskbar
        self.canvas.create_rectangle(
            0, canvas_height - self.toolbar_height, 
            canvas_width, canvas_height, 
            fill="darkgray", outline="black"
        )
        
        # Start button
        start_button = self.canvas.create_rectangle(
            0, canvas_height - self.toolbar_height, 
            100, canvas_height, 
            fill="green", outline="black",
            tags="start_button"
        )
        start_text = self.canvas.create_text(
            50, canvas_height - self.toolbar_height // 2, 
            text="Start", font=("Arial", 12)
        )
        
        # Create start menu
        self.start_menu = StartMenu(
            self.canvas, 
            0, 
            canvas_height, 
            250, 
            300
        )
        
        # Bind start button click
        self.canvas.tag_bind(start_button, "<Button-1>", lambda e: self.start_menu.toggle())
        self.canvas.tag_bind(start_text, "<Button-1>", lambda e: self.start_menu.toggle())
    
    def on_resize(self, event):
        # Recreate desktop on window resize
        self.create_desktop()

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopShell(root)
    root.mainloop()