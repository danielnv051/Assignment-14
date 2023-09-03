import arcade
from bullet import Bullet


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.center_x = game.width // 2
        self.center_y = 50
        self.change_x = -1
        self.change_y = 0
        self.width = 48
        self.height = 48
        self.speed = 4
        self.game_with = game.width
        self.bullet_list = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 24:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.game_with - 24:
                self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)

        arcade.play_sound(
            sound=":resources:sounds/laser3.wav"
        )