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
        self.score=0
        self.enemy_list = []
        self.heart_list = []

        self.gameover = arcade.load_sound(':resources:sounds/gameover3.wav',False)
        self.laser_sound = arcade.load_sound(':resources:sounds/hit2.wav')
        self.black_page=arcade.load_texture("black.png")
        
        for i in range(3):
            heart_object=Heart(i)
            self.heart_list.append(heart_object)

        self.second=time.time()
        self.rise_speed=time.time()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background
        )
        arcade.draw_text(str(self.score),self.width-60,15,arcade.color.WHITE,25,12)

        self.me.draw()

        for doshmanan in self.enemy_list:
            doshmanan.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()

        for heart in self.heart_list:
            heart.draw()

        if len(self.heart_list)==0:
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
        if len(self.heart_list)!=0 :
            self.me.move()
            
            for doshmana in self.enemy_list:
                doshmana.move()

                if arcade.check_for_collision(self.me, doshmana):
                    print("Game Over☠")
                    exit(0)

                elif doshmana.center_y < 0:
                    self.enemy_list.remove(doshmana)
                    self.heart_list.pop()
                    if len(self.heart_list)==0:
                        print("Game Over")
                        arcade.play_sound(self.gameover,1)

            for bullet in self.me.bullet_list:
                bullet.move()

            for doshmana in self.enemy_list:
                for bullet in self.me.bullet_list:
                    if arcade.check_for_collision(doshmana, bullet):
                        
                        arcade.play_sound(sound=self.laser_sound)

                        self.enemy_list.remove(doshmana)
                        self.me.bullet_list.remove(bullet)
                        self.score+=1

            if time.time()-self.second>=3:
                    self.second=time.time()
                    self.doshmana=Enemy(self)
                    self.enemy_list.append(self.doshmana)

            if time.time()-self.rise_speed>=10:
                self.rise_speed=time.time()
                Enemy(self).rise_speed()
                self.me.bullet_rise_speed()
        
        else:
            self.enemy_list.clear()
            self.me.bullet_list.clear()
            self.me.kill()

    
    



    


