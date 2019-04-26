import arcade
import random
import os

# ---Constants
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_WALL = .3
SPRITE_SCALING_COIN = .5
COIN_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# how many pixels to keep within margin between character and edge of screen
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5

class Coin(arcade.Sprite):
    """ Class represents good sprites"""
    def reset_pos(self):
        # Reset coin to random spot above screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):
    """Main window of game"""
    def __init__(self):
        """Initializer"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Off the Wall")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Player and score
        self.player_sprite = None
        self.score = 0
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False


        # Sounds
        self.coin_sound = arcade.load_sound("images/coin.m4a")

        # bakground
        arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)
        # Do not show mouse
        self.set_mouse_visible(False)

    def setup(self):
        """ Game and initialize variables"""
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up player
        self.player_sprite = Player("images/grimm.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # set viewport boundaries; numbers set to what we scroll to
        self.view_left = 0
        self.view_bottom = 0

        # -- Wall Setup
        # Rows in loop
        #wall
        for x in range (600, 800, 60):
            wall = arcade.Sprite("images/red.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        # Create a column of boxes
        for y in range(800, 600, 60):
            wall = arcade.Sprite("images/red.png", SPRITE_SCALING_WALL)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        # Create coins
        for i in range(COIN_COUNT):
            # Create coin instnace
            coin = Coin("images/coin.png", SPRITE_SCALING_COIN)
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)


            coin_placed_successfully = False

            # Place coins until finding proper spot
            while not coin_placed_successfully:
                # Position
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # If coin hits wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            # Add coin to lists
            self.coin_list.append(coin)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def draw_game(self):
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Put text
        output = f"Moneys collected: {self.score}"
        arcade.draw_rectangle_filled(100, 20, 300, 10, arcade.color.BLACK)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 20)

    def on_draw(self):
        """Render screen"""

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

    def on_key_press(self, key, modifiers):
        """Key being pressed """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Release a key """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """
        # Update on sprite collision
        self.physics_engine.update()
        self.coin_list.update()
        self.wall_list.update()

        # score points
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.kill()
            self.score += 1
            arcade.play_sound(self.coin_sound)

         # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        # Call update to move the sprite
        # If using a physics engine, call update on it instead of the sprite
        # list.

        # --Manage Scrolling
        changed = False

        # scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
