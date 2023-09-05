import random
import time

from typing import Optional
import arcade
from arcade import Texture
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.enemy_list = []
        self.gameover = arcade.load_sound(':resources:sounds/gameover3.wav',False)
        self.laser_sound = arcade.load_sound(':resources:sounds/hit2.wav')
        self.black_page=arcade.load_texture("black.png")
        for i in range(3):
            heart_object=Heart(i)
            self.heart_list.append(heart_object)

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

        for heart in self.heart_list:
            heart.draw()

        if len(self.heart_list)==0 or self.collosion==1:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.black_page)
            arcade.draw_text("GAME OVER",self.width/3,self.height/2,arcade.color.ORANGE,36,15)
            

        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
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

            elif doshmana.center_y < 0:
                self.enemy_list.remove(doshmana)

        for bullet in self.me.bullet_list:
            bullet.move()

        for doshmana in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(doshmana, bullet):
                    
                    fall_sound = arcade.load_sound(path=self.laser_sound)
                    arcade.play_sound(sound=fall_sound)

                    self.enemy_list.remove(doshmana)
                    self.me.bullet_list.remove(bullet)

    
        if random.randint(1,6) == 6:
            self.new_doshman = Enemy(self)
            self.enemy_list.append(self.new_doshman)



    


