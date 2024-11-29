import tkinter as tk
from PIL import Image, ImageTk

class Taskbar(tk.Canvas):
    def __init__(self, master, image_path, num_items=6, **kwargs):
        super().__init__(master, **kwargs)

        # Load taskbar background image using PIL
        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((800, 100))  # Resize as needed
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

        # Display the image as the background
        self.create_image(0, 0, image=self.bg_image_tk, anchor=tk.NW)

        self.num_items = num_items
        self.rect_width = 800 // num_items  # Width of each rectangle
        self.rect_height = 100  # Height of rectangles
        self.rectangles = []  # Store rectangle IDs

        # Define a list of colors for the rectangles
        self.colors = ["lightblue", "lightgreen", "lightcoral", "lightgoldenrodyellow", "lightpink", "lightcyan", "lavender", "lightgray", "lightseagreen"]

        # Create rectangles (taskbar items) with different colors
        for i in range(self.num_items):
            rect_color = self.colors[i % len(self.colors)]  # Cycle through colors
            rect = self.create_rectangle(
                i * self.rect_width, 0,
                (i + 1) * self.rect_width, self.rect_height,
                fill=rect_color, outline="black"
            )
            self.rectangles.append(rect)
            print(f"Rectangle {i}: {rect} created at position {i * self.rect_width}")

        self.bind("<ButtonPress-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

        self.dragging = None
        self.offset_x = 0

    def on_click(self, event):
        print(f"Click event at ({event.x}, {event.y})")
        # Check if the click is inside any rectangle
        for i, rect in enumerate(self.rectangles):
            if self.bbox(rect)[0] <= event.x <= self.bbox(rect)[2] and \
               self.bbox(rect)[1] <= event.y <= self.bbox(rect)[3]:
                self.dragging = i
                self.offset_x = event.x - self.bbox(rect)[0]  # Offset for drag
                print(f"Rectangle {i} clicked, starting drag.")
                break
        if self.dragging is None:
            print("No rectangle clicked.")

    def on_drag(self, event):
        if self.dragging is not None:
            print(f"Dragging rectangle {self.dragging} to ({event.x}, {event.y})")
            rect = self.rectangles[self.dragging]
            # Move the rectangle horizontally with the mouse
            self.coords(rect, event.x - self.offset_x, 0,
                        event.x - self.offset_x + self.rect_width, self.rect_height)

    def on_release(self, event):
        if self.dragging is not None:
            # Calculate the new position based on the x-coordinate
            new_pos = (event.x - self.offset_x + self.rect_width // 2) // self.rect_width
            # Clamp new position to be within bounds
            if new_pos < 0:
                new_pos = 0
            elif new_pos >= self.num_items:
                new_pos = self.num_items - 1

            print(f"Release event at ({event.x}, {event.y}), calculated new position: {new_pos}")

            # Get the original position of the dragged rectangle
            original_pos = self.dragging

            # Check if the new position is the same as the original, snap back if true
            if new_pos == original_pos:
                print(f"Rectangle {self.dragging} is in the same position, snapping back")
                self.coords(self.rectangles[self.dragging],
                            self.dragging * self.rect_width, 0,
                            (self.dragging + 1) * self.rect_width, self.rect_height)
            else:
                # Move the rectangle to the new position if it's different
                if new_pos != original_pos:
                    print(f"Moving rectangle {self.dragging} to position {new_pos}")
                    # Move the rectangle to the new position
                    self.rectangles.insert(new_pos, self.rectangles.pop(self.dragging))
                    
                    # Update the rectangle positions
                    for i, rect in enumerate(self.rectangles):
                        self.coords(rect, i * self.rect_width, 0,
                                    (i + 1) * self.rect_width, self.rect_height)
                        print(f"Rectangle {i} moved to position {i * self.rect_width}")

            self.dragging = None  # Reset dragging state

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Taskbar Widget")

    taskbar = Taskbar(root, "taskbar.png", num_items=6, width=800, height=100)
    taskbar.pack()

    root.mainloop()
