#README.md
On running this script, a person is first required to give input through speech and then output will be the first two sentences of the search result as given on Wikipedia.
This makes use of 'pyttsx3' and 'speech_recognition' for the purpose of taking input and providing output in speech format and 'wikipedia' library for the scraping. 'sys' library has been used for the sole purpose of termination of the program.



#requirements.txt
-> Suggest more funtionalities that can be added to it
-> Suggest improvisations in implementation
-> Improve documentation



import pyttsx3
import speech_recognition as SR
import wikipedia 
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# for voice in voices:
#     print(voice.id)
# select voice among the available options 

engine.setProperty('voice', voices[1].id) 

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
