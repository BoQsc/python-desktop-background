from tkinter import Tk, Canvas, PhotoImage, NW
from PIL import Image, ImageTk, ImageOps

class ScalableBackground:
    def __init__(self, root, image_path):
        self.root = root
        
        # Create canvas
        self.canvas = Canvas(root, width=400, height=400)
        self.canvas.pack(fill="both", expand=True)

        # Load high-quality image
        self.load_image(image_path)

        # Bind resizing event
        root.bind("<Configure>", self.resize_image)

    def load_image(self, image_path):
        # Open image with high color depth and quality preservation
        self.pil_image = Image.open(image_path)
        
        # Convert to RGB to ensure consistent color handling
        #self.pil_image = self.pil_image.convert('RGB')
        
        # Store original dimensions
        self.original_width = self.pil_image.width
        self.original_height = self.pil_image.height

        # Initial image display
        self.display_image(self.pil_image)

    def display_image(self, image_to_display):
        # Convert to PhotoImage
        self.photo_image = ImageTk.PhotoImage(image_to_display)
        
        # Create or update image on canvas
        if not hasattr(self, 'image_id'):
            self.image_id = self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)
        else:
            self.canvas.itemconfig(self.image_id, image=self.photo_image)

    def resize_image(self, event):
        # Calculate scale factors
        width_scale = event.width / self.original_width
        height_scale = event.height / self.original_height

        # Choose the larger scale to ensure full window coverage
        scale = max(width_scale, height_scale)

        # Calculate the new image size
        new_img_width = int(self.original_width * scale)
        new_img_height = int(self.original_height * scale)

        # Resize with highest quality settings
        resized_image = self.pil_image.resize(
            (new_img_width, new_img_height), 
            Image.LANCZOS  # Best quality resampling
        )

        # Center the image if it's larger than the window
        x = (event.width - new_img_width) // 2
        y = (event.height - new_img_height) // 2

        # Display the resized image
        self.display_image(resized_image)
        self.canvas.coords(self.image_id, x, y)

# Create window
root = Tk()
root.geometry("800x600")
root.title("High-Quality Background Image")

# Initialize the scalable background
ScalableBackground(root, "background.png")

root.mainloop()