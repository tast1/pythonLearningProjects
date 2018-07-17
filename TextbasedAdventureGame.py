import random
import math
from tkinter import *
from tkinter import ttk



PrisonCellDoorOpen = False




def SetScene():
    print('''
            ****************************************
            *                                      *
            *  Welcome to a Noobs python adventure *
            *                                      *
            ****************************************
                                                    ''')

    RightKey = 12
    print("You have awoken inside a priosn cell, you can not recall how or when you have arrvice")
    input("Press enter to continue the intro")
    print("You have apperently been here for a while, and cant recall the last time you have eaten, you feel ur stomach crumpeling in hunger.....")
    print("Inside the prison cell you can only see A toilet, a sink with a broken mirrior above it. And a small window with bars going across it.")


    Lookarround = input("Do you want to look arround you, and see if you can figure something out ? Y/N").upper()
    if Lookarround == 'Y':
        choice1or2 = input("Do you want to look at the window 1, or do you want to look at the sink with the broken mirror2")
        if choice1or2 == '1':
            print("U apporach the Window")
            print("You look out thrugh the small gap in the window, u cant see much, its pitch dark outside...")

            GoToSink = input("Do you want to go to the sink with the broken mirror? Y/N").upper()
            if GoToSink == 'Y':
                choice1or2 == '2'
            if GoToSink == 'N':
                print("You continue to stear out the window.")
        if choice1or2 == '2':
            print ("U approach the sink with the broken mirror.")
            Mirror = input("You can now see that the mirror is cracked... Maybe you can break a pice loose? Y/N").upper()
            if Mirror == 'Y':
                ChanceForMirror = random.randint(0, 1)
                if ChanceForMirror == 1:
                    print("You managed to get a pice of the mirror loose, you now have a makeshift weapon!!")
                    print("You hear a guard approaching......")
                    Guard1 = input("Do you want to try to lure the guard, or do you want to pretend that you are asleep? 1/2")
                    if Guard1 == '1':
                        print("The guard approaches the cell, and as he gets closer. You can hear the ristteling of the keys to your freedom...")
                        print("You now see the shaddow of the guard beeing cast in the hallway, by the torches light in the end of your cell's corridor.")
                        Guard1Distance1 = input("The guard is close, do you want to wait. Or do you want to draw his attention now? Y/N?").upper()
                        if Guard1Distance1 == 'Y':
                            print("you have called on the guard...")
                            print("The guard looks at you and have a grim smile accross his face... He asks if you finaly have decided to wake up.")
                            TimeInCell = input("Ask the guard how long you have been here Y/N").upper()
                            if TimeInCell == 'Y':
                                print("You ask me ?....You have been here for a goodwhile.")
                                print("The guard approches ur cell even closer, almost as he wants to get a good view of your face, as the information settles in.")
                                Attack1 = input("The guard is very close now, you can almost certainly grap him. Do you want to try to kill the guard with ur pice of glass? Y/N").upper()
                                if Attack1 == 'Y':
                                    print("U launch ur self att the guard, streching out your hand between the bars, and you get a firm grip on his jacket...You pull him towards your cell bars with all the strength you can muster....")
                                    print("The guard looks shocked for a secound, as his brain dont fully understand whats going on. As he slowly realices that you want to harm him, he starts strugeling back. The guard reaches for his sword....")
                                    Trought_Attack = input("You see the guard reaching for his sword, you need to try to cut his trought now, or it might be urs thats getting opend...Y/N").upper()
                                    if Trought_Attack == 'Y':
                                        print("U get ur other hand trough holding the pice of mirror, u can feel it cutting ur hand open, as u press on it so you dont loose it. You manage to pull the guard closer to you in a final attempt. You have managed to get a good hold on him and u lunge at his trought with the pice of mirror.")
                                        print("You can feel something hot and whet arround ur fingers...And you can hear the guard gurgeling for air, as his heart keeps bumping more and more blood out the gaping whole in his throught...You think for ur self, how much blood is inside one man ? The blood quickly starts making its way down the halway where he came from, finnling in the cracks in the floor.")
                                        SearchGuard2 = input("Search the body guard? Y/N ? ").upper()
                                        if SearchGuard2 == 'Y':
                                            ##This dont work as intended.... No mather what key I use, The door opens...
                                            print("You found a Keychain with 12 keys....")
                                            EscapeCell = input("Do you want to try to open your prison cell door? Y/N").upper()
                                            if EscapeCell == 'Y':
                                                PickKey = input("You try to find the right key for your door. There is 12 keys pick one").upper()
                                                if PickKey is RightKey:
                                                    TryAnotherKey = ("You have selectec the wrong key, try another. U just tried key")
                                                if RightKey == 12:
                                                    PrisonCellDoorOpen = True
                    if Guard1 == '2':
                        print("You hear the guard talking, but u have no idea how he is talking to. Maybe he is talking to him self, as you have heard countless other board guards to. When they are left to them slefs for long houers, watching beaten up men inside prison cells. As when you come to think of it, you havent heard any other prisoners since you awoke. Are you the only one in here? That cant be, that would be silly if you where the only one in the whole corridor of this prison....")
                        print("But you are left to wounder, and reflect about the past events leading you to end up here... Its almost as the loss of memory seems a bit to convinient. Maybe you have been hit in the head?")
                        Head_examination1 = input("Do you want to examin your head, and try to feel if u can find a wound on ur head? Y/N").upper()
                        if Head_examination1 == 'Y':
                            print("You slowly start examening your head with your finger, slowly so you dont accidentely cause ur self paint by sticking ur fingers inside a wound. You cant feel anything in the front of ur head and face. You slowly start to drag your fingers across your hair, as you where combing your hair...")
                            print("You think to ur self, this must look redicolus if some one saw you. Standing inside a prison cell and combing ur own heair with ur fingers, as you have done many a times on the docs, afther loading and unloading heavy cargo from all the far corners of the world.... Then All of a sudden, u feel something wierd as your fingers made theyr way to the spot. Most elderly men have a bold patch, often refered to as a 'moon', the hair there give away in unatruall manner, as you feel as tough the hair is attached to loose chucnk of scalp... As you feel arround the back of ur head, you feel like some one tried to scalp you, but failed to do so. Only a small pice of flesh is holding it on place, and you feel with ur fingers down in the gaping wound, then all of asudden ur finger tips meets something hard. A strange feeling you did not anticipate, it sends shivers down your spine.. as you realice you are tuching your own skull, there is no longer any felsh and skin or hair. Between your fingers and your scull......")
                            Fingerandscull = input("You quickly realice that this cant bee good, you need to assess the damage... Do you want to try using the mirror to get a bether view of the wound ? Y/N").upper()
                            if Fingerandscull == 'Y':
                                print("You stand infront of the broken mirror, that now have cracks along the the whole mirror, afhter u managed to pull apice loose.")
                                InspectHead = input("You cant get a good view of your wound, naturally since ur eyese are on the oposite side...But you have a pice of the mirror, maybe you can allinge it so you can see the back of your head? Y/N").upper()
                                if InspectHead == 'Y':
                                    print("You try alligning the pice of mirrir u have, so it refeclts the wound to the mirror...You finally manage to get a good view, and you quickly realice that its only beeing held togeather by a tiny layer of skin. It looks like it hatched out by a axe, or maybe a polearm with a heavy blade...")
                                    print("You think to your self, how in gods name did you manage to get ur self in a situvation where you have been attacked with such weapons, and how lucky you have been... if the blade had been tiny pit to the right, you certanly would have been dead. ")
                                    TreathHeadWound = input("You are struck by a stragne feeling that you are entagled in something, you have no understanding of. And no mather the mangnitude severity of the actions leading you here. You have most likely been attack by a sate officall, as they are the once with polearms with heavy sharpend metall at the end. You need to do something about the wound on ur head. Do you want to make a makeshift bandage with ur thsirt , just so you can hold the loose scalp in place.1 Or do you want to cut it of. 2 1/2").upper()
                                    if TreathHeadWound == '1':
                                        print("You take of your shirt.")
                                        MakeHeadWrap = input("Do you want to use the pice of mirror to cut the shirt? Y/N").upper()
                                        if MakeHeadWrap == 'Y':
                                            print("You carefully cut the thishirt into long smaller pices, so you can wrap it arround ur head.")
                                    if TreathHeadWound == '2':
                                        print("U take a hold of ur loose scalp in one hand, and the pice of mirror in the other......")
                                        CutOffScalp = input("Are you really sure this is the best option? What do you do if you manage to get out of here? are you going to live with a gaping whole on the top of ur head for the rest of your life? Y/N").upper()
                                        if CutOffScalp == 'Y':
                                            print("You draw a deep breath of air as you make your self ready to cut it of...")
                                            print("You hear a deep voice comming from whitin the corridor hallway. HAVE YOU LOST YOUR SENCES MAN ? You quickly turn arround,looking to find the source of the voice... When you turn arround there is no guard looking into your cell, you look arround somewhat confused...You hear the voice once more. I am over here you donkey. You now hear that the voice comes from the farwall in your cell, there is a brick missing. ")
                                            DialogOldMan1 = input("Do you approach the voice from wall? Y/N").upper()
                                            if DialogOldMan1 == 'Y':
                                                print("The voice once more speaks, but this time more softly. So you are looking to finish the deed the royal guards men wherent skilled enough to finish? ")
                                                DialogOldMan2 = input(" 1 ask the fellow prisoner what he knows of your enprisonment. 2 ask the fellow prisoner how long he has been observing you. 3 Ask the fellow prisoner if he dont have anything else bether to do, then to watch you....").upper()
                                                if DialogOldMan2 == '1':
                                                    print("You dont recall anything? You are most fortunate I tell you...")
                                                    DialogEmprisonment2 = input(" Ask the prisoner who he is, and why he thinks he can judge your fortune by loosing all recolection of the past events? Y/N ").upper()
                                                    if DialogEmprisonment2 == 'Y':
                                                        print("Well well, would you look at that... You have absolutely no memory of how you ended up here you say. Well the story aint sunshine and rainbows, let me tell you that much.")
                                                        DialogEmprisonment3 = input(" 1 Was it really that bad? 2 Ask the man to tell you what you ask him, you have no memory what so ever, and are only left with a unsetteling feeling sending shivers down ur spine. 3 Ask the man who he is, and why he ended up in here.")
                                                        if DialogEmprisonment3 == '2':
                                                            print("Okey okey... No reason to get all tangeld up, its not like we are going anywhere soon, neither are the hangmans noose waiting for us upon the houer of dawn. We are damed men we are, Ill tell you as it is..")
                                                            print("We are here becuae we got tangeled up in some business that did not take well to sunlight, one might say... We where working on the docs, unloading some cargo from a ship far away. Some distante corner spices of all flavors, some sweet as a summer bride. Some bitter as a infants diper... We worked in due haste, and where about to unload one of the last boxes, when the rope snaped. Once the boxe hit the ground, it splintered into smithereens... Inside the box there where something i never seen before, it was a triangle shaped stone, carved with all kinds of wierd symbols... Some repreesenting humans with head of dogs. It was quiet a sight ill tell you. But none the less, the captain mayde the biggest of fuzzes about it, started yelling commands, and soon the crew where quick to cover it up and getting it inside a new box. We where soon threatend to great pain and suffering if we as much as mentioned what we saw.")
                                                            print("They where soon to get the thing aboard the ship again, and set sail as they where hunted by the flying Dutchman. Word must have spread quickly, because we where soon joined by royal guards men. They started asking questions we could not anwere... Afther we started explaining what happend. A smoke bomb whent of and guards started shouting and waiving theyr weapons arround, as they where certain they where getting attacked. You must have gotten hit by one of the guards weiving theyr polearms in blindes. I was struck accorss the back and feel to my knees. Then they brought us here....")
                                                            DialogEmprisonment4 = input("1 So you are telling me I am here because some one had a big triangle made of stone with markings on it ? 2 This is a joke right?")
                                                            if DialogEmprisonment4 == '1':
                                                                print("Yes... I am affraid so, the guards seemed rather interested in the triangle... So i guess there must be something special bout this here triangle. I must say that I have never quiet seem something like it. And I have seen some strange things in my days. Its no question that something is special about it. The once how had it, hid it and the guards where also interested... And then there is the smoke bomb... I certain this was no coincedence, as soon as we told them it happend...")
                                                                print("What it going on....? triangles....markings? Humans with dog heads? Has this man gone insane?..... How ever you dont think he is joking or making it up. For some reason it sounds familiar. ")
                                                                GuardEncounter1 = input("You hear footsteps in the halway..... It's certain to be one of the guards. #1 Try not to attract the guard. #2 Yell on the guard. #3 Ask the fellow prisoner what they should do.")
                                                                if GuardEncounter1 == '1':
                                                                    print("Let's be quiet for while yes? The voice form the other side of the wall is no longer there, as it was never some one on the other side.")
                                                                if GuardEncounter1 == '2':
                                                                    print("You call on the guard....")
                                                                    GuardEncounter2 = input("The guard approches, you can see he is looking at you like you where nothing more than a mouse... #1 Ask the guard why you have ended up in here. #2 Ask the guard for food. ")
                                                                    if GuardEncounter2 == '1':
                                                                        print("The guard looks at you with a grim smile accross his face. Well Well you have quiet a meeting to look forward to inmate. You seem to have tangeld your self up in something the higher ups are werry interested in getting theyr hands in. I must addmit i wounder how a nobody like you got involved in these mathers.... The guard comes closer to the cell... looking at you mokingly as he wants to see if your sceard by the news...")
                                                                        AttackGuard = input("The guard is so close you are certain you can reach him trough the bars, You Still have your pice of the mirror. Its by no means a good weapon, but it will do... Do you want to reach for the guard and try to slit his trought? Y/N").upper()
                                                                        if AttackGuard == 'Y':
                                                                            print("You launch your self at the guard, the guard just stands there somewhat shocked by your actions. This is all the hesitation you needed. You now have a firm grip arround the guards jacket. The guard still dont quiet understand whats happening, but he starts to realise that he is in danger. He starts to fight back, but soon realise the he must go for his sowrd.")
                                                                            Slittrought = input("You see the guard reaching for his sword, and realise you have to go for it now. Do you want to go for it now ? Y/N")
                                                                            if Slittrought == 'Y':
                                                                                print("In a final struggle u attempt to draw the guard closer to the bars in ur cells. You manage to pull him close. In your other hand you hold the pice of the mirror, your fingers are squeesing around it. You can feel the mirrror cutting into ur fingers, but it dosent maher. If you drop it now, its over....You start feeling a something whet and hot running accross ur hand, and you start hearing the guard gasping for air, as the hearth keeps pumping harder and harder, and the blood poors out of his gaping wound in the trought. The guard quickly falls down and no longer uther a sound....")
                                                                                SearchGuard = input("You have killed the guard. Do you want to search the body of the guard. Y/N")
                                                                                if SearchGuard == '1':
                                                                                    print("U search the body, and you find keys!!!")




                                                                if GuardEncounter1 == '3':
                                                                    print("The guards never usally wants anything else than make it harder for every one, they dont want to be her, and can do what they want...")


                                        if CutOffScalp == 'N':
                                            print("You must have lost ur sences... what where u thinking???")



                if ChanceForMirror == 0:
                    print("Oh... u have cut ur self on the sharp glass...")
                    print("You need to stop the bleeding, or else you might not make it")
                    MakeBandage = input("You can use ur thsirt as a makeshift bandage, it might get cold Y/N")
                    if MakeBandage == 'Y':
                        print("You take your tshirt of, and tear it into smaller pices and wrap it arround ur hand.")
                    if MakeBandage == 'N':
                        print("You need to use soemthing else then....")
    if Lookarround == 'N':
        print("Are you just going to subcome to your situvation, and not try to get out ?")
        input("......")


SetScene()

def EscapePrisonCell():
    if PrisonCellDoorOpen == True:
        print("You have gotten our of the cell.... WHAT NOW ??")


EscapePrisonCell()
