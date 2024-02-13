def sortByLenght(array):
    def lenOfWord(e):
        return len(e)
    array.sort(key=lenOfWord)
    return array

print(sortByLenght(["Beg", "Life", "I", "To"]))