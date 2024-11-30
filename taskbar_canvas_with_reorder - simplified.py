import tkinter as tk
from PIL import Image, ImageTk

def on_click(event):
    global dragging, offset_x
    print(f"Click event at ({event.x}, {event.y})")
    dragging = None
    for i, rect in enumerate(rectangles):
        if canvas.bbox(rect)[0] <= event.x <= canvas.bbox(rect)[2] and \
           canvas.bbox(rect)[1] <= event.y <= canvas.bbox(rect)[3]:
            dragging = i
            offset_x = event.x - canvas.bbox(rect)[0]
            print(f"Rectangle {i} clicked, starting drag.")
            break
    if dragging is None:
        print("No rectangle clicked.")

def on_drag(event):
    if dragging is not None:
        print(f"Dragging rectangle {dragging} to ({event.x}, {event.y})")
        rect = rectangles[dragging]
        canvas.coords(rect, event.x - offset_x, 0,
                      event.x - offset_x + rect_width, rect_height)
        canvas.tag_raise(rect)

def on_release(event):
    global dragging
    if dragging is not None:
        new_pos = (event.x - offset_x + rect_width // 2) // rect_width
        new_pos = max(0, min(new_pos, num_items - 1))

        print(f"Release event at ({event.x}, {event.y}), calculated new position: {new_pos}")

        original_pos = dragging

        if new_pos == original_pos:
            print(f"Rectangle {dragging} is in the same position, snapping back")
            canvas.coords(rectangles[dragging],
                          dragging * rect_width, 0,
                          (dragging + 1) * rect_width, rect_height)
        else:
            print(f"Moving rectangle {dragging} to position {new_pos}")
            rectangles.insert(new_pos, rectangles.pop(dragging))
            for i, rect in enumerate(rectangles):
                canvas.coords(rect, i * rect_width, 0,
                              (i + 1) * rect_width, rect_height)
                print(f"Rectangle {i} moved to position {i * rect_width}")

        dragging = None

root = tk.Tk()
root.title("Custom Taskbar Widget")

canvas = tk.Canvas(root, width=800, height=100)
canvas.pack()

bg_image = Image.open("taskbar.png").resize((800, 100))
bg_image_tk = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_image_tk, anchor=tk.NW)

num_items = 6
rect_width = 800 // num_items
rect_height = 100
colors = ["lightblue", "lightgreen", "lightcoral", "lightgoldenrodyellow", "lightpink", "lightcyan"]

rectangles = []
for i in range(num_items):
    rect_color = colors[i % len(colors)]
    rect = canvas.create_rectangle(
        i * rect_width, 0,
        (i + 1) * rect_width, rect_height,
        fill=rect_color, outline="black"
    )
    rectangles.append(rect)
    print(f"Rectangle {i}: {rect} created at position {i * rect_width}")

dragging = None
offset_x = 0

canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

root.mainloop()
