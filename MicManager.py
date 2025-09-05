import debuglogger as log
import pyaudio

def list_active_microphones():
    pa = pyaudio.PyAudio()
    log.write("Number of devices (all APIs, input + output):"+ str(pa.get_device_count()))

    for i in range (pa.get_device_count()):
        device_info = pa.get_device_info_by_index(i)
        if device_info['maxInputChannels'] != 0 and device_info['hostApi'] == 0:
            log.write('Device ' + str(i) + ': ' + device_info['name'])