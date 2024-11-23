from tkinter import Tk, Label, PhotoImage

# Initialize Tkinter
root = Tk()

# Load a transparent PNG
image = PhotoImage(file="a.png")

# Display the image in a label
label = Label(root, image=image)
label.pack()

# Run the Tkinter event loop
root.mainloop()