items = ['A rusty Sword','Gold Coin','Diamond']
monsters = ['Ogre','Troll']
treasure = []
rooms = [
    {'N':1,'S':2,'E':3,'W':4,'description':'A big room light by candles','items':[0]},
    {'S':0,'description':'A big small dark room','monsters':[0]},
    {'N':0,'description':'A brightly lit room','items':[1]},
    {'W':0,'description':'A dim cellar','monsters':[1]},
    {'E':0,'description':'A small room - with a sky light','items':[2]},
]

current_room = 0
inventory = []

def move_room(inst, room):
  if inst in rooms[room]:
      return rooms[room][inst]
  else:
    return -1

def look(room):
        print('You can see')
        for m in rooms[room].get('monsters',[]):
            print(monsters[m])
        for i in rooms[room].get('items',[]):
            print(items[i])
        if (len(rooms[room].get('monsters',[])) + len(rooms[room].get('items',[]))) == 0:
            print('Nothing')

def transfer(from_, to_, prompt, error):
  if len(from_) != 0 :
    print(prompt)
    show_inventory(from_)
    while True:
      xfer = input('Choose >')
      if int(xfer) >= 0 and int(xfer) < len(from_):
        to_.append(from_[int(xfer)])
        del from_[int(xfer)]
        break
      else:
        print('Cannot do that ... ')
  else:
    print( error )

def show_inventory(inv):
    for index, i in enumerate(inv):
        print(str(index), items[i])

while True:
  print(rooms[current_room]['description'] + "\n")

  while True: #instruction loop

    instruction = input('>')

    if instruction == 'QUIT':
      exit()

    # Movement
    if instruction in 'NSEW':
      new_room = move_room(instruction, current_room)
      if new_room == -1:
        print('You cannot move that way\n')
      else:
        current_room = new_room
        break

    # Look instruction
    if instruction == 'LOOK':
      look(current_room)

    # Pick up something - if there is something to pick up
    if instruction == 'PICK':
      transfer( from_ = rooms[current_room]['items'],
                to_ = inventory,
                prompt='Pick up what ?',
                error='Nothing to pick up')

    # Pick up something - if there is something to pick up
    if instruction == 'DROP':
      transfer( to_ = rooms[current_room]['items'],
                from_ = inventory,
                prompt='Drop what ?',
                error='Nothing to drop')

    #Inv instruction
    if instruction == 'INV':
      show_inventory(inventory)
