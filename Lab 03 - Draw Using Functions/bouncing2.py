# Getting the ball to move
import arcade

WIDTH = 800
HEIGHT = 600
TITLE = "The bouncing ball"

def on_draw(dt):
    arcade.start_render()
    arcade.draw_circle_filled(on_draw.x, on_draw.y, 25, arcade.color.REDWOOD)
    if on_draw.x < 0:
        on_draw.vx = abs(on_draw.vx)
    if on_draw.x > WIDTH:
        on_draw.vx = - abs(on_draw.vx)
    if on_draw.y < 0:
        on_draw.vy = abs(on_draw.vy)
    if on_draw.y > HEIGHT:
        on_draw.vy = -abs(on_draw.vx)
    on_draw.x += on_draw.vx
    on_draw.y += on_draw.vy

on_draw.x = 100
on_draw.y = 50
on_draw.vx = 3
on_draw.vy = 2

arcade.open_window(WIDTH, HEIGHT, TITLE)

arcade.schedule(on_draw, 1/60)
arcade.run()
