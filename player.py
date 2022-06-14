import random
from random import randint, choice

class Player:
    health = 10
    max_health = 10
    position = [randint(0, 3), randint(0, 3)]

    def was_hit(self, hid):
        # self.health -= hid
        self.health -= 1 + random.choice(range(hid+1))

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("player's health:", self.health)

