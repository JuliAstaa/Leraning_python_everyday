""" 
Task
Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True

In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS
 """

def is_uppercase(inp):
    #cek apakah string mengandung alphabet apa tidak
    contains_alphabets = any(char.isalpha() for char in inp)
    return inp.isupper() if contains_alphabets else True

print(is_uppercase("$%&"))