import ctypes
import tkinter as tk
from tkinter import ttk
import winreg as reg

# Load necessary Windows libraries
dsound_dll = ctypes.windll.LoadLibrary("dsound.dll")
ole32_dll = ctypes.oledll.ole32

# Define necessary Windows types
LPDSENUMCALLBACK = ctypes.WINFUNCTYPE(ctypes.c_bool,
                                      ctypes.c_void_p,
                                      ctypes.c_wchar_p,
                                      ctypes.c_wchar_p,
                                      ctypes.c_void_p)

def get_devices():
    devices = []

    def cb_enum(lpGUID, lpszDesc, lpszDrvName, _unused):
        dev = ""
        if lpGUID is not None:
            buf = ctypes.create_unicode_buffer(500)
            if ole32_dll.StringFromGUID2(ctypes.c_int64(lpGUID), ctypes.byref(buf), 0):
                dev = buf.value
        
        devices.append((lpGUID, lpszDesc, lpszDrvName))
        return True

    # Enumerate output devices
    dsound_dll.DirectSoundEnumerateW(LPDSENUMCALLBACK(cb_enum), None)  # Output devices
    
    return devices

def set_default_output_device(guid):
    key = reg.HKEY_CURRENT_USER
    subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Audio\Devices"

    try:
        with reg.OpenKey(key, subkey, 0, reg.KEY_WRITE) as key_handle:
            reg.SetValueEx(key_handle, "DefaultDevice", 0, reg.REG_SZ, guid)
    except FileNotFoundError:
        print(f"Could not set default output device with GUID {guid}")

def select_output_device():
    devices = get_devices()
    device_list = [(desc, guid) for guid, desc, _ in devices]
    
    root = tk.Tk()
    root.title("Select Output Device")

    var = tk.StringVar()
    ttk.Label(root, text="Select Output Device:").pack(pady=5)
    device_selector = ttk.Combobox(root, textvariable=var, values=[desc for desc, _ in device_list])
    device_selector.pack(pady=5)
    device_selector.set(device_list[0][0])  # Set default value

    def on_select(event):
        selected_device = var.get()
        guid = next(guid for desc, guid in device_list if desc == selected_device)
        print(f"Selected Output Device GUID: {guid}")
        set_default_output_device(guid)

    device_selector.bind("<<ComboboxSelected>>", on_select)

    root.mainloop()

if __name__ == '__main__':
    select_output_device()
