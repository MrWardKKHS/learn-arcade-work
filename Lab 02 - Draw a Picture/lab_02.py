import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, 'road')

color1 = arcade.color.AIR_SUPERIORITY_BLUE
color2 = (200, 200, 255)
points = (0, 0), (WIDTH, 0), (WIDTH,HEIGHT), (0, HEIGHT)
colors = (color1, color1, color2, color2)
rect = arcade.create_rectangle_filled_with_colors(points, colors)

arcade.set_background_color(arcade.color.TIMBERWOLF)

arcade.start_render()

rect.draw()
arcade.draw_polygon_filled([(0, 0), (400, 100), (600, 100), (550, 0)], arcade.color.ASH_GREY)
arcade.draw_polygon_filled([(0, 0), (400, 100), (400, 150), (0, 200)], arcade.color.BROWN_NOSE)
arcade.draw_rectangle_outline(250,140, 100, 100, arcade.color.RED_PURPLE)
arcade.draw_lrtb_rectangle_filled(20, 50, 300, 10, arcade.color.MEDIUM_RUBY)

arcade.finish_render()

arcade.run()