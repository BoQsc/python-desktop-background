import ctypes
import tkinter as tk
from tkinter import ttk

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
    dsound_dll.DirectSoundEnumerateW(LPDSENUMCALLBACK(cb_enum), None)  # Output devices
    
    return devices

def set_audio_device(device_name):
    import subprocess

    # Use PowerShell to set the audio device
    ps_script = f'''
    If (! (Get-Module -Name "AudioDeviceCmdlets" -ListAvailable)) {{
        $url = 'https://github.com/frgnca/AudioDeviceCmdlets/releases/download/v3.0/AudioDeviceCmdlets.dll'
        $location = ($profile | split-path) + "\\Modules\\AudioDeviceCmdlets\\AudioDeviceCmdlets.dll"
        New-Item "$($profile | split-path)\\Modules\\AudioDeviceCmdlets" -Type directory -Force

        [Net.ServicePointManager]::SecurityProtocol = "tls12, tls11, tls"
        (New-Object System.Net.WebClient).DownloadFile($url, $location)
    }}

    If (! (Get-Module -Name "AudioDeviceCmdlets")) {{
        get-module -Name "AudioDeviceCmdlets" -ListAvailable | Sort-Object Version | select -last 1 | Import-Module -Verbose
    }}

    if ((Get-Module -Name "AudioDeviceCmdlets")) {{
        Get-AudioDevice -List | where Type -like "Playback" | where name -like "*{device_name}*" | Set-AudioDevice -Verbose
        Get-AudioDevice -List | where Type -like "Recording" | where name -like "*{device_name}*" | Set-AudioDevice -Verbose
    }}
    '''
    subprocess.run(['powershell', '-Command', ps_script])

def select_output_device():
    devices = get_devices()
    device_list = [desc for _, desc, _ in devices]
    
    root = tk.Tk()
    root.title("Select Output Device")

    var = tk.StringVar()
    ttk.Label(root, text="Select Output Device:").pack(pady=5)
    device_selector = ttk.Combobox(root, textvariable=var, values=device_list)
    device_selector.pack(pady=5)
    device_selector.set(device_list[0])  # Set default value

    def on_select(event):
        selected_device = var.get()
        print(f"Selected Output Device: {selected_device}")
        set_audio_device(selected_device)

    device_selector.bind("<<ComboboxSelected>>", on_select)

    root.mainloop()

if __name__ == '__main__':
    select_output_device()
