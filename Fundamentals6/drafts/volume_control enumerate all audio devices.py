import ctypes

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
        
        devices.append((dev, lpszDesc, lpszDrvName))
        return True

    # Enumerate both input and output devices
    dsound_dll.DirectSoundCaptureEnumerateW(LPDSENUMCALLBACK(cb_enum), None)  # Input devices
    dsound_dll.DirectSoundEnumerateW(LPDSENUMCALLBACK(cb_enum), None)          # Output devices
    
    return devices

if __name__ == '__main__':
    for devid, desc, name in get_devices():
        print(f'{devid}: {desc} | {name}')
