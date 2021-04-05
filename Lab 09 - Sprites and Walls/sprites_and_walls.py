""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")
        self.player_list = None
        self.wall_list = None
        self.physics_engine = None


    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite("./PNG/Adventurer/Poses/adventurer_cheer1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)
        for i in range(173, 650, 64):
            wall = arcade.Sprite("./boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = i
            wall.center_y = 200
            self.wall_list.append(wall)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
    
    def update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y =  -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x =  -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x =  MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


window = MyGame()
window.setup()
arcade.run()
