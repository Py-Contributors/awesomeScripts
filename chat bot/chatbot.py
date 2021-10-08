import speech_recognition as sr
import datetime
import webbrowser as wb
import os
import pyttsx3
import wikipedia
import pywhatkit
import pyjokes as pj
import smtplib
import requests
from bs4 import BeautifulSoup
import winsound
import operator


engine = pyttsx3.init()


def search():
    speech("enter the topic you want to search on wikipedia  ")
    query = takeCommand().lower()
    wresult = str(wikipedia.search(query, results=1))
    results = wikipedia.summary(wresult, sentences=2)
    speech("According to Wikipedia")
    print(results)
    speech(results)


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if(hour >= 0 and hour < 12):
        wish = 'good morning'
        # speech('good morning')
        # print('good morning')
    elif(hour >= 12 and hour <= 18):
        wish = 'good afternoon'
        # speech('good afternoon')
        # print('good afternoon')
    else:
        wish = 'good evening'
        # speech('good evening')
        # print('good evening')

    return wish


def Whatsapp():
    speech('opening whatsApp')
    os.startfile('C:\\Users\\avyay\\AppData\\Local\\WhatsApp\\WhatsApp.exe')


def chrome():
    speech('opening chrome')
    os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')


def speech(audio):
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')       # getting details of current voice
    # engine.setProperty('voice', voices[1].id)  # changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def dateAndTime():
    time = datetime.datetime.now().strftime("%Y\n %B\n %A\n %I %M %S %Z")
    print(time)
    speech(time)


def google():
    wb.open('google.com')
    speech("opening google")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print()
        print("Listening...")
        print()
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        print()
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        print()
        print(e)
        return "None"
    return query


def playmusic():
    speech("what would you like to play ")
    song = takeCommand()
    speech('playing '+song)
    pywhatkit.playonyt(song)


def joke():
    speech('telling a joke')
    a = pj.get_joke(language='en', category='neutral')
    speech(a)
    print(a)


def searchOnGoogle():
    speech('what would you like to search on google')
    print('what would you like to search on google')
    a = takeCommand()
    pywhatkit.search(a)


def weather():
    speech("please tell city name ")

    city = takeCommand().lower()
    print(city)

    url = "https://google.com/search?q="+"weather"+city
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_skyDescription = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    data = time_skyDescription.split('\n')
    time = data[0]
    sky = data[1]

    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

    strd = listdiv[5].text

    pos = strd.find('wind')
    otherData = strd[pos:]

    print("Temperature is ", temp)
    speech("Temperature is "+temp)
    print("time is ", time)
    speech("time is "+time)
    print("sky description: ", sky)
    speech("sky description: "+sky)
    print(otherData)


def alarm(Timing):

    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))

    altime = altime[11:-3]
    print(altime)
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)

    print(f"Done, alarm is set for {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour and Mireal == datetime.datetime.now().minute:
            print("alarm is running")
            winsound.PlaySound('abc', winsound.SND_LOOP)

        elif Mireal < datetime.datetime.now().minute:
            break


def calculate():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        speech("say what you want to calculate, example 3 plus 3")
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        my_string = r.recognize_google(audio)
        print(my_string)

        def get_operator_fn(op):
            return{
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                'divided': operator.__truediv__,
            }[op]

        def evel_binary(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        speech("your result is ")
        speech(evel_binary(*(my_string.split())))


wish = wishMe()
print(wish)
speech(f"{wish} sir, i am jarvis what would you like to do")

while True:

    speechinput = takeCommand().lower()
    # print(speechinput)

    if 'time' in speechinput:
        dateAndTime()

    elif 'google' in speechinput:
        google()

    elif 'play music' in speechinput:
        playmusic()

    elif 'open whatsapp' in speechinput:
        Whatsapp()

    elif 'open chrome' in speechinput:
        chrome()

    elif 'search' in speechinput:  # wikipedia
        search()

    elif 'tell me a joke' in speechinput:
        joke()

    elif 'send mail' in speechinput:
        sendmail()

    elif 'exit' in speechinput:
        speech("goodbye sir going off duty")
        print("goodbye sir going off duty")
        exit()

    elif 'search on web' in speechinput:
        searchOnGoogle()

    elif 'what is the weather' in speechinput:
        weather()

    elif 'what is your name' in speechinput:
        speech('my name is jarvis your personal voice assistant')

    elif'who made you' in speechinput:
        speech('i was made by avyay jain')

    elif 'alarm' in speechinput:
        speech("say set alarm for 5:30 am ")
        print("say set alarm for 5:30 am")
        tt = takeCommand()
        tt = tt.replace("set alarm to ", "")
        tt = tt.replace(".", "")
        tt = tt.upper()
        alarm(tt)

    elif'calculate' in speechinput:
        calculate()
