""" Build a Python program that prompts the user to enter a sentence and then prints the number of words in that sentence.z """

import re

def lengthOfSentence(sentence):
    sentence = re.findall(r'\b\w+\b', sentence)
    return len(sentence)

print(lengthOfSentence('My name is I Made Juli Astawa ! , and you?'))