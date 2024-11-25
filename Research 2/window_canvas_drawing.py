import tkinter

# Create the main application window
window = tkinter.Tk()

# Create and configure the canvas
canvas = tkinter.Canvas(window, width=400, height=300)
canvas.pack(fill=tkinter.BOTH, expand=True)

# Load the image
background_image = tkinter.PhotoImage(file="background.png")

# Add the image to the canvas
canvas.create_image(0, 0, anchor=tkinter.NW, image=background_image)

# Draw other shapes or text on top of the background
canvas.create_line(50, 50, 150, 50, fill="red", width=3)
canvas.create_rectangle(50, 100, 150, 200, fill="blue")
canvas.create_oval(200, 100, 300, 200, fill="green")
canvas.create_text(200, 250, text="Hello, Canvas!", font=("Arial", 16), fill="white")

# Start the event loop
window.mainloop()
