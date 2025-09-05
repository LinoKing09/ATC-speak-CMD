import pyttsx3

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)

engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.say("Say again.") 
engine.runAndWait()