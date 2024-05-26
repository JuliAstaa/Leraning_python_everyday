import re
def shortcut( s ):
    result = re.sub(r'[aiueo]', '', s)
    return result
    

removeVowel = lambda string: re.sub('[aiueo]', '', string)