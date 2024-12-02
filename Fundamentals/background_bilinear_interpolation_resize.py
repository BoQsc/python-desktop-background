from tkinter import Tk, Canvas, PhotoImage

def bilinear_interpolation_resize(src_image, new_width, new_height):
    original_width = src_image.width()
    original_height = src_image.height()
    new_image = PhotoImage(width=new_width, height=new_height)
    
    for y in range(new_height):
        for x in range(new_width):
            # Map destination pixel to source space
            src_x = (x / new_width) * (original_width - 1)
            src_y = (y / new_height) * (original_height - 1)
            
            x0 = int(src_x)
            y0 = int(src_y)
            x1 = min(x0 + 1, original_width - 1)
            y1 = min(y0 + 1, original_height - 1)
            
            dx = src_x - x0
            dy = src_y - y0
            
            # Retrieve the RGB values from the source image
            c00 = src_image.get(x0, y0)
            c10 = src_image.get(x1, y0)
            c01 = src_image.get(x0, y1)
            c11 = src_image.get(x1, y1)
            
            # Perform bilinear interpolation
            interpolated_color = tuple(
                int(
                    c00[i] * (1 - dx) * (1 - dy) +
                    c10[i] * dx * (1 - dy) +
                    c01[i] * (1 - dx) * dy +
                    c11[i] * dx * dy
                )
                for i in range(3)
            )
            
            # Set the pixel on the new image
            new_image.put('#{:02x}{:02x}{:02x}'.format(*interpolated_color), (x, y))
    
    return new_image

# Example usage
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

# Load "background.png" and resize it
original_image = PhotoImage(file="background.png")  # Ensure background.png is in the same directory
resized_image = bilinear_interpolation_resize(original_image, 300, 300)

# Display resized image
canvas.create_image(0, 0, anchor='nw', image=resized_image)
root.mainloop()
