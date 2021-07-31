import arcade
import random
from pathlib import Path
from arcade.experimental.lights import Light, LightLayer

WIDTH = 800
HEIGHT = 800

AMBIENT_COLOR = (10, 10, 10)

class Bullet(arcade.Sprite):

    def __init__(self):
        super().__init__(Path("laser.png"), 0.6)
        self.light = Light(self.center_x, self.center_y, 100, arcade.color.ELECTRIC_BLUE, 'soft')
        game.light_layer.add(self.light)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.light.position = self.position

    def kill(self):
        game.light_layer.remove(self.light)
        self.remove_from_sprite_lists()



class Coin(arcade.Sprite):

    def update(self):
        pass
    #     self.center_y -= 2
    #     if self.center_y < - 20:
    #         self.center_y = random.randrange(HEIGHT + 10, HEIGHT + 100)
    #         self.center_x = random.randrange(10, WIDTH - 10)
            

    # def reset(self):
    #         self.center_y = random.randrange(HEIGHT + 10, HEIGHT + 100)
    #         self.center_x = random.randrange(10, WIDTH - 10)

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        self.coin_list = []
        self.player_list = []
        self.bullet_list = []

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AUROMETALSAURUS)
        self.light_layer = None
        self.player_list = None
        self.background_sprite_list = None

    def setup(self):
        self.coin_list = arcade.SpriteList()
        self.background_sprite_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite(Path("./PNG/Soldier/Poses/soldier_stand.png"))
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)
        for x in range(-128, 2000, 128):
            for y in range(-128, 1000, 128):
                sprite = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png")
                sprite.position = x, y
                self.background_sprite_list.append(sprite)

        self.make_coins()

        self.light_layer = LightLayer(WIDTH, HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)

        light = Light(100, 200, 100, arcade.color.WHITE, 'soft')
        self.light_layer.add(light)
        self.player_light = Light(0, 0, 150, arcade.color.WHITE, 'soft')
        self.light_layer.add(self.player_light)

    def make_coins(self):
        for i in range(80):
            coin = Coin(Path("coin.png"), 0.07)
            coin.center_x = random.randint(10, WIDTH - 10)
            coin.center_y = random.randint(150, HEIGHT - 10)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        with self.light_layer:
            self.background_sprite_list.draw()
            self.coin_list.draw()
            self.player_list.draw()
            self.bullet_list.draw()
        self.light_layer.draw(ambient_color=AMBIENT_COLOR)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, self.height - 50, arcade.color.BLUE_SAPPHIRE, 32)
    
    def on_mouse_press(self, x, y, button, modifiers):
        bullet = Bullet()
        bullet.center_x = self.player_sprite.center_x 
        bullet.center_y = self.player_sprite.center_y + 10
        bullet.change_y = 12
        bullet.angle = 90
        bullet.light.position = bullet.position
        self.bullet_list.append(bullet)
        

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        # self.player_sprite.center_y = y
        self.player_light.position = self.player_sprite.position
    
    def update(self, dt):
        self.coin_list.update()
        self.bullet_list.update()
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            if hit_list:
                bullet.kill()
            for coin in hit_list:
                self.score += 1
                coin.kill()
            if not self.coin_list:
                self.make_coins()

        self.player_light.position = self.player_sprite.position


game = Game(WIDTH, HEIGHT, "Lights")
game.setup()

arcade.run()
