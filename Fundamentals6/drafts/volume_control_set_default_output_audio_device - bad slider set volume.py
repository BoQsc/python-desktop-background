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

# Function to enumerate audio devices
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

# Function to set audio device
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

# Function to adjust volume
def set_volume(volume):
    import subprocess

    # PowerShell command to set volume
    ps_script = f'''
    Function Set-Speaker($Volume) {{
        $wshShell = new-object -com wscript.shell
        1..50 | % {{ $wshShell.SendKeys([char]174) }}
        1..$Volume | % {{ $wshShell.SendKeys([char]175) }}
    }}

    Set-Speaker -Volume {volume}
    '''
    subprocess.run(['powershell', '-Command', ps_script])

# Function to select output device with volume slider
def select_output_device():
    devices = get_devices()
    device_list = [desc for _, desc, _ in devices]
    
    root = tk.Tk()
    root.title("Select Output Device with Volume Control")

    var_device = tk.StringVar()
    var_volume = tk.DoubleVar()

    ttk.Label(root, text="Select Output Device:").pack(pady=5)
    device_selector = ttk.Combobox(root, textvariable=var_device, values=device_list)
    device_selector.pack(pady=5)
    device_selector.set(device_list[0])  # Set default value

    ttk.Label(root, text="Volume:").pack(pady=5)
    volume_slider = ttk.Scale(root, from_=0, to=100, variable=var_volume)
    volume_slider.pack(pady=5)

    def on_select(event):
        selected_device = var_device.get()
        selected_volume = int(var_volume.get())
        print(f"Selected Output Device: {selected_device}, Volume: {selected_volume}")
        set_audio_device(selected_device)
        set_volume(selected_volume)

    device_selector.bind("<<ComboboxSelected>>", on_select)
    volume_slider.bind("<B1-Motion>", lambda e: on_select(None))

    root.mainloop()

if __name__ == '__main__':
    select_output_device()
