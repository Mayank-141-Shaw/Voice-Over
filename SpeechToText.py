import speech_recognition as sr
import pyttsx3

# internet connection is necessary to run
r = sr.Recognizer()

def speak_txt(cmd):
    engine = pyttsx3.init()
    engine.say(cmd)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as src:            # microphone is the input
            r.adjust_for_ambient_noise(src, duration=0.2)             # wait a momment for mic to adjust to threshold noise

            print('Say: ')
            audio = r.listen(src)                                       # speak or give audio input to mic
            print('Stop ')
            txt = r.recognize_google(audio)                             # recognizer needs a google connection

            print(txt)
            speak_txt(txt)
    except sr.RequestError as se:
        print('Could not request results {0}'.format(se))
    except sr.UnknownValueError:
        print('Unlnown value occured')