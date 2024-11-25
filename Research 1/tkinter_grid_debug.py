import tkinter as tk

def show_grid(parent, rows=10, cols=10, cell_size=50):
    """Draw a visible grid on the parent widget for debugging."""
    for row in range(rows):
        for col in range(cols):
            # Create a visible cell using a Label with a border
            label = tk.Label(
                parent, 
                text=f"{row},{col}", 
                borderwidth=1, 
                relief="solid", 
                bg="lightgray"
            )
            label.grid(row=row, column=col, ipadx=cell_size//10, ipady=cell_size//20)

# Main application
root = tk.Tk()
root.geometry("500x500")

# Frame to show grid debugging
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Add grid to the frame
show_grid(frame, rows=8, cols=8, cell_size=50)

root.mainloop()
