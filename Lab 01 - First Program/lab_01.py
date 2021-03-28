import arcade

arcade.open_window(600, 600, "My first arcade game")

arcade.set_background_color(arcade.color.ZAFFRE)

arcade.start_render()

arcade.draw_rectangle_filled(300, 300, 50, 30, arcade.color.DEEP_JUNGLE_GREEN)

arcade.finish_render()

arcade.run()