# Getting the ball to move
import arcade

WIDTH = 800
HEIGHT = 600
TITLE = "The bouncing ball"

def on_draw(dt):
    arcade.start_render()
    arcade.draw_circle_filled(on_draw.x, on_draw.y, 25, arcade.color.REDWOOD)
    on_draw.x += 3
    on_draw.y += 2

on_draw.x = 100
on_draw.y = 50

arcade.open_window(WIDTH, HEIGHT, TITLE)

arcade.schedule(on_draw, 1/60)
arcade.run()
