"""
Name: jarvis_speech_recognition_3.py
Author:Rex
Date:3/5/24
Purpose: Voice recognition from Google Speech API OOP
"""

#pip install speechrecognition
from sys import exit
import speech_recognition as sr
import wikipedia

class Jarvis:
    def __init__(self) -> None:
        #Create SpeechRecognition recognizer object
        self.r = sr.Recognizer()

    def take_user_input(self):
        """Recognize user voice input using
        Speech recognitino mudoule, coverts it to text"""


        print("COMMANDS: Wikipedia, start up my suit, hello, quit")
        with sr.Microphone() as source:
            self.r.pause_threshold = 1
            print('Listening . . . .')
            audio = self.r.listen(source)

        try:
            print("Recognizing . . .")
            #Capture the recongized word in a variable
            recognized_words = self.r.recognize_google(
                audio, language='en-US', show_all=True
            )

            #Google speech recognition returns a list of dictionaries
            #Pull only the transcript wwith the highest confidence
            self.query = recognized_words['alternative'] [0] ['transcript']
            print(self.query)

        except sr.UnknownValueError:
            print(f"Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            #If there was an error communicationg with Google Speech
            print(f"Google Speech did no respond: {e}")

#Commands---------------------------------------

    def steel_man_suit(self):
        print("\nRight away sir! The suit is starting up now.\n")

    def wikipedia(self):
        """Recognize user voice input using
        Speech recognitino mudoule, coverts it to text"""
        with sr.Microphone() as source:
            self.r.pause_threshold = 1
            print('Listening . . . .')
            audio = self.r.listen(source)

        try:
            print("Recognizing . . .")
            #Capture the recongized word in a variable
            recognized_words = self.r.recognize_google(
                audio, language='en-US', show_all=True
            )

            #Interpret words
            search_term = recognized_words['alternative'] [0] ['transcript']

            #Search wikipedia with search term
            self.__summary = wikipedia.summary(search_term, sentences = 3)
            print(f"\n{self.__summary}")

        except sr.UnknownValueError:
            print(f"Google Speech Recognition could not understand audio")
            

        except sr.RequestError as e:
            #If there was an error communicationg with Google Speech
            print(f"Google Speech did no respond: {e}")
            

#---------------------------------------------------
    def voice_commands(self):
        if self.query == "quit":
            print("Goodbye!")
            exit()
        
        if self.query == "hello":
            print("\nHello sir!\n")

        if self.query == "start up my suit":
            jarvis.steel_man_suit()

        if self.query == "Wikipedia":
            jarvis.wikipedia()
#--------------------------------------------------

#Create a jarvis program object
jarvis = Jarvis()
while True:
    jarvis.take_user_input()
    jarvis.voice_commands()