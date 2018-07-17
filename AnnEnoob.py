

import random
import tkinter
from tkinter import *
from tkinter import ttk

def prompt():
    x = input("Type a command: ")
    return x


def __str__(self):
    return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        ##self.location_x, self.location_y = world.starting_position
        self.victory = False

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

class Item():
    ##The base class for all items##

    def __int__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value




class ViewInvetory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name="ViewInvetory", hotkeys='i')

def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

class Gold(Item):
    def __init__(self):
        self.amt = amt
        super().__init__(name="Gold",
                        description="A round coin with {] Stamped on the font of it.".format(str(self.amt)),
                        value=self.amt)

def startScene():
    print('''

        ************************
        *******WELCOME**********
        ************************

        ''')
    Name = input("What is ur name traveleer ? ")
    print("Welcome", Name)
    StartGame = input("Do u want to start the game ?").upper()
    if StartGame == 'Y':
        StartGameScene()
    if StartGame == 'N':
        startScene()


def StartGameScene():

    print('''

        Options
        1 Look arround
        2 inventory

        ''')
    command = prompt()
    if command == '2':
        ViewInvetory()

startScene()
