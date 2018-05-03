# -*- coding: utf-8 -*-

import time


def reader(x):
    """Provides pretty output for the player. Works as a narrator, that shows
    lines piece by piece."""
    x = str(x)
    count = 0
    prettyline = ""
    for i in x:
        # Add to output
        prettyline += i

        # Count whitespaces
        if (i == " "):
            count += 1

        # Print after some whitespaces and clear output variable
        if (count == 8):
            print(prettyline)
            prettyline = ""
            count = 0
            time.sleep(2)
        # TODO !!! PRINT REST after last chunk !!!
    print(prettyline)


def savelvl(lvl):
    F = open("C:\\Users\\Kabibubi\\workspace\\A_Journey_East\\levels\\level.txt", "w")
    F.write(lvl)
    F.close()


def loadlvl():
    F = open("C:\\Users\\Kabibubi\\workspace\\A_Journey_East\\levels\\level.txt", "r")
    lvl = F.read()
    print(lvl)


def riddle(qstn, solutions):
    """Asks a riddle. qstn is the riddle, solutions a list of possible
    anserws. solutions must be all lowercase without whitespaces."""
    print(qstn)
    answ = input("Wie lautet deine Antwort?\n")
    nansw = answ.lower()
    nansw = nansw.replace(" ", "")
    nansw = nansw.replace("der", "")
    nansw = nansw.replace("die", "")
    nansw = nansw.replace("das", "")
    nansw = nansw.replace("ein", "")
    nansw = nansw.replace("eine", "")
    nansw = nansw.replace("einer", "")
    if (nansw in solutions):
        print("Richtig!")
    else:
        print("Falsch..." + nansw + " ist nicht richtig")


riddle("""Lös mir das:\nWas wiegt weniger als die leichteste Feder?
Und doch kann kein Mensch es länger als ein paar Momente halten.""", ["atem",
"luft"])