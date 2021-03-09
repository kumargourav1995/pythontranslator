# Language Translation program using google Translation API in python
#Author: Kumar Gourav Dakhinray
#Libraries Used: Google text to speech, Speech recognition, Google Trans & Play sound


import gtts                                     #google text to speech library
import speech_recognition as sr                 #speech recognition Library
import googletrans                              #google translation Library. USE googletrans 3.1.0a0 strictly
import playsound                                #Library to play sound

recognizer=sr.Recognizer()                         #initializing voice recogniser
translator=googletrans.Translator()                 #initializing google translate

print("WELCOME TO THE LANGUAGE TRANSLATOR PROGRAM.\n")
print("WHAT DO YOU WANT TO TRANSLATE TODAY\n")
print("- Press 1 for TEXT TO TEXT Translation\n")
print("- press 2 for TEXT TO AUDIO Translation\n")
print("- press 3 for AUDIO TO TEXT Translation\n")
print("- Press 4 for AUDIO TO AUDIO Translation\n")

choice = input("ENTER YOUR CHOICE\n")

if choice =='1':
    try:
        text=input("ENTER YOUR TEXT\n")
    except:
       pass
    a=translator.translate(text, dest='hi')
    print("Translating the text file to your preferred language\n")
    print("processing............\n")
    print(a.text)

if choice == '2':
    try:
        text=input("ENTER YOUR TEXT\n")
    except:
       pass

    a=translator.translate(text, dest='hi')
    print("Translating the text file to your preferred language\n")
    print("processing............\n")
    converted_audio=gtts.gTTS(a.text,lang='hi')
    converted_audio.save('audio.mp3')
    playsound.playsound('audio.mp3')

if choice =='3':
    try:
        with sr.Microphone() as source:
            print('SPEAK NOW')
            voice = recognizer.listen(source)

            text = recognizer.recognize_google(voice)
        print(text)
    except:
        pass

a=translator.translate(text, dest='hi')
print("\nprocessing............\n")
print("translated text\n\n"+a.text)

if choice=='4':
    try:
        with sr.Microphone() as source:
            print('SPEAK NOW')
            voice = recognizer.listen(source)

            text = recognizer.recognize_google(voice)
            print(text)
    except:
        pass

a=translator.translate(text, dest='hi')
print(a.text)
converted_audio=gtts.gTTS(a.text,lang='hi')
converted_audio.save('audio.mp3')
playsound.playsound('audio.mp3')