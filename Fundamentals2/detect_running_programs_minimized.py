import psutil
import win32gui
import win32process

def is_window_minimized(hwnd):
    # Check if the window is minimized (iconic)
    return win32gui.IsIconic(hwnd)

def enum_windows_proc(hwnd, lparam):
    global running_windows
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == lparam:
        if win32gui.IsWindowVisible(hwnd):
            state = 'minimized' if is_window_minimized(hwnd) else 'normal'
            process_name = psutil.Process(pid).name() if psutil.pid_exists(pid) else "Unknown"
            running_windows.append((process_name, state))

def get_running_windows():
    global running_windows
    running_windows = []
    for process in psutil.process_iter(['pid', 'name']):
        try:
            win32gui.EnumWindows(enum_windows_proc, process.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_windows

print(get_running_windows())
