# extending the class arcade.Window
from random import randint
import arcade
import os

WIDTH = 1000
HEIGHT = 1000
DEAD_ZONE = 0.2

laser_sound = arcade.load_sound(os.path.join("C:\\","Users", "award", "dev", "learn-arcade-work", "Lab 07 - User Control", 'laser.ogg'))

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        self.ball = Ball(width/2, height/2)
        arcade.set_background_color(arcade.color.HANSA_YELLOW)
        self.set_mouse_visible(False)
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None
        print(self.joystick.__dict__)


    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(laser_sound)
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.radius += 3
            self.ball.color = (randint(0,255), randint(0,255), randint(0,255), 255)
        else:
            self.ball.radius -= 3
            self.ball.color = (randint(0,255), randint(0,255), randint(0,255), 255)
            

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, dt):
        self.ball.update(self.joystick)
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.x = x
        self.ball.y = y

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.ball.vel_y += 10
        if symbol == arcade.key.DOWN:
            self.ball.vel_y += -10
        if symbol == arcade.key.LEFT:
            self.ball.vel_x += -10
        if symbol == arcade.key.RIGHT:
            self.ball.vel_x += 10

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.ball.vel_y -= 10
        if symbol == arcade.key.DOWN:
            self.ball.vel_y -= -10
        if symbol == arcade.key.LEFT:
            self.ball.vel_x -= -10 
        if symbol == arcade.key.RIGHT:
            self.ball.vel_x -= 10


class Ball():
    def __init__(self, x, y, vel_x=0, vel_y=0):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = arcade.color.RICH_CARMINE
        self.radius = 25

    def update(self, joystick):
        if abs(joystick.x) > DEAD_ZONE:
            self.x += joystick.x * 10
        if abs(joystick.y) > DEAD_ZONE:
            self.y += joystick.y * -10


    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)


window = Game(WIDTH, HEIGHT, 'USING THE WINDOW CLASS')

arcade.run()