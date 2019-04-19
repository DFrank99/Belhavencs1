import os
import random
import arcade
# --- Constants ---
SPRITE_SCALING_PLAYER = 0.05
SPRITE_SCALING_GOOD = 0.04
SPRITE_SCALING_BAD = 0.1
GOOD_COUNT = 50
BAD_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3

class Bad(arcade.Sprite):
    """ Class represents coins on screen. child class of arcade library "Sprite" class"""
    def reset_pos(self):
        # Reset coin to random spot above screen
        self.center_x = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_y = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the asteroids
        self.center_x -= 1

        # See if coin has fallen off side of screen
        if self.right < 0:
            self.reset_pos()

class Good(arcade.Sprite):
    """ Class represents good sprites"""
    def reset_pos(self):
        # Reset coin to random spot above screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the hearts
        self.center_y -= 1

        # See if coin has fallen off bottom of screen
        if self.top < 0:
            self.reset_pos()

class MyGame(arcade.Window):
    """ Custom window class """

    def __init__(self):
        """ Initializer """
        # Call parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Seeing Hearts")
        arcade.set_background_color(arcade.color.BRIGHT_UBE)

        # Start of first page instructions
        self.current_state = INSTRUCTIONS_PAGE_0

        # Variable that hold sprite lists
        self.player_list = None
        self.good_list = None
        self.bad_list = None

        # Player info
        self.player_sprite = None
        self.score = 0

        # instructions in an image
        self.instructions = []
        texture = arcade.load_texture("images/instructions_0.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/instructions_1.png")
        self.instructions.append(texture)

        # Sound
        self.good_sound = arcade.load_sound("images/SciFiGun2.m4a")
        self.bad_sound = arcade.load_sound("images/Swipe9.m4a")

        # Dont show mouse
        self.set_mouse_visible(False)



    def setup(self):
        """ Set up game and initialize variable; has to be called ourselves"""

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up player
        self.player_sprite = arcade.Sprite("images/kuromi.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create coins
        for i in range(GOOD_COUNT):

            # Create coin instnace
            good = Good("images/good.png", SPRITE_SCALING_GOOD)

            # Position
            good.center_x = random.randrange(SCREEN_WIDTH)
            good.center_y = random.randrange(SCREEN_HEIGHT)

            # Add coin to lists
            self.good_list.append(good)

        # Create coins
        for i in range(BAD_COUNT):

            # Create coin instnace
            bad = Bad("images/bad.png", SPRITE_SCALING_BAD)

            # Position
            bad.center_x = random.randrange(SCREEN_WIDTH)
            bad.center_y = random.randrange(SCREEN_HEIGHT)

            # Add coin to lists
            self.bad_list.append(bad)

    def draw_instructions_page(self, page_number):
        """Draw instructions"""
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game_over(self):
        """Draws a Game Over screen"""
        output = "GAME OVER"
        arcade.draw_text(output, 240, 400, arcade.color.BLACK, 54)

        output = "Try again! Click to restart."
        arcade.draw_text(output, 300, 300, arcade.color.BLACK, 14)

    def draw_game(self):
        self.good_list.draw()
        self.bad_list.draw()
        self.player_list.draw()

        # Put text
        output = f"Hearts Obtained: {self.score}"
        arcade.draw_rectangle_filled(100, 20, 300, 10, arcade.color.WHITE)
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 20)

    def on_draw(self):
        """ Draw stuff"""
        arcade.set_background_color(arcade.color.BRIGHT_UBE)
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def on_mouse_press(self, x, y, button, modifiers):
        """Press mouse button"""
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # start game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # restart game
            self.setup()
            self.current_state = GAME_RUNNING

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handles Mouse motion"""
        # Character moves with mouse
        if self.current_state == GAME_RUNNING:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y


    def update(self, delta_time):
        """ Movement and game Logic"""

        if self.current_state == GAME_RUNNING:
            # Call update on sprites
            self.good_list.update()
            self.bad_list.update()

            #this is when character collides with sprite
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.good_list)
            die_list = arcade.check_for_collision_with_list(self.player_sprite,self.bad_list)

            # score points
            for good in hit_list:
                good.kill()
                self.score += 1
                arcade.play_sound(self.good_sound)
            for bad in die_list:
                bad.kill()
                self.score -= 1
                arcade.play_sound(self.bad_sound)

            # ending game
            if self.score == 0 and self.bad_list == 0:
                self.current_state = GAME_OVER
            if len(self.good_list) == 0:
                self.current_state = GAME_OVER
                self.set_mouse_visible(True)


def main():
    """ Main Method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__=="__main__":
    main()
