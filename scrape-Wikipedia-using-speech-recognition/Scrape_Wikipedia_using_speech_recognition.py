import pyttsx3
import speech_recognition as SR
import wikipedia
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice.id)
# select voice among the available options
# engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def obey_command():
    # It takes input from the microphone and returns output as a string
    mic = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        mic.pause_threshold = 1
        audio = mic.listen(source)
    try:
        print("Recognizing...")
        query = mic.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":

    query = obey_command().lower()

    if 'wikipedia' in query:
        speak("Searching wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(result)

    sys.exit()
