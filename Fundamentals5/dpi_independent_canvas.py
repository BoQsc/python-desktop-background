
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, bg="gray", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

scaling_factor = root.tk.call('tk', 'scaling')
canvas.scale("all", 0, 0, scaling_factor, scaling_factor)

root.mainloop()