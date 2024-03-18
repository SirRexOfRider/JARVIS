"""
Name: wikipedia_1.py
Author:Rex
Date:3/18/2024
Purpose: Import and use wikipedia
"""

#pip install wikipedia
import wikipedia

#type in your search term
result = input("Search Wikipedia: ")

#Return a summary result of 3 sentences
summary = wikipedia.summary(result, sentences = 3)

#print result
print(summary)