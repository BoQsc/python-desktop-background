import ctypes
from ctypes import wintypes

def get_dpi_for_primary_monitor():
    hdc = ctypes.windll.user32.GetDC(0)
    dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # 88 is LOGPIXELSX
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return dpi

print(f"Primary Monitor DPI: {get_dpi_for_primary_monitor()}")

# Tkinter-based check for the primary monitor DPI
import tkinter
root = tkinter.Tk()
dpi = root.winfo_fpixels('1i')
print(f"Tkinter-reported DPI: {dpi}")
root.destroy()
