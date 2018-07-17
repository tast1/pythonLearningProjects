



def StartScene():


    Name = input("What is ur name stranger?")

    print(Name , "Welcome")

    Play = input("Wanna play?").upper()

    if Play == 'Y':
        print("LETS PLAY THE GAME")
        GameBegins()
    if Play == 'N':
        print("Oh... I see, lets se how strongly you dont want to play my game....")
        StartScene()

    while Play != 'Y' and Play != 'N':
        Play

def prompt():
    x = input("Type a command: ")
    return x

def GameBegins():

    print("I am going to ask you some questions, you are going to answere as best you can.")
    Understand = input('''
        *
        * Do you understand the rules ?
        *Yes or NO ''').upper()
    if Understand == 'Y':
        print("Nice you have come this far. Lets see how long u last. ;) ")
        RoudOne()
    if Understand == 'N':
        print("Thats to bad....Lets see if you get it this time....")
        StartScene()
    elif Understand != 'Y' and Understand != 'N':
        GameBegins()

def RoudOne():

    print('''
        **********WELCOME*************
        **********TO******************
        **********THE*****************
        **********MOST****************
        **********INTERSTING**********
        **********GAME****************
        **********YOU*****************
        **********WILL****************
        **********EVER****************
        **********PLAY****************

        ''')
    print('''
                ***QUESTION 1***
        ''')
    print ('''
                What is the Exalibur ?

                ***Options***
                1 A boat
                2 A Roman title.
                3 A Sword.
                4 A Spaceship.

                ''')

    command = prompt()
    if command == '3':
        print("Wow...You have given the correct answere.")
        Question2 = input("Are u ready for the next question? Y/N").upper()
        if Question2 == 'Y':
            RoundTwo()

        if Question2 == 'N':
            print("You are doing so good....But oh well..")
            GameOver()

    if command == '1':
        GameOver()

    if command == '2':
        GameOver()

    if command == '4':
        GameOver()

def GameOver():

    print("YOU LOST....")
    PlayAgain = input('''

        DO YOU WANT TO PLAY AGAIN?

        ''').upper()
    if PlayAgain == 'Y':
        StartScene()
    if PlayAgain == 'N':
        print("Haha dont give up so easy thats no fun...")
        print('''

            ________
 /  _____/_____    _____   ____     _______  __ ___________
/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \
\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/
 \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|
        \/     \/      \/     \/                   \/


''')

StartScene()
