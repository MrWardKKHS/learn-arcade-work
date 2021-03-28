# a slightly more detailed version 
import arcade

WIDTH = 600
HEIGHT = 400
TITLE = 'My Game'

window = arcade.open_window(WIDTH, HEIGHT, TITLE)

arcade.set_background_color(arcade.color.REDWOOD)

arcade.start_render()
arcade.finish_render()

arcade.run()