import arcade
import random
from pathlib import Path

WIDTH = 800
HEIGHT = 800

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

    def setup(self):
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite(Path("./PNG/Soldier/Poses/soldier_stand.png"))
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        self.coin_sprite = arcade.Sprite(Path("coin.png"))
        for i in range(80):
            coin = Coin(Path("coin.png"), 0.07)
            coin.center_x = random.randint(10, WIDTH - 10)
            coin.center_y = random.randint(150, HEIGHT + 20)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, self.height - 50, arcade.color.BLUE_SAPPHIRE, 32)
    
    def on_mouse_press(self, x, y, button, modifiers):
        bullet = arcade.Sprite(Path("laser.png"), 0.6)
        bullet.center_x = self.player_sprite.center_x 
        bullet.center_y = self.player_sprite.center_y + 10
        bullet.change_y = 12
        bullet.angle = 90
        self.bullet_list.append(bullet)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        # self.player_sprite.center_y = y
    
    def update(self, dt):
        self.coin_list.update()
        self.bullet_list.update()
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            for coin in hit_list:
                self.score += 1
                coin.kill()
                bullet.kill()


game = Game(600, 600, "Sprites")
game.setup()

arcade.run()
