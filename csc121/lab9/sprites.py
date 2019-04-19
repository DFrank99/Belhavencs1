""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    """ Class represents coins on screen. child class of arcade library "Sprite" class"""
    def reset_pos(self):
        # Reset coin to random spot above screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if coin has fallen off bottom of screen
        if self.top < 0:
            self.reset_pos()

class MyGame(arcade.Window):
    """ Custom window class """

    def __init__(self):
        """ Initializer """
        # Call parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variable that hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Player info
        self.player_sprite = None
        self.score = 0

        # Dont show mouse
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up game and initialize variable; has to be called ourselves"""

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up player
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create coins
        for i in range(COIN_COUNT):

            # Create coin instnace
            coin = Coin("coin_01.png", SPRITE_SCALING_COIN)

            # Position
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add coin to lists
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        # Draw sprite lists here. sprites are divided into different groups
        # Other game engines might cal these sprite layers/sprite groups
        # Sprites that dont move should be drawn in their own group
        # Try avoiding drawing sprites on ther own use SpriteList
        self.coin_list.draw()
        self.player_list.draw()

        # Put text
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handles Mouse motion"""
        # Character matches mouse
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game Logic"""
        # Call update on sprites
        self.coin_list.update()

        # Generate a list of all sprites colliding with player
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)

        # Loop through each colliding sprite, remove it, and add to score
        for coin in hit_list:
            coin.kill()
            self.score += 1

def main():
    """ Main Method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__=="__main__":
    main()
