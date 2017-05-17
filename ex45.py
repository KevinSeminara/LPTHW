import random
import time

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

inputword = raw_input('Enter word> ')
#inputguess = raw_input('Enter guess> ')
rightcounter = 0

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
    time.sleep(.015)




