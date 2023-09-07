import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
 engine.say(text)
 engine.runAndWait()
def take_command():
 try:
    with sr.Microphone() as source:
        print('listening....')
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'alexa' in command:
          command=command.replace('alexa','')


 except:
    pass
 return command

def run_alexa():
    command=take_command()

    if 'play' in command:
        song=command.replace('play','')

        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')

        talk('Current time is'+time)
    elif 'info' in command:
        person=command.replace('info','')
        info=wikipedia.summary(person,1)
        talk(info)
    elif 'date' in command:
        talk('Sorry ,I am an ai bot .')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')
while True:
 run_alexa()

