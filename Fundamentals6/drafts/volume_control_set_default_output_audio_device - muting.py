import ctypes

# Constants
WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_MUTE = 0x80000

# Getting the handle of the window
hwnd = ctypes.windll.user32.GetForegroundWindow()

# Sending the message
ctypes.windll.user32.SendMessageW(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_MUTE)
