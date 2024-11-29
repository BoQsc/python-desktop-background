import tkinter as tk
from PIL import Image, ImageTk
import io

class SmoothBackground:
    def __init__(self, root, image_path):
        self.root = root
        self.canvas = tk.Canvas(root, width=900, height=900)
        self.canvas.pack(fill="both", expand=True)

        # Load original high-quality image
        self.original_image = Image.open(image_path)
        self.original_width = self.original_image.width
        self.original_height = self.original_image.height

        # Cache for resized images to improve performance
        self.image_cache = {}
        self.last_resize_width = 0
        self.last_resize_height = 0

        # Store the current PhotoImage to prevent garbage collection
        self.current_photo = None

        # Bind resize event with optimized handler
        self.root.bind("<Configure>", self.on_resize)

        # Initial display
        self.display_image(self.root.winfo_width(), self.root.winfo_height())

    def on_resize(self, event):
        # Debounce resize events
        if (abs(event.width - self.last_resize_width) > 10 or 
            abs(event.height - self.last_resize_height) > 10):
            self.display_image(event.width, event.height)

    def display_image(self, width, height):
        # Calculate scale factors
        width_scale = width / self.original_width
        height_scale = height / self.original_height

        # Choose the larger scale to ensure full window coverage
        scale = max(width_scale, height_scale)

        # Calculate new dimensions
        new_width = int(self.original_width * scale)
        new_height = int(self.original_height * scale)

        # Check cache first
        cache_key = (new_width, new_height)
        if cache_key not in self.image_cache:
            # High-quality resize
            resized_image = self.original_image.copy()
            resized_image = resized_image.resize(
                (new_width, new_height), 
                Image.LANCZOS  # Highest quality resampling
            )
            
            # Convert to PhotoImage
            self.image_cache[cache_key] = ImageTk.PhotoImage(resized_image)

        # Get image from cache
        self.current_photo = self.image_cache[cache_key]

        # Clear previous image and add new one
        self.canvas.delete("all")
        self.canvas.create_image(
            width // 2, height // 2,  # Center the image
            image=self.current_photo, 
            anchor='center'
        )

        # Update last resize dimensions
        self.last_resize_width = width
        self.last_resize_height = height

# Create main window
root = tk.Tk()
root.geometry("800x600")
root.title("Smooth Background Scaling")

# Initialize smooth background
SmoothBackground(root, "background.png")

# Start the application
root.mainloop()