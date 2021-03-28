import arcade
import random

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.coin_list = []
        self.player_list = []

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.APRICOT)

    def setup(self):
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite(r'PNG\Soldier\Poses\soldier_stand.png')
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        self.coin_sprite = arcade.Sprite(r"C:\Users\award\dev\learn-arcade-work\coin.png")
        for i in range(30):
            coin = arcade.Sprite(r"C:\Users\award\dev\learn-arcade-work\coin.png", 0.1)
            coin.center_x = random.randint(50, 550)
            coin.center_y = random.randint(50, 550)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 50, 550, arcade.color.BLUE_SAPPHIRE, 32)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    
    def update(self, dt):
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.kill()
            self.score += 1


game = Game(600, 600, "Sprites")
game.setup()

arcade.run()
