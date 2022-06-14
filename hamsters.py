from random import randint, choice
from player import Player

class Hamster:
    def __init__(self, hid, map):
        self.id = hid
        self.health = 2
        self.position = self.get_clear_position(map)

    def get_clear_position(self, map):
        map_height = len(map.split("\n"))
        map_width = len(map.split("\n")[0])
        while True:
            x = choice([ele for ele in range(0, map_width) if ele != Player.position[0]])
            y = choice([ele for ele in range(0, map_height) if ele != Player.position[1]])
            coords = [x, y]
            if map.split("\n")[coords[1]][coords[0]] == "*":
                return coords

    def on_shot(self):
        self.health -= 1
        if self.health == 0:
            print(self.id, "was killed")
            return True
        else:
            return False

