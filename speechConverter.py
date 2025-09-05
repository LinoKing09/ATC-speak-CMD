import speech_recognition as sr
import pyttsx3 

engine = pyttsx3.init()

def listen(Mic_Index): 
    r = sr.Recognizer() 
    mic = sr.Microphone(device_index=Mic_Index) 

    try:
        # using the microphone as source for input.
        with mic as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            UserText = r.recognize_google(audio2)
            UserText = UserText.lower()
            enable_automatic_punctuation=False
            print(UserText)
            #SpeakText(MyText)
            return UserText
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "Error"
        
    except sr.UnknownValueError:
        print("nothing spoken")
        return None
 

def speak(command):  
    # Initializing the engine
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(command) 
    engine.runAndWait()
     
 
