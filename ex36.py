def room_1():
    print "You are now in room one!"
    print "Do you want to live or die?"

    while True:
        choice = raw_input('> ')
        if "live" in choice:
            print "I'm jealous of your will to live!"
            exit(0)
        elif "die" in choice:
            print "Ah yes, the sweet release of death."
            exit(0)
        else:
            print confusion()


def room_2():
    print "You are now in room two!"
    print "Is this room cool or fun?"

    while True:
        choice = raw_input('> ')
        if "cool" in choice:
            print "Ice cold, baby!"
            exit(0)
        elif "fun" in choice:
            print "What about this seems fun to you?"
            exit(0)
        else:
            print confusion()

def start_room():
    print "Welcome to pointless decision game!"
    print "Would you like to go to room 1 or 2"

    while True:
        choice = raw_input('> ')
        if "1" in choice or "one" in choice:
            room_1()
        elif "2" in choice or "two" in choice:
            room_2()
        elif "exit" in choice:
            print "Later!"
            exit(0)
        else:
            print confusion()

def confusion():
    return "I don't know what that means, dude."

start_room()
# Test commit