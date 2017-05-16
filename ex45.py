import random
import time

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

inputword = raw_input('Enter word> ')
#inputguess = raw_input('Enter guess> ')
totalcounter = 0
rightcounter = 0
fullmatch = False
lettermatch = False

inputlist = list(inputword)
guesslist = []
printlist = []


while rightcounter < len(inputword):
    guesslist = []
    for each in inputword:
        guesslist.append(random.choice(letters))

    if guesslist[rightcounter] == inputword[rightcounter]:
        printlist.append(guesslist[rightcounter])
        rightcounter += 1
        print ''.join(printlist) + ''.join(guesslist[rightcounter:])
    elif len(printlist) == 0:
        print ''.join(guesslist)
    else:
        print ''.join(printlist) + ''.join(guesslist[rightcounter:])
    time.sleep(.030)




