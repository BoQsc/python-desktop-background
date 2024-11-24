import tkinter as tk

def countdown(count):
    # Update the text with the current count value
    canvas.itemconfig(text_id, text=f"{count:02}")
    if count > 0:
        # Call countdown again after 1 second
        root.after(1000, countdown, count - 1)

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300, highlightthickness=0)
canvas.pack()

# Background image
img = tk.PhotoImage(file="background.png")
canvas.create_image(200, 150, image=img)  # Adjusted to center the image

# Draw text
text_id = canvas.create_text(320, 261, text="100", font="calibri 40 bold", fill="white")

# Start the countdown
countdown(100)

root.mainloop()
