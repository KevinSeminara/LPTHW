from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


def Death(Scene):

    quips = [
        "You died. Sorry!",
        "Too bad that you are dead.",
        "Good bye cruel world"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "You are in the Central Corridor"
        print "An enemy jumps out in front of you!"
        action = raw_input("shoot or run?> ")

        if action == "shoot":
            print "You miss because you're a bad shot"
            return 'death'
        elif action == "run":
            print "He lunges at you but misses, you leave quickly"
            return 'laser_weapon_armory'
        else:
            print "Does not compute!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You are now in the Laser Weapon Armory!"
        print "There is a bomb"
        print "You only have 10 guesses"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses <10:
            print "WRONG!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "Wow you guessed the code"
            print "You can proceed!"
            return 'the_bridge'
        else:
            print "The bomb explodes and you are dead"
            return 'death'



class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game= Engine(a_map)
a_game.play()