import ctypes

# Function to shutdown the system
def shutdown():
    user32 = ctypes.windll.user32
    user32.ExitWindowsEx(4, 0)  # 1 for EWX_SHUTDOWN flag

# Call the shutdown function
shutdown()