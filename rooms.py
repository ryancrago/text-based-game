from numpy import array
MOVEMENT = {"north":array([0,1,0]), "south":array([0,-1,0]), "east":array([1,0,0]), "west":array([-1,0,0]), "up":array([0,0,1]), "down":array([0,0,-1])}

class Room():
    '''Room Object'''
    def __init__(self):
        self.room_items = []
        self.usable_items = {}
        self.allowed_movements = []
        self.descriptions = {}
    def get_item(self, player):
        '''get an item from the room to the player's inventory'''
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
        '''use item from player's inventory'''
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
        '''ask the player where they would like to move'''
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