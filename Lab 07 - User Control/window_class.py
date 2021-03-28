# extending the class arcade.Window

import arcade

WIDTH = 1000
HEIGHT = 1000

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        self.ball = Ball(width/2, height/2, 3, 4)
        arcade.set_background_color(arcade.color.HANSA_YELLOW)
    
    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, dt):
        self.ball.update()

class Ball():
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self):
        if self.x < 0:
            self.vel_x = abs(self.vel_x)
        if self.x > WIDTH:
            self.vel_x = - abs(self.vel_x)
        if self.y < 0:
            self.vel_y = abs(self.vel_y)
        if self.y > HEIGHT:
            self.vel_y = -abs(self.vel_y)
        self.x += self.vel_x
        self.y += self.vel_y


    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 25, arcade.color.REDWOOD)


window = Game(WIDTH, HEIGHT, 'USING THE WINDOW CLASS')

arcade.run()