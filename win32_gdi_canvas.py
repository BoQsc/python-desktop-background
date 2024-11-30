import ctypes
import sys

if sys.platform == 'win32':
    # Win32 code
    user32 = ctypes.windll.user32

    # Define constants
    WM_PAINT = 0x000F
    WM_DESTROY = 0x0002

    # Define window class
    class WNDCLASS(ctypes.Structure):
        _fields_ = [
            ('style', ctypes.c_uint),
            ('lpfnWndProc', ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int)),
            ('cbClsExtra', ctypes.c_int),
            ('cbWndExtra', ctypes.c_int),
            ('hInstance', ctypes.c_int),
            ('hIcon', ctypes.c_int),
            ('hCursor', ctypes.c_int),
            ('hbrBackground', ctypes.c_int),
            ('lpszMenuName', ctypes.c_wchar_p),
            ('lpszClassName', ctypes.c_wchar_p)
        ]

    # Window procedure
    def WndProc(hwnd, msg, wParam, lParam):
        if msg == WM_PAINT:
            hdc, ps = user32.BeginPaint(hwnd, None)
            user32.Rectangle(hdc, 50, 50, 150, 150)
            user32.EndPaint(hwnd, ps)
        elif msg == WM_DESTROY:
            user32.PostQuitMessage(0)
        return user32.DefWindowProcW(hwnd, msg, wParam, lParam)

    # Convert the Python function to a WinFunctionType
    WndProc = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int)(WndProc)

    # Main function
    def main():
        wc = WNDCLASS()
        wc.lpfnWndProc = WndProc
        wc.hInstance = user32.GetModuleHandleW(None)
        wc.lpszClassName = "CanvasClass"

        class_atom = user32.RegisterClassW(ctypes.byref(wc))
        if class_atom == 0:
            raise Exception("RegisterClassW failed")

        hwnd = user32.CreateWindowExW(
            0, class_atom, "Canvas Example",
            0x00000000 | 0x00C00000 | 0x00080000 | 0x00040000 | 0x00020000,
            100, 100, 300, 300,
            None, None, wc.hInstance, None
        )
        if hwnd == 0:
            raise Exception("CreateWindowExW failed")

        user32.ShowWindow(hwnd, 1)
        user32.UpdateWindow(hwnd)

        msg = ctypes.wintypes.MSG()
        while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

    if __name__ == "__main__":
        main()
elif sys.platform == 'linux':
    # Linux code
    xlib = ctypes.cdll.LoadLibrary('libX11.so')

    # Define constants
    ExposureMask = 0x00000002
    BlackPixel = lambda d, s: xlib.BlackPixel(d, s)
    WhitePixel = lambda d, s: xlib.WhitePixel(d, s)
    XEvent = ctypes.c_void_p

    # Main function
    def main():
        dpy = xlib.XOpenDisplay(None)
        if not dpy:
            raise Exception("Cannot open display")

        default_screen = xlib.XDefaultScreen(dpy)
        root = xlib.XRootWindow(dpy, default_screen)

        win = xlib.XCreateSimpleWindow(
            dpy, root, 100, 100, 300, 300, 1,
            WhitePixel(dpy, default_screen),
            BlackPixel(dpy, default_screen)
        )

        xlib.XSelectInput(dpy, win, ExposureMask)
        xlib.XMapWindow(dpy, win)

        while True:
            event = XEvent()
            xlib.XNextEvent(dpy, ctypes.byref(event))
            if event.contents.type == 12:  # Expose event
                gc = xlib.XCreateGC(dpy, win, 0, None)
                xlib.XSetForeground(dpy, gc, WhitePixel(dpy, default_screen))
                xlib.XFillRectangle(dpy, win, gc, 50, 50, 100, 100)
                xlib.XFreeGC(dpy, gc)

    if __name__ == "__main__":
        main()
else:
    print("Unsupported platform")