import random
import math
from tkinter import *
from tkinter import ttk

IsTitleShowen = False

def PrisonCellScene():
    if IsTitleShowen == False:
        print('''
            ****************************************
            *                                      *
            *  Welcome to a Noobs python adventure *
            *                                      *
            ****************************************
                                                    ''')
    global gold
    gold = 2
    global health
    health = 10
    global energy
    energy = 10
    global mele
    mele   = 10
    global ranged
    ranged = 0
    global fullhealth
    fullhealth = 10
    global attacksum
    attacksum = 10
    global MakeshitWeapon
    makeshift = 0

    print('''
        Options
        1 look inside ur prison cell
        9 Stats
            ''')
    command = prompt()
    if command == '1':
        PrisonCell2()
    elif command == '9':
        Stats()



def Stats():
    print('''
        ************''')
    print(gold)
    print(health)
    print(mele)
    print(energy)
    global ranged
    if ranged > 0:
        print("Ranged", ranged)
        print ("ammo", Ammo)
    PrisonCellScene()


def prompt():
    x = input("Type a command:")
    return x




    #### Different scenes###

def PrisonCell2():
    print("****************************************")
    print('''
You are in your prisoncell. You see a sink with a broken mirror, and a window.
    ''')
    print('''Options:
1. Inspect window
2. Inspect the sink with the broken mirror
3. Do nothing
9. Stats
10. Go to title screen
''')

    command = prompt()
    if command == '1':
        CellMirror()
    elif command == '2':
        SinkAndMirror()
    elif command == '9':
        Stats()
    elif command == '10':
        PrisonCellScene()
    else:
        PrisonCell2()



def CellMirror():
    print("You see a sink, not sure if you even can call it that. But u also seea borken mirror.")
    print('''Options:
        1. Inspect the broken mirror
        2. Inspect the sink
        3. Go back
        ''')
    command = prompt()
    if command == '1':
        print("U look at the broken mirror, you might be able to break a pice of the mirror loose")
        print('''Options
            1. Try to break a pice of the mirror free.
            2. Go back
            ''')
        command = prompt()
        if command == '1':
            Success = 1
            if Success == 1:
                print("You have broken a pice of the mirror off, and you now have a makeshift weapon!!!")
                PrisonGuardEncounter()
                print(Stats)
            if Success == 2:
                print("U are bleeding pretty badly..")
                print('''Options
                    1. Make a improvised bandage with ur tshirt
                    2. Dont do anything
                    ''')
                command = prompt()
                if command == '1':
                    print("You have taken of our tshirt and wrapped it arround ur hand.")
                    print(''' Options
                        1 Return bacn to your prison cell.
                        2 Try getting a pice of the mirror lose again..
                        ''')
                    command = prompt()
                    if command == '1':
                        PrisonCell2()
                elif command == '2':
                    CellMirror()

def CellSink():
    print("There is a sink, its not a sink but still a sink...")
    print(''' Options
        1 See if u can find anything.
        2 go back
        ''')
    command = prompt()
    if command == '1':
        print("You look at the obomination of a sink, there is nothing here, the sink nothing more than bucket stuck in the wall.")
        print('''
            Options
            1 go back
            ''')
        command = prompt()
        if command == '1':
            CellSink()
    if command == '2':
        PrisonCell2()
    else:
        PrisonCell2()

def PrisonGuardEncounter():
    print(''''You hear a guard apporaching ur cell.....
        Options
        1 Lure the guard to your prison cell?
        2 Pretend to be asleep.
            ''')
    command = prompt()
    if command == '1':
        print('''The guard approhes the cell, and as he gets closer. You can hear the ritteling of the keys to your freedom...
            You see the shaddow of the guard beeing casted in the halawy, but the torched lighting up the end of your cells corridor
                        ''')
        command = prompt()
        if command == '1':


PrisonCell2()


