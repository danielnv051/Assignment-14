import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + 24
        self.width = 48
        self.height = 48
        self.angle = 180
        self.speed = 5

    def move(self):
        self.center_y -=self.speed

    def rise_speed(self):
        self.speed+=1
        print(self.speed)

