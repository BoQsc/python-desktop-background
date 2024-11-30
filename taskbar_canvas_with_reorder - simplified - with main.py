import tkinter as tk
from PIL import Image, ImageTk

def on_click(event):
    global dragging, offset_x
    for i, rect in enumerate(rectangles):
        x1, y1, x2, y2 = canvas.bbox(rect)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            dragging = i
            offset_x = event.x - x1
            break

def on_drag(event):
    if dragging is not None:
        rect = rectangles[dragging]
        canvas.coords(rect, event.x - offset_x, 0, event.x - offset_x + rect_width, rect_height)
        canvas.tag_raise(rect)

def on_release(event):
    global dragging
    if dragging is not None:
        new_pos = (event.x - offset_x + rect_width // 2) // rect_width
        new_pos = max(0, min(new_pos, num_items - 1))
        if new_pos != dragging:
            rect = rectangles.pop(dragging)
            rectangles.insert(new_pos, rect)
        for i, rect in enumerate(rectangles):
            canvas.coords(rect, i * rect_width, 0, (i + 1) * rect_width, rect_height)
        dragging = None

def main():
    global root, canvas, rectangles, num_items, rect_width, rect_height, dragging, offset_x

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

    rectangles = [canvas.create_rectangle(i * rect_width, 0, (i + 1) * rect_width, rect_height,
                                          fill=colors[i % len(colors)], outline="black") for i in range(num_items)]

    dragging, offset_x = None, 0
    canvas.bind("<ButtonPress-1>", on_click)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)

    root.mainloop()

if __name__ == "__main__":
    main()
