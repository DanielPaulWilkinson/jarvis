from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def getDefaultAudioDevice():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume


def volume100():
    getDefaultAudioDevice().SetMasterVolumeLevel(-0, None)


def volume90():
    getDefaultAudioDevice().SetMasterVolumeLevel(-1.5, None)


def volume80():
    getDefaultAudioDevice().SetMasterVolumeLevel(-3.4, None)


def volume70():
    getDefaultAudioDevice().SetMasterVolumeLevel(-5.4, None)


def volume60():
    getDefaultAudioDevice().SetMasterVolumeLevel(-7.6, None)


def volume50():
    getDefaultAudioDevice().SetMasterVolumeLevel(-10.2, None)


def volume40():
    getDefaultAudioDevice().SetMasterVolumeLevel(-13.6, None)


def volume30():
    getDefaultAudioDevice().SetMasterVolumeLevel(-17.7, None)


def volume20():
    getDefaultAudioDevice().SetMasterVolumeLevel(-23.4, None)


def volume10():
    getDefaultAudioDevice().SetMasterVolumeLevel(-32.6, None)


def volume0():
    getDefaultAudioDevice().SetMasterVolumeLevel(-50.0, None)
