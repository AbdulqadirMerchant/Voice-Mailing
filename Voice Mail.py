import yagmail
import speech_recognition as sr
import pyttsx3
from time import sleep

sleep(6)

engine = pyttsx3.init()


def record_voice():
    try:
        recording = sr.Recognizer()
        with sr.Microphone() as source:
            recording.adjust_for_ambient_noise(source)
            engine.say("Please read your message now.....")
            engine.runAndWait()
            audio = recording.listen(source)
            message = recording.recognize_google(audio)
            return message
    except:
        engine.say("Looks like something went wrong... Please try again!")
        engine.runAndWait()


mail = yagmail.SMTP(user = "<Your Mail ID>", password = "<Mail Password>")
message = record_voice()
mail.send(to = "<Receiver Mail ID>", subject = "Voice mail using python", contents = message)
engine.say("Mail has been sent successfully!")
engine.runAndWait()
