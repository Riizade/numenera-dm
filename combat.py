import json

class Actor:
    name = "Unknown"
    health = 0
    max_health = 0
    status = "None"
    notes = ""

    def boardline(self):
        return name[0:16]+"\t"+str(health)+"/"+str(max_health)+"\t"+status+"\t"+notes 

class NPC(Actor):
    damage = ""
    armor = ""
    movement = ""
    modifications = []
    motive = ""

class Board:
    Combatants = []

# returns a formatted combat line of an actor
def boardline(actor):
    strings = []
    strings.append(pad(actor.name, 16))
    strings.append(pad(actor.health+"/"+actor.max_health, 7))
    strings.append(pad(actor.status, 12))
    strings.append(pad(actor.notes, 20))
    return "\t".join(strings)

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

# input loop
while True:
    cmd = raw_input("Enter a command:\n")

    inputs = cmd.split(" ")
    if cmd[0] == "exit":
        exit(0)
    elif cmd[0] == "help":
        print_help()
    else:
        print("Unknown command "+cmd[0])
