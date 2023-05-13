from numpy import array
MOVEMENT = {"north":array([0,1,0]), "south":array([0,-1,0]), "east":array([1,0,0]), "west":array([-1,0,0]), "up":array([0,0,1]), "down":array([0,0,-1])}
#test
class Room():
    def __init__(self):
        self.room_items = []
        self.usable_items = {}
        self.allowed_movements = []
        self.descriptions = {}
    def get_item(self, player):
        if self.room_items:
            pick = input(f"What item would you like to 'get'?").lower()
            if pick in self.room_items:
                print(f"You pickup the {pick}.")
                player.inventory.append(pick)
                self.room_items.remove(pick)
            else:
                print(f"Couldn't find {pick} in room.")
        else:
            print(f"There's nothing to pick up here!")
    def use_item(self, player):
        if player.inventory:
            print(f"Your inventory:\n{player.inventory}")
            pick = input(f"What item would you like to 'use'?").lower()
            if pick in player.inventory:
                if pick in self.usable_items:
                    print(self.usable_items[pick])
                    player.inventory.remove(pick)
                    del self.usable_items[pick]
                    self.special(pick)
                else:
                    print(f"You can't use {pick} here.")
            else:
                print(f"You don't have {pick} in your inventory.")
        else:
            print(f"You don't have anything in your inventory to 'use'!")
    def move(self, player):
        print(f"You can go in the following directions:\n{self.allowed_movements}")
        direction = input("Which direction would you like to 'move'?")
        if direction in MOVEMENT:
            if direction in self.allowed_movements:
                print(f"You move {direction}.")
                player.position = direction
            else:
                print(f"You can't move {direction} from here.")
        else:
            print(f"'{direction}' isn't a valid direction")
    def description(self):
        key = tuple(self.room_items), tuple(self.usable_items)
        return "\n\n"+self.description.get(key, "Invalid room setting - something broke")
    def special(self, thing):
        if thing == 'key':
            self.allowed_movements.append('down')
Rooms = {}
#spawn
r = Room()
r.room_items.append('Rusty Key')
r.usable_items['Torch'] = "The torch sure burns bright."
r.allowed_movements.append('south')
r.descriptions[(('Rusty Key',),('Torch'))] = "A seemingly locked door. But it's too dark to find the lock."
r.descriptions[(('Rusty Key',),())] = "The lock has shown itself. For some reason it's in the bottom left corner."
r.descriptions[((),())] = "The door has opened you can now move 'south'."
Rooms[(0,0,0)] = r
#Room 1
r = Room()
r.room_items.append('Torch')
r.usable_items['Old Book'] = "An old book, perhaps you should return it to it's bookshelf."
r.allowed_movements.append('west')
r.allowed_movements.append('north')
r.descriptions[(('Old Book'))] = "There is a bookshelf that seems to be missing a book."
r.descriptions[((),())] = "The book shelf has moved to the side, you can now move 'west'."
Rooms[(-1,0,0)] = r
#Chest Room
r = Room()
r.room_items.append('Torch')
r.usable_items['Wooden Cross'] = "A wooden cross. You have no idea what this could be used for."
r.allowed_movements.append('east')
r.allowed_movements.append('down')
r.descriptions[(('Torch',),('Wooden Cross'))] = "There are stairs that lead to a dark corridor. Maybe there are more clues there?"
r.descriptions[(('Wooden Cross,'),())] = "After lighting up the corridor you notice a cutout in the shape of a cross."
r.descriptions[((),())] = "The door to the next room has been opened. You can now move 'down'."
Rooms[(0,0,-1)] = r
#Tomb
r = Room()
r.room_items.append('Torch')
r.usable_items["Mummy's key"] = "This key is made out of Mummy cloth. Perhaps it opens the door to the treasure?"
r.allowed_movements.append('up')
r.allowed_movements.append('north')
r.descriptions[(("Mummy's key"))] = "You find a door that is covered in cloth with a lock on it."
r.descriptions[((),())] = "When the door opens the cloth all decays. This includes the key. You can now move 'north'."
Rooms[(0,1,0)] = r
#Treasure Room
r = Room()
r.allowed_movements.append('south')
r.descriptions[((),())] = "Congratulations! You found the sacred treasure!"
Rooms[(0,1,0)] = r