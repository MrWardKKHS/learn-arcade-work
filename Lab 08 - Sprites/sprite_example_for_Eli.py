import arcade
import random
from math import atan2, degrees, sin, cos
from opensimplex import OpenSimplex

WIDTH = 1000
HEIGHT = 1000

noise = OpenSimplex()

class Coin(arcade.Sprite):

    def update(self):
        self.center_x += cos(self.movement_angle) * self.speed
        self.center_y += sin(self.movement_angle) * self.speed
        self.noise += 0.01
        self.movement_angle = noise.noise2d(self.noise, self.noise)
        self.center_x += self.change_x
        self.center_y += self.change_y

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.coin_list = None
        self.player_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.APRICOT)

    def setup(self):
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite(r'PNG\Soldier\Poses\soldier_stand.png')
        self.player_sprite.center_x = WIDTH/2
        self.player_sprite.center_y = HEIGHT/2
        self.player_list.append(self.player_sprite)

        self.coin_sprite = arcade.Sprite(r"C:\Users\award\dev\learn-arcade-work\coin.png")
        for i in range(100):
            coin = Coin(r"C:\Users\award\dev\learn-arcade-work\coin.png", 0.1)
            coin.center_x = random.randint(-500, WIDTH + 500)
            coin.center_y = random.randint(-500, HEIGHT + 500)
            coin.noise = i * 100
            coin.movement_angle = noise.noise2d(coin.noise, coin.noise)
            coin.speed = random.randint(-5, 5)
            self.coin_list.append(coin)

    def on_mouse_press(self, x, y, button, modifiers):
        SCALE_FACTOR = 0.01
        dx = self.player_sprite.center_x - x
        dy = self.player_sprite.center_y - y
        for coin in self.coin_list:
            coin.change_x += dx * SCALE_FACTOR
            coin.change_y += dy * SCALE_FACTOR

    def on_mouse_motion(self, x, y, dx, dy):
        dx = self.player_sprite.center_x - x
        dy = self.player_sprite.center_y - y
        deg = degrees(atan2(dx, dy))
        self.player_sprite.angle = -deg - 90

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 50, 550, arcade.color.BLUE_SAPPHIRE, 32)
    
    def update(self, dt):
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.kill()
            self.score += 1


game = Game(WIDTH, HEIGHT, "Sprites")
game.setup()

arcade.run()
