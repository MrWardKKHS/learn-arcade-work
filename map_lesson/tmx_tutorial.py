import arcade

WIDTH = 1200
HEIGHT = 800
TITLE = 'TMX lesson'

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.setup()

    def setup(self):
        my_map = arcade.tilemap.read_tmx("./map_lesson/maps/level1.tmx")
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map, layer_name="Platforms", use_spatial_hash=True, scaling=0.3)
        self.coin_list = arcade.tilemap.process_layer(map_object=my_map, layer_name="Coins", scaling=0.3)
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.wall_list.draw()

game = Game()
arcade.run()