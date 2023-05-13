from numpy import array
from rooms import Rooms, MOVEMENT, r
import pickle
actions = ("quit"
           "save"
           "load"
           "take"
           "use"
           "move")
class Player():
    def __init__(self):
        self.position = (0, 0, 0)
        self.inventory = []
        self.name = input("What will your adventurer's name be?\n")
        print(f"Welcome brave adventurer, {self.name}")
        @property
        def position(self):
            return tuple(self.__position)
        @position.setter
        def position(self, new):
            self.__position += new
def valid_input(prompt = "What will you do next adventurer?"):
    print("COMMANDS")
    response = None
    while response not in actions:
        print(f"ACTIONS:\n{actions}")
        response = input(prompt).lower()
    return response
def save():
    with open('game.dat','wb') as f:
        pickle.dump(player,f)
        pickle.dump(rooms,f)
    print(f"Game saved!")
def load():
    global player
    global rooms
    try:
        with open('game.dat','rb') as f:
            player = pickle.load(f)
            rooms = pickle.load(f)
        print(f"Game loaded!")
    except FileNotFoundError:
        print(f"Game file not found!")
player = Player()	    
def main(player):
    choice = None
    while choice != "quit":
        room = MOVEMENT.get(player.position, "Invalid room setting - something broke")
        print(r.description())
        choice = valid_input()
        if choice == "quit":
            print("Thanks for playing!")
        elif choice == "save":
            save()
        elif choice == "load":
            load()
        elif choice == "take":
            room.get_item(player)
        elif choice == "use":
            room.use_item(player)
        elif choice == "move":
            room.move(player)
if __name__ == "__main__":
    main(player)