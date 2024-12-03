import tkinter as tk
from PIL import Image, ImageTk
from collections import OrderedDict

class SmoothBackground:
    def __init__(self, root, image_path, cache_limit=10):
        self.root = root
        self.canvas = tk.Canvas(root, width=900, height=900)
        self.canvas.pack(fill="both", expand=True)

        # Load the original high-quality image
        self.original_image = Image.open(image_path)
        self.original_width = self.original_image.width
        self.original_height = self.original_image.height

        # Cache for resized images with a limit to reduce memory usage
        self.image_cache = OrderedDict()
        self.cache_limit = cache_limit  # Maximum number of cached images
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
        scale = max(width_scale, height_scale)

        # Calculate new dimensions
        new_width = int(self.original_width * scale)
        new_height = int(self.original_height * scale)

        # Check if the resized image is already in cache
        cache_key = (new_width, new_height)
        if cache_key not in self.image_cache:
            # High-quality resize with LANCZOS filter
            resized_image = self.original_image.resize(
                (new_width, new_height), 
                Image.LANCZOS
            )
            
            # Convert to PhotoImage for tkinter
            photo_image = ImageTk.PhotoImage(resized_image)

            # Store in cache and maintain cache size
            self.image_cache[cache_key] = photo_image
            if len(self.image_cache) > self.cache_limit:
                self.image_cache.popitem(last=False)  # Remove the oldest item

        # Get the image from the cache
        self.current_photo = self.image_cache[cache_key]

        # Clear previous image and add the new one centered
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

# Initialize smooth background with a cache limit
SmoothBackground(root, "background.png", cache_limit=10)

# Start the application
root.mainloop()
