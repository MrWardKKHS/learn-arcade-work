import arcade
from threading import Timer

WIDTH = 1800
HEIGHT = 1000

TITLE = "TMX Playground"

#scaling
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 0.6
PLAYER_JUMP_SPEED = 20
PLAYER_START_X = 200
PLAYER_START_Y = 50

VIEWPORT_MARGIN = 300

RIGHT_FACING = 0
LEFT_FACING = 1

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.facing_direction = RIGHT_FACING

        self.cur_texture_index = 0
        self.scale = CHARACTER_SCALING

        self.jumping = False
        main_path = "./PNG/Soldier/Poses/"

        self.idle_texture_pair = load_texture_pair(f"{main_path}soldier_stand.png")
        self.jump_texture_pair = load_texture_pair(f"{main_path}soldier_jump.png")
        self.fall_texture_pair = load_texture_pair(f"{main_path}soldier_fall.png")
        self.walk_textures = []
        for i in range(4):
            texture = load_texture_pair(f"{main_path}soldier_walk1.png")
            self.walk_textures.append(texture)
        for i in range(4):
            texture = load_texture_pair(f"{main_path}soldier_walk2.png")
            self.walk_textures.append(texture)
        
        self.texture = self.idle_texture_pair[0]
        self.set_hit_box(self.texture.hit_box_points)

    def update_animation(self, delta_time = 1/60):
        if self.change_x < 0 and self.facing_direction == RIGHT_FACING:
            self.facing_direction = LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == LEFT_FACING:
            self.facing_direction = RIGHT_FACING

        if self.change_y > 0:
            self.texture = self.jump_texture_pair[self.facing_direction]
            return
        if self.change_y < 0:
            self.texture = self.fall_texture_pair[self.facing_direction]
            return 
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]
            return 

        self.cur_texture_index += 1
        self.cur_texture_index = self.cur_texture_index % len(self.walk_textures)
        self.texture = self.walk_textures[self.cur_texture_index][self.facing_direction]

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.player_sprite = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0
        self.score = 0
        self.level = 1
        self.end_of_map = 0

        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self, level):
        self.view_bottom = 0
        self.view_left = 0
        self.score = 0
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        self.load_map(f'./Maps/level{level}.tmx')
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)


    def load_map(self, resource):
        platforms_layer_name = 'Platforms'
        coins_layer_name = 'Coins'
        foreground_layer_name = 'Detail'
        dont_touch_layer_name = "Death"

        my_map = arcade.tilemap.read_tmx(resource)

        self.end_of_map = my_map.map_size.width * GRID_PIXEL_SIZE

        self.wall_list = arcade.tilemap.process_layer(
            map_object=my_map, 
            layer_name=platforms_layer_name, 
            scaling=TILE_SCALING, 
            use_spatial_hash=True
        )

        self.coin_list = arcade.tilemap.process_layer(
            my_map, 
            coins_layer_name, 
            TILE_SCALING,
            use_spatial_hash=True
        )

        self.foreground_list = arcade.tilemap.process_layer(
            my_map, 
            foreground_layer_name, 
            TILE_SCALING
        )

        self.dont_touch_list = arcade.tilemap.process_layer(
            my_map, 
            dont_touch_layer_name, 
            TILE_SCALING, 
            use_spatial_hash=True
        )
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

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

        # top_boundary = self.view_bottom + HEIGHT - VIEWPORT_MARGIN
        # if self.player_sprite.top > top_boundary:
        #     self.view_bottom += self.player_sprite.top - top_boundary
        #     changed = True

        # bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        # if self.player_sprite.bottom < bottom_boundary:
        #     self.view_bottom -= bottom_boundary - self.player_sprite.bottom
        #     changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left, 
            WIDTH + self.view_left - 1, 
            self.view_bottom, 
            HEIGHT + self.view_bottom - 1)
    
    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.coin_list.draw()
        self.dont_touch_list.draw()
        self.player_list.draw()
        self.foreground_list.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom, arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
            
    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_sprite.update_animation(delta_time)

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        
        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            self.setup(self.level)

        if arcade.check_for_collision_with_list(self.player_sprite, self.dont_touch_list):
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            self.setup(self.level)

        if self.player_sprite.center_x >= self.end_of_map:
            self.level += 1
            self.setup(self.level)

        self.scroll()

window = MyGame()
window.setup(window.level)
arcade.run()