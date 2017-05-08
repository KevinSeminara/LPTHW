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


class Death(Scene):

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

        while guesses <10 :
            print "WRONG!"
            guesses += 1
            guess = raw_input("[keypad]> ")

            if guess == code:
                print "Wow you guessed the code"
                print "You can proceed!"
                return 'the_bridge'
            elif guess == "hint":
                print code
            else:
                print "The bomb explodes and you are dead"
                return 'death'



class TheBridge(Scene):

    def enter(self):
        print "You are now on The Bridge!"
        print "There is a bomb! oh no!"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "it goes off"
            return 'death'
        elif action == "slowly place the bomb":
            print "It worked!"
            print "Now we can leave!"
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You are now surrounded by escape pods"
        print "There are 5 escape pods"
        print "Which one do you take"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")

        if guess != good_pod:
            print "You chose pod %s" % guess
            print "That pod exploded!"
            return 'death'
        elif guess == "hint":
            print good_pod
        else:
            print "You've escaped and won!"
            return 'finished'
class Finished(Scene):

    def enter(self):
        print "You are the best!!!!!!!!!"

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game= Engine(a_map)
a_game.play()