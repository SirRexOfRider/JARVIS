"""
Name: jarvis_speech_recognition_1.py
Author:Rex
Date:3/4/24
Purpose: Voice recognition for Google
Sample code using Google Speech Recognition
form the SpeechRecognition library sample code.
You can use the Google Speech API for free 50 times a day
"""

#pip install SPeechRecognition
import speech_recognition as sr

#Create SpeechRecognition recognizer object
r = sr.Recognizer()

#With your local microphone as the source
with sr.Microphone() as source:
    print('Listening . . . .')
    audio = r.listen(source)

    try:
        print("Recognizing . . .")
        #Capture the recongized word in a variable
        recognized_words = r.recognize_google(
            audio, language='en-US', show_all=True
        )
        #Google speech recognition returns a list of dictionaries
        #Pull only the transcript wwith the highest confidence
        recognized_words = recognized_words['alternative'] [0] ['transcript']
        print(f"You may have said: {recognized_words}")
    except sr.UnknownValueError:
        print(f"Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        #If there was an error communicationg with Google Speech
        print(f"Google Speech did no respond: {e}")

