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
    def move(self, move):
        self.position = tuple(array(self.position) + MOVEMENT.get(move, array([0,0,0])))

player = Player()	    
def main(player):
    choice = None
    while choice != "quit":
        room = rooms.get(player.position, "Invalid room setting - something broke")
        print(room.description())
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