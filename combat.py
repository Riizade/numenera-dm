import json

class Actor:
    name = "Unknown"
    health = 0
    max_health = 0
    status = "None"
    notes = ""

    # returns a formatted combat line of an actor
    def boardline(self):
        strings = []
        strings.append(pad(self.name, 16))
        strings.append(pad(self.health+"/"+self.max_health, 7))
        strings.append(pad(self.status, 12))
        strings.append(pad(self.notes, 20))
        return "\t".join(strings)

class Combatant(Actor):
    damage = ""
    armor = ""
    movement = ""
    modifications = []
    motive = ""
    loot = ""

class NPC(Combatant):
    history = ""
    occupation = ""
    location = ""
    faction = ""
    disposition = ""
    tone = ""


class Board:
    Combatants = []

# returns a new s that is n characters long, truncated or padded as needed
def pad(s, n):
    l = len(s)
    if (l > n):
        return s[:n-1]
    if (l == n):
        return s
    if (l < n):
        return s+" "*(n-l)

def print_help():
    print("You're on your own.")

def open_actor(filename):
    extension = filename.split('.')[-1].lower()
    if extension == 'npc':
        # open as NPC
        pass
    elif extension == 'pc':
        # open as PC
        pass
    elif extension == 'enc':
        # open as Board
    else:
        print("Unknown filetype ."+extension)

def main():
    # instantiate environment

    # input loop
    while True:
        cmd = raw_input("Enter a command:\n")

        inputs = cmd.split(" ")
        if inputs[0] == "exit":
            exit(0)
        elif inputs[0] == "help":
            print_help()
        else:
            print("Unknown command "+inputs[0])

if __name__ == "__main__":
    main()