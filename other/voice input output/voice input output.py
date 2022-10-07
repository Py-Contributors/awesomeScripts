import pyttsx3 as pt
import speech_recognition as sr

# voice input-----
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hey Buddy Say Something :")
    a = r.listen(source)

    try:
        text = r.recognize_google(a)
        print(text)
    except Exception as e:
        print(e)


# voice output-----
engine = pt.init()


def speak(sent):
    engine.say(sent)
    engine.runAndWait()
    print(sent)
    return sent


if __name__ == "__main__":
    b = str(input("Please enter what to say: "))
    speak(b)
