import random
from typing import Optional
import arcade
from arcade import Texture
from spaceship import Spaceship
from enemy import Enemy


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.enemy_list = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background
        )
        self.me.draw()

        for doshmanan in self.enemy_list:
            doshmanan.draw()

            for bullet in self.me.bullet_list:
                bullet.draw()

        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.me.change_x = -1
        elif symbol == arcade.key.D:
            self.me.change_x = 1
        elif symbol == arcade.key.S:
            self.me.change_x = 0
        elif symbol == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0

    def on_update(self, delta_time: float):
        self.me.move()
        
        for doshmana in self.enemy_list:
            doshmana.move()
            if arcade.check_for_collision(self.me, doshmana):
                print("Game Over☠")
                exit(0)
            if doshmana.center_y < 0:
                self.enemy_list.remove(doshmana)

        for bullet in self.me.bullet_list:
            bullet.move()

        for doshmana in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(doshmana, bullet):
                    
                    fall_sound = arcade.load_sound(path=":resources:sounds/hit2.wav")
                    arcade.play_sound(sound=fall_sound)

                    self.enemy_list.remove(doshmana)
                    self.me.bullet_list.remove(bullet)

        if random.randint(1, 50) == 6:
            self.new_doshman = Enemy(self)
            self.enemy_list.append(self.new_doshman)
