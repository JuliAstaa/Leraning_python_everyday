def longest(s1, s2):
    char = set(f"{s1}{s2}")
    mylist = sorted(char)
    return "".join(mylist)

print(longest("aretheyhere", "yestheyarehere"))
        