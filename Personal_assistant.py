dfrom gettext import find
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import time

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('YVGKHH-97XXLTX5EJ')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate',130)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Boss')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Boss')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening Boss')

greetMe()

# speak('Hello Boss')
# speak('How may I help you?')

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('Here it is')
            webbrowser.open('www.youtube.com')

        elif 'weather' in query or 'climate' in query:
            speak('Here it is')
            res=client.query(query)
            weather=next(res.results).text
            speak(weather)

        elif 'good afternoon' in query or 'good morning' in query or 'good evening' in query:
            speak('How may I help you,sir')

        elif 'i love you' in query or 'love you' in query:
            speak('Love you too..feeling great to be your friend')

        elif 'i hate you' in query or 'hate you' in query:
            speak('I''m sorry..please forgive me..')

        elif 'what is your name' in query:
            speak('My name is Jarvis, what\'s your\'s?')
            name=myCommand();
            name=name.replace('I am ','')
            speak('Hi,'+name+', Glad to have a conversation with u')

        elif 'who are you' in query:
            speak('I am Aravindh\'s personal assistant')

        elif 'what can you do' in query:
            speak('I can open youtube,music,google and can search for you,I will be your personal assistant')

        elif 'open google' in query:
            speak('Here it is')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('Here it is')
            webbrowser.open('www.gmail.com')

        # elif 'play some music' in query:
        #     speak('Here it is')
        #     webbrowser.open('https://gaana.com/song/bodhai-kaname')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient?')
            recipient = myCommand()

            if 'myself' in recipient:
                try:
                    speak('What should I say?')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("aravindhs.21it@gmail.com", '9042094948')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Boss!I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Boss, have a good day.')
            sys.exit()

        elif 'change your name' in query or 'can i change your name' in query or 'can you change your name' in query:
            speak('No,Its not possible')

        elif 'hello' in query:
            speak('Hello Boss..How are you?')

        elif 'hi' in query:
            speak('Hi Boss')

        elif 'who is your well wisher' in query:
            speak('Itz Mr.Arjun')

        elif 'who do you miss right now' in query:
            speak('I am missing Chendhur now.')

        elif 'hai' in query:
            speak('Hai Boss')

        elif 'bye' in query or 'thank you' in query or 'adios' in query or 'ciao' in query:
            speak('Bye Boss, have a good day.')
            sys.exit()

        elif 'play some music' in query:
            webbrowser.open('https://gaana.com/song/bodhai-kaname')
            speak('Okay, here is your music!Play the song and Enjoy!')

        elif 'search' in query:
            speak('What are you searching for?')
            search=myCommand()
            url='https://google.com/search?q=' + search
            speak('here is what I found for  '+search )
            webbrowser.get().open(url)
            print('here is what I found for ' + search )

        elif 'greet them' in query:
            speak('Welcome to our presentation!Have a great day')

        elif 'find' in query:
            speak('What do you wanna know?')
            try:
                search=myCommand()
                res=client.query(search)
                question=next(res.results).text
                speak(question)
            except:
                speak('Sorry sir..Unable to get it.')

        else:
            speak('Anyother')
        time.sleep(3)
        # speak('Anyother')