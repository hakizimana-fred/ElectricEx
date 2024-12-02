import sounddevice as sd
import numpy as np

SETTINGS = {
    'SAMPLE_RATE': 44100,
    'DURATION': 0.5,       
    'THRESHOLD': 0.02     
}

def detect_sound():
    try:
        print(SETTINGS['SAMPLE_RATE'])
        while True:
            audio_data = sd.rec(int(SETTINGS['SAMPLE_RATE'] * SETTINGS['DURATION']), samplerate=SETTINGS['SAMPLE_RATE'], channels=1, dtype='float64')
            sd.wait()

            rms_volume = np.sqrt(np.mean(audio_data**2))

            # Check if sound level exceeds the threshold
            if rms_volume > SETTINGS['THRESHOLD']:
                print("Sound detected!")
                turn_on_or_off(True)
            else:
                print("No significant sound detected.")
                turn_on_or_off(False)

    except KeyboardInterrupt:
        print('\nListening Aborted')


def turn_on_or_off(is_on):
    if is_on:
        print("Light ON")
    else:
        print("Light OFF")
        return 0


detect_sound()