import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Masuk dengan akun Gmail Anda
    server.login('x@gmail.com', 'password')
    email = EmailMessage()
    email['From'] = 'x@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    #Masukkan list email tujuan
    #Format 'inisial' : 'alamat email'
    '1': 'y@gmail.com',
    '2': 'z@gmail.com'
}


def get_email_info():
    talk('Namaku Ruby Bot, aku orang bule a, Mau ngirim email ke c i pa')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('subjek nya i pa')
    subject = get_info()
    talk('Pesannya i pa')
    message = get_info()
    send_email(receiver, subject, message)
    talk('okay aku kirim in')

get_email_info()