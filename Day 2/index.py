##slicing string
## spesific sliicing index:index
## start slicing :index
## end slicing index:

## ex:
myStr = str('hello world')
print(myStr[:5])


##modify string
## upper(), lower(), srtip(), replace(), split()

##uper() return string to uppercase
toUpper = str('hello world')
print(toUpper.upper())

## lower(), return string to lowercase
toLower = str('HELLO WORLD')
print(toLower.lower())

# strip(), remove whitespace
removeWS = str('     Hello world     ')
print('without strip(): ',removeWS, 'with strip():', removeWS.strip())

# replace(), replace spesific string. note replace() is casesencitive, ex: e != E
# replace() have 2 parameter, first one is the string that u want to change, Secondly, what do you want to turn the string into
strReplace = str('Hello World')
print(strReplace.replace('Hello', 'Om Swastyatu'))


# split(), split strin into substring, like array
strToSplit = str('You are my everything')
print(strToSplit.split(' '))


#string concatination 
# ex:
hello = str('Om Swastyastu') 
world = str('World')
print(hello, world)