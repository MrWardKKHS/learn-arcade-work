# refactoring the code to a ball class
import arcade

WIDTH = 800
HEIGHT = 600
TITLE = "The bouncing ball"

class Ball():
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
    

def on_draw(dt):
    arcade.start_render()
    arcade.draw_circle_filled(ball.x, ball.y, 25, arcade.color.REDWOOD)
    if ball.x < 0:
     ball.vel_x = abs(ball.vel_x)
    if ball.x > WIDTH:
     ball.vel_x = - abs(ball.vel_x)
    if ball.y < 0:
     ball.vel_y = abs(ball.vel_y)
    if ball.y > HEIGHT:
     ball.vel_y = -abs(ball.vel_y)
    ball.x += ball.vel_x
    ball.y += ball.vel_y

ball = Ball(100, 200, 3, 5)

arcade.open_window(WIDTH, HEIGHT, TITLE)

arcade.schedule(on_draw, 1/60)
arcade.run()
