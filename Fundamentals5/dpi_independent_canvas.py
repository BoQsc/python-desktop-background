
import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window, bg="gray", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

scaling_factor = window.tk.call('tk', 'scaling')
canvas.scale("all", 0, 0, scaling_factor, scaling_factor)

window.mainloop()