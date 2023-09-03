import random
from typing import Optional
import arcade
from arcade import Texture
from spaceship import Spaceship
from enemy import Enemy

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resource:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 6
        self.change_x = 0
        self.change_y = 1

    def move(self):
        self.center_y += self.speed

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.doshmans = []

        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background
        )
        self.me.draw()
        
        for doshmanan in self.doshmans:
            doshmanan.draw()
        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.me.change_x = -1
        elif symbol == arcade.key.D:
            self.me.change_x = 1
        elif symbol == arcade.key.S:
            self.me.change_x = 0
        elif symbol == arcade.key.SPACE:
            ...

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0
            
    def on_update(self, delta_time: float):

        self.me.move()
        for doshmana in self.doshmans:
            if arcade.check_for_collision(self.me, doshmana):
                print('Game Over☠')
                exit(0)

            doshmana.move()

        if random.randint(1,50) == 6 :
            self.new_doshman = Enemy(self)
            self.doshmans.append(self.new_doshman)