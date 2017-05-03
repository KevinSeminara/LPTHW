class GameConsole(object):
    hdmi = True
    pass

class Playstation(GameConsole):

    def __init__(self, bc):
        self.bc = bc

    def speak(self):
        print "I am a playstation!"

class Xbox(GameConsole):

    def __init__(self, bc):
        self.bc = bc

PS4 = Playstation(False)

Xbone = Xbox(True)

print "Xbox's bc is: %s" % Xbone.bc

PS4.speak()
Xbone.hdmi = False
print Xbone.hdmi
print PS4.hdmi
