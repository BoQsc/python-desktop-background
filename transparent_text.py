import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300, highlightthickness=0)
canvas.pack()

# background image
img = tk.PhotoImage(file="background.png")
canvas.create_image(400, 300, image=img)

# draw text
canvas.create_text(320, 261, text="00", font="calibri 40 bold", fill="white")

root.mainloop()