import arcade

SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
WIDTH = 800
HEIGHT = 600
VIEWPORT_MARGIN = 50
MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Sprites With Walls Example")
        self.player_list = None
        self.wall_list = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0

    def scroll(self):
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left +=  self.player_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left, 
            WIDTH + self.view_left - 1, 
            self.view_bottom, 
            HEIGHT + self.view_bottom - 1)

    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.view_left = 0
        self.view_right = 0

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite("./PNG/Adventurer/Poses/adventurer_cheer1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)
        # for i in range(173, 650, 64):
        #     wall = arcade.Sprite("./boxCrate_double.png", SPRITE_SCALING_BOX)
        #     wall.center_x = i
        #     wall.center_y = 200
        #     self.wall_list.append(wall)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        # Draw some gridlines to help place blocks
        world_left = -3200
        world_right = 3200
        world_top = 3200
        world_bottom = -3200
        # horizontal
        for i in range(world_bottom, world_top, 64):
            arcade.draw_line(world_left, i, world_right, i, arcade.color.BLACK)
        # vertical
        for i in range(world_left, world_right, 64):
            arcade.draw_line(i, world_top, i, world_bottom, arcade.color.BLACK)
        self.wall_list.draw()
        self.player_list.draw()
    
    def update(self, delta_time):
        self.scroll()
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

    def on_mouse_press(self, x, y, button, modifiers):
        '''add a box on current mouse location when mouse is clicked'''
        if button == arcade.MOUSE_BUTTON_LEFT:
            wall = arcade.Sprite("./boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = (x + self.view_left) // 64 * 64 + 32
            wall.center_y = (y + self.view_bottom) // 64 * 64 + 32
            self.wall_list.append(wall)
            # TODO add ability to delete on click
        # print wall positions on right click 
        # could this be saved to file?
        else:
            print([[box.center_x, box.center_y] for box in self.wall_list])

    
window = MyGame()
window.setup()
arcade.run()
