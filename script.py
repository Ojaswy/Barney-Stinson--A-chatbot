import aiml
import os
import time, sys
#from gtts import gTTS
#from pygame import mixer
import pyttsx
import warnings

mode = "text"
if len(sys.argv) > 1:
    if sys.argv[1] == "--voice" or sys.argv[1] == "voice":
        try:
            import speech_recognition as sr
            mode = "voice"
        except ImportError:
            print("\nInstall SpeechRecognition to use this feature.\nStarting text mode\n")

terminate = ['bye','shutdown','exit','quit','gotosleep','goodbye']
# def speak(jarvis_speech):
#   tts = gTTS(text=jarvis_speech, lang='en')
#   tts.save('jarvis_speech.mp3')
#   mixer.init()
#   mixer.music.load('jarvis_speech.mp3')
#   mixer.music.play()
#   while mixer.music.get_busy():
#       time.sleep(1)

def offline_speak(jarvis_speech):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(jarvis_speech)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go for Barney: ")
        audio = r.listen(source)
    try:
        print r.recognize_google(audio)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        offline_speak("I couldn't understand what you said! Would you like to repeat?")
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    #kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    if mode == "voice":
        response = listen()
    else:
        response = raw_input("Go for BARNEY : ")
    if response.lower().replace(" ","") in terminate:
        break
    jarvis_speech = kernel.respond(response)
    print "Barney: " + jarvis_speech
    offline_speak(jarvis_speech)
    
