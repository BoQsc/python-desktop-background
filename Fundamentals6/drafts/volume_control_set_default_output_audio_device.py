import ctypes
from ctypes import wintypes

# Load necessary Windows libraries
ole32_dll = ctypes.windll.ole32
mmdeviceapi = ctypes.windll.MMDevAPI
propsys = ctypes.windll.ProgID  # Ensure this is correctly handled

# Define necessary Windows types
class PROPERTYKEY(ctypes.Structure):
    _fields_ = [("fmtid", ctypes.c_int64), ("pid", ctypes.c_int)]

PKEY_Device_FriendlyName = PROPERTYKEY(0xDE1AB5B3C8BF4014, 13)  # Defined property key for device name

IMMDeviceEnumerator = ctypes.POINTER(ctypes.c_void_p)
IMMDeviceCollection = ctypes.POINTER(ctypes.c_void_p)
IMMDevice = ctypes.POINTER(ctypes.c_void_p)
IPropertyStore = ctypes.POINTER(ctypes.c_void_p)

# Function to get default audio endpoint
IMMDeviceEnumerator_CreateInstance = mmdeviceapi.CoCreateInstance
IMMDeviceEnumerator_CreateInstance.restype = wintypes.HRESULT
IMMDeviceEnumerator_CreateInstance.argtypes = [wintypes.REFGUID, wintypes.HANDLE, wintypes.DWORD, wintypes.REFGUID, ctypes.POINTER(ctypes.c_void_p)]

# Function to get default audio device
IMMDeviceEnumerator_GetDefaultAudioEndpoint = mmdeviceapi.CoCreateInstance
IMMDeviceEnumerator_GetDefaultAudioEndpoint.restype = wintypes.HRESULT
IMMDeviceEnumerator_GetDefaultAudioEndpoint.argtypes = [wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(ctypes.c_void_p)]

# Function to open property store
IMMDevice_OpenPropertyStore = IMMDevice.contents[0]  # Example pointer, adjust as necessary
IMMDevice_OpenPropertyStore.restype = wintypes.HRESULT
IMMDevice_OpenPropertyStore.argtypes = [wintypes.DWORD, ctypes.POINTER(IPropertyStore)]

# Function to get property value
IPropertyStore_GetValue = IPropertyStore.contents[0]  # Example pointer, adjust as necessary
IPropertyStore_GetValue.restype = wintypes.HRESULT
IPropertyStore_GetValue.argtypes = [ctypes.POINTER(PROPERTYKEY), ctypes.POINTER(ctypes.c_void_p)]

# Function to set default audio playback device
def set_default_audio_playback_device(devID):
    hr = mmdeviceapi.CoCreateInstance(ctypes.byref(GUID_CPolicyConfigClient),
                                      None,
                                      CLSCTX_ALL,
                                      ctypes.byref(IPolicyConfigClient),
                                      ctypes.byref(pPolicyConfig))

    if hr == 0:
        hr = pPolicyConfig.SetDefaultEndpoint(devID, eConsole)
        pPolicyConfig.Release()
    
    return hr

def get_default_output_device():
    deviceEnumerator = ctypes.c_void_p()
    hr = IMMDeviceEnumerator_CreateInstance(None, None, 1, ctypes.byref(GUID_MMDeviceEnumerator), ctypes.byref(deviceEnumerator))
    if hr == 0:
        device = ctypes.c_void_p()
        hr = IMMDeviceEnumerator_GetDefaultAudioEndpoint(deviceEnumerator, eRender, eMultimedia, ctypes.byref(device))
        if hr == 0:
            propertyStore = ctypes.c_void_p()
            hr = IMMDevice_OpenPropertyStore(device, 0, ctypes.byref(propertyStore))
            if hr == 0:
                friendlyName = ctypes.c_wchar_p()
                hr = IPropertyStore_GetValue(propertyStore, ctypes.byref(PKEY_Device_FriendlyName), ctypes.byref(friendlyName))
                if hr == 0:
                    print(f"Default Output Device: {friendlyName.value}")
                propertyStore.Release()
            device.Release()
        deviceEnumerator.Release()

def main():
    get_default_output_device()
    set_default_audio_playback_device("{0.0.1.00000000}.{your-device-guid}")

if __name__ == '__main__':
    main()
