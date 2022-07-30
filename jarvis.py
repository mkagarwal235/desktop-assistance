import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import random
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    """This function will convert string  into speech..."""
    engine.say(audio)
    engine.runAndWait()     #without this command speech will not be qudiable to us.
def wishMe():
    """This func will wish when program is executing..."""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis Please tell me how may i help you?")
def takeCommand():
    # it take microphone input and return string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold=2000
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again Please.....")
        return "None"
    return query
def sendEmail(to,contet):
    """This func is used to send mail........"""
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('monuagarwal235@gmail.com','9304536730')
    server.sendmail('monuagarwal235@gmail.com',to,contet)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace('wikipedia',' ')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir='C:\\Users\\cws\\Music'
            songs=os.listdir(music_dir)
            number=random.randint(0,len(songs)-1)
            print(number)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[number]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strptime("%H%M%S")
            print(f"sir the time is {strTime}")
        elif 'open code' in query:
            codepath='C:\\Users\\cws\\AppData\\Local\\Programs\\Microsoft VS Code\\Code'
            os.startfile(codepath)
        elif 'open turbo c' in query:
            cpath='"C:\\TURBOC3\\Turbo C++\\"'
            os.startfile(cpath)
        elif 'send email' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to="monukumar25149@gmail.com"
                sendEmail(to ,content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("sorry my friend monu i am not able to senf this email.")
        elif 'close' in query:
            exit()

