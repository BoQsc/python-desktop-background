import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

class Taskbar(tk.Frame):
    def __init__(self, master, image_path, num_buttons=6, **kwargs):
        super().__init__(master, **kwargs)
        self.canvas = Canvas(self, width=600, height=100)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Load the image using PIL
        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((600, 100), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Display the background image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        
        # Create rectangles (buttons)
        self.rects = []
        self.rect_width = 80
        self.rect_height = 60
        self.spacing = 10  # Space between rectangles
        
        for i in range(num_buttons):
            x1 = i * (self.rect_width + self.spacing)
            y1 = 20
            x2 = x1 + self.rect_width
            y2 = y1 + self.rect_height
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="black", tags="rect")
            self.canvas.tag_bind(rect, "<Button-1>", self.on_click)
            self.canvas.tag_bind(rect, "<B1-Motion>", self.on_drag)
            self.canvas.tag_bind(rect, "<ButtonRelease-1>", self.on_release)
            self.rects.append(rect)
        
        self.drag_data = {"item": None, "x": 0, "y": 0}

    def on_click(self, event):
        # Identify which rectangle is clicked
        for rect in self.rects:
            if self.canvas.tag_cget(rect, "tags") == "rect":
                x1, y1, x2, y2 = self.canvas.coords(rect)
                if x1 < event.x < x2 and y1 < event.y < y2:
                    self.drag_data["item"] = rect
                    self.drag_data["x"] = event.x
                    self.drag_data["y"] = event.y

    def on_drag(self, event):
        if self.drag_data["item"]:
            # Move the rectangle as the mouse moves
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            self.canvas.move(self.drag_data["item"], dx, 0)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_release(self, event):
        # Reset the drag data
        self.drag_data["item"] = None

# Example usage
root = tk.Tk()
root.title("Taskbar Widget Example")

taskbar = Taskbar(root, image_path="taskbar.png", num_buttons=6)
taskbar.pack(fill=tk.X)

root.mainloop()
