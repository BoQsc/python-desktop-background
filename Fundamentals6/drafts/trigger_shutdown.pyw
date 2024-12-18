import ctypes

# Function to shutdown the system
def shutdown():
    user32 = ctypes.windll.user32
    user32.ExitWindowsEx(0, 0)  # 1 for shutdown, 0 for no flags

# Call the shutdown function
shutdown()
