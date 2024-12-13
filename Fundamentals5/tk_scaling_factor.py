import tkinter as tk

root = tk.Tk()

# Get the DPI scaling factor
scaling_factor = root.tk.call('tk', 'scaling')
print(scaling_factor)
# Optionally set your own scaling factor
root.tk.call('tk', 'scaling', scaling_factor)

root.mainloop()
