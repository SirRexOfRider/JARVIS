"""
Name: wikipedia_2.py
Author:Rex
Date:3/18/2024
Purpose: Import and use wikipedia/oop
"""

#pip install wikipedia
import wikipedia



class WikipediaApp:
    def __init__(self):
        pass

    def get_wikipedia(self):
        """Search wikipedia"""

        try:
            #Type in your search term
            result = input("Search wikipedia: ")
            #Return a summary result of 3 sentences
            self.__summary = wikipedia.summary(result, sentences = 3)
        
        except:
            #Use raise for troubleshooting exceptions
            #raise
            #if there is an exception, allow the user to try again
            print("Try a different search term.")
    
    def display_wikipedia(self):
        """Display Wikipedia search results"""

        print(self.__summary)

#Create a jarvis program object
wikipedia_app = WikipediaApp()
while True:
    wikipedia_app.get_wikipedia()
    wikipedia_app.display_wikipedia()


