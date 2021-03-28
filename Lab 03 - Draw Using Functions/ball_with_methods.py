# adding an update and draw method to the ball class
# making 100 balls

import arcade
from random import randint

WIDTH = 800
HEIGHT = 600
TITLE = "The bouncing self"
balls = []

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
    

def on_draw(dt):
    arcade.start_render()
    
    for b in balls:
        b.update()
        b.draw()
    

# ball = Ball(100, 200, 3, 5)
# ball2 = Ball(320, 20, 4, 6)

for i in range(100):
    b = Ball(randint(0, WIDTH), randint(0, HEIGHT), randint(-10, 10), randint(-10, 10))
    balls.append(b)

arcade.open_window(WIDTH, HEIGHT, TITLE)

arcade.schedule(on_draw, 1/60)
arcade.run()
