import speech_recognition as sr
from time import ctime
import playsound
import os
import random
from gtts import gTTS
import webbrowser
import pyjokes

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            Piku_speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            Piku_speak('Sorry, I did not understand what you said')
            return None
        except sr.RequestError:
            Piku_speak('Sorry, my speech service is down')
            return None

def Piku_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(2, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'your name' in voice_data:
        Piku_speak('My name is Piku')
    elif 'time' in voice_data:
        Piku_speak(ctime())
    elif 'MSP of rice' in voice_data:
        Piku_speak("The minimum support price of grade A rice is 2203 per quintal whereas the common quality rice is 2183 per quintal.")
    elif 'MSP of wheat' in voice_data:
        Piku_speak("The minimum support price of wheat is 2275 per quintal.")
    elif 'MSP of cotton' in voice_data:
        Piku_speak('The minimum support price of  medium staple cotton is 6620 per quintal whereas the long staple cotton is 7020 per quintal. ')
    elif 'MSP of gram' in voice_data:
        Piku_speak('The minimum support price of gram commonly known as chana is 5440 per quintal')
    elif 'MSP of moong ' in voice_data:
        Piku_speak('The minimum support price of moong is 8558 per quintal.')
    elif 'MSP of Groundnut' in voice_data:
        Piku_speak('The minimum support price of Groundnut is 6377 per quintal.')
    elif 'MSP of sunflower seed ' in voice_data:
        Piku_speak('The minimum support price of sunflower seed is 6760 per quintal.')
    elif 'MSP of bajra ' in voice_data:
        Piku_speak('The minimum support price of bajra is 2500 per quintal.')
    elif 'Government ' in voice_data or 'yojanas' in voice_data:
        Piku_speak('Here is a list of Government yojanas for farmers Pradhan Mantri Kisan Samman Nidhi.Pradhan Mantri Kisan MaanDhan Yojana .Pradhan Mantri Fasal Bima Yojana.Agriculture Infrastructure Fund (AIF).Micro Irrigation Fund.')
    elif 'search' in voice_data:
        search = record_audio("What do you want to search?")
        url = "https://google.com?q=" + search
        webbrowser.get().open(url)
        Piku_speak("Here is what I found for " + search)
    elif 'location' in voice_data:
        location = record_audio("What is the location?")
        url = "https://google.nl/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        Piku_speak("Here is the location of " + location)
    elif 'joke' in voice_data:
        Piku_speak(pyjokes.get_joke())
    elif 'youtube' in voice_data:
        Piku_speak("Here you go to Youtube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in voice_data:
        Piku_speak("Here you go to Google")
        webbrowser.open("https://www.google.com")

Piku_speak("How can I help you?")
ask1 = True
while ask1:
    voice_data = record_audio()
    if voice_data is not None:
        respond(voice_data)
