# -----this is the jarviz project which we instructions and computer work with the use of our instructions 


# -----pyttsx3 ----pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3. An application invokes the pyttsx3.

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

# ----Creating the voice with the help of pyttsx
# ----there are 2 main voices girl and man
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

# -----Creating a function which we genrate a audio voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# -----Creating the function which is wish of me according the time 
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")

    speak("I am Jarviz Sir. Please tell me how may I help you")

# -----it takes microphone input frpm the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mtayyabashraf7@gmail.com','tayyab21')
    server.sendmail('mtayyabashraf7@gmail.com', to, content)
    server.close()
if __name__== '__main__':
    wishme()
    while True:
        query =takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        
        elif 'play music' in query:
            music_dir ='D:\\songs\\Nusrat Fatah Ali Khan'
            songs = os.listdir(music_dir)
            print(songs)
            ran=random.randint(0,6)
            os.startfile(os.path.join(music_dir,songs[ran]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\TAYYAB\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'email to tayyab' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'mtayyabashraf7@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent Successfully!")
            except Exception as e:
                print(e)
                speak("Soory my friend tayyab bhai. I am not able to send this email")
        elif 'exit' in query:
            exit()
 