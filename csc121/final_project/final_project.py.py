import arcade
import random
import math
import os

# -- Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# -- Sprite Constants
WALL_SCALING = 0.1
CHARACTER_SCALING = 0.3
BAD_SCALING = 0.1
BULLET_SCALING = 0.1
COIN_SCALING = 0.2
COIN_COUNT = 50
BAD_COUNT = 10
TEXTURE_RIGHT = 1
TEXTURE_LEFT = 0
NATIVE_SIZE = 128
SPRITE_SIZE = int(NATIVE_SIZE * CHARACTER_SCALING)
EXPLOSION_COUNT = 30
SPLAT_COUNT = 30

# -- Movement
MOVEMENT_SPEED = 4
GRAVITY = 6
JUMP_SPEED = 10
BULLET_SPEED = 6
LEFT_VIEWPORT_MARGIN = 50
RIGHT_VIEWPORT_MARGIN = 30
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 50

# -- INSTRUCTIONS (states game will be in)
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3
window = None


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

class Coin(arcade.Sprite):

    def update(self):
        # Rotate the coin.
        self.angle += self.change_angle

class MyGame(arcade.Window):
    """Main application class"""
    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "DEMI-lition")

        # BACKGROUND & INSTRUCTIONS
        arcade.set_background_color(arcade.color.ARSENIC)
        self.background = None
        self.current_state = INSTRUCTIONS_PAGE_0
        # instructions as images
        self.instructions = []
        texture = arcade.load_texture("images/instructions1.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/instructions2.png")
        self.instructions.append(texture)


        # SPRITE LIST
        self.wall_list = None
        self.coin_list = None
        self.player_list = None
        self.bad_list = None
        self.bullet_list = None

        # PLAYER SPRITE
        self.player = None
        self.player_sprite = None
        self.score = 0

        # MOVEMENT
        self.view_bottom = 0
        self.view_left = 0


        # Sounds
        self.shoot_sound = arcade.load_sound("sounds/shoot.m4a")
        self.zombie_sound = arcade.load_sound("sounds/growl.m4a")
        self.shoot_sound = arcade.load_sound("sounds/shoot.m4a")
        self.hit_sound = arcade.load_sound("sounds/hit.m4a")
        self.jump_sound = arcade.load_sound("sounds/jump.m4a")
        self.coin_sound = arcade.load_sound("sounds/coin.m4a")
        self.start_sound = arcade.load_sound("sounds/song.m4a")
        self.end_sound = arcade.load_sound("sounds/over.m4a")
        self.explosion = arcade.load_sound("sounds/explosion.m4a")

        # Pre-load animation frames. We don't do this in the __init__
        # of the explosion sprite because it takes too long and would cause game to pause.
        self.explosion_texture_list = []
        for i in range(EXPLOSION_COUNT):
            texture_name = f"images/explosion.png"
            self.explosion_texture_list.append(arcade.load_texture(texture_name))
        for i in range(SPLAT_COUNT):
            self.explosion_texture_list.append(arcade.load_texture(texture_name))

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.background = arcade.load_texture("images/background.jpg")
        # -- CREATE SPRITE LIST
        self.score = 0
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # -- WALLS
        # Loop floor horizontal
        for x in range(0, 2000, SPRITE_SIZE):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)
        for x in range(0, 2000, SPRITE_SIZE):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.top = 600
            wall.left = x
            self.wall_list.append(wall)
        for x in range(0, SCREEN_HEIGHT, SPRITE_SIZE):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.left = 0
            wall.top = x
            self.wall_list.append(wall)
        for x in range(0, SCREEN_HEIGHT, SPRITE_SIZE):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.right = 2050
            wall.top = x
            self.wall_list.append(wall)


        # platforms
        # Create rows of boxes
        for x in range(373, 650, 40):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
        for x in range(900, 1000, 40):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
        for x in range(100, 300, 40):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)
        for x in range(373, 650, 40):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 400
            self.wall_list.append(wall)
        for x in range(775, 1000, 40):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 450
            self.wall_list.append(wall)

        # -- SETUP PLAYER
        self.player = arcade.AnimatedWalkingSprite()

        character_scale = CHARACTER_SCALING
        # STANDING
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("girl/idle/right/idle_01.png",
                                                                    scale=character_scale))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("girl/idle/left/idle_01.png",
                                                                    scale=character_scale))

        # WALK RIGHT
        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_01.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_02.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_03.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_04.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_05.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_06.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_07.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_08.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_09.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_10.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_11.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_12.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_13.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_14.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_15.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_16.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_17.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_18.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_19.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("girl/walk/right/walk_20.png",
                                                                   scale=character_scale))

        # WALK LEFT
        # mirrored is false cuz sprite is turned already
        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_01.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_02.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_03.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_04.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_05.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_06.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_07.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_08.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_09.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_10.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_11.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_12.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_13.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_14.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_15.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_16.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_17.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_18.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_19.png",
                                                                  scale=character_scale, mirrored=False))
        self.player.walk_left_textures.append(arcade.load_texture("girl/walk/left/walk_20.png",
                                                                  scale=character_scale, mirrored=False))

        self.player.texture_change_distance = 20
        self.player.center_x = 150
        self.player.center_y = 90
        self.player.scale = CHARACTER_SCALING
        self.player_list.append(self.player)

        # --- COINS
        # Create coin instnace
        coordinate_list = [[500, 450],
                           [70, 350],
                           [600, 75],
                           [830, 500],
                           [900, 250]]
        for coordinate in coordinate_list:
            coin = arcade.Sprite("images/coin.png", COIN_SCALING)
            coin.center_x = coordinate[0]
            coin.center_y = coordinate[1]
            # Set up the initial angle, and the "spin"
            coin.angle = 360
            coin.change_angle = random.randrange(5, 6)
            self.coin_list.append(coin)
        # Add coin to lists
        self.coin_list.append(coin)

        # -- ENEMY
        for i in range(BAD_COUNT):
            coordinate_list = [[400, 250],
                               [120, 350],
                               [700, 80],
                               [860, 500],
                               [930, 80]]
            for coordinate in coordinate_list:
                bad = arcade.Sprite("zombie/idle/idle_02.png", BAD_SCALING)
                bad.center_x = coordinate[0]
                bad.center_y = coordinate[1]
                self.bad_list.append(bad)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.wall_list)

    def draw_instructions_page(self, page_number):
        """Draw an instruction page. Load the page as an image"""
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game_over(self):
        """Draw "Game over" across the screen"""
        arcade.draw_rectangle_filled(530, 300, 500, 400, arcade.color.WHITE)
        output = arcade.load_texture("images/over.png")
        scale = .5
        arcade.draw_texture_rectangle(530, 350, scale * output.width,
                                      scale * output.height, output, 0)

        output = "Click to restart the SLAUGHTER!"
        arcade.draw_text(output, 310, 200, arcade.color.ALIZARIN_CRIMSON, 24)

    def draw_game(self):
        """Draw all the sprites, along with the score."""
        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()
        self.player.draw()
        self.wall_list.draw()
        self.bad_list.draw()
        self.bullet_list.draw()

        # Put the text on the screen.
        output = f"Starie Stars: {self.score}"
        arcade.draw_text(output, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.color.SAE, 30)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      4000, 800, self.background)

        # Draw all sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.bad_list.draw()
        self.bullet_list.draw()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()
            arcade.play_sound(self.start_sound)

        else:
            self.draw_game()
            self.draw_game_over()

    def on_key_press(self, key, modifiers):
        """Called whenever the mouse moves"""
        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = JUMP_SPEED
            arcade.play_sound(self.jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user presses a mouse button"""
        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the user presses a mouse button"""
        # Change states as needed.
        if self.current_state == INSTRUCTIONS_PAGE_0:
            # Next page of instructions.
            self.current_state = INSTRUCTIONS_PAGE_1
            arcade.play_sound(self.start_sound)
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # Start the game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

        # -- BULLETS
        # Create a bullet
        bullet = arcade.Sprite("images/bullet.png", BULLET_SCALING)
        # Position the bullet at the player's current location
        start_x = self.player.center_x
        start_y = self.player.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need
        # to add in self.view_bottom and self.view_left.
        dest_x = x
        dest_y = y
        self.view_bottom = view_bottom
        self.view_left = view_left

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        bullet.angle = math.degrees(angle)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def on_mouse_motion(self, x, y, dx, dy):
        """Called whenever the mouse moves"""
        # Only move the user if the game is running.
        #if self.current_state == GAME_RUNNING:


    def update(self, delta_time):
        """ Movement and game logic """
        # Only move and do things if the game is running.
        if self.current_state == GAME_RUNNING:
            # Call update on all sprites
            self.coin_list.update()
            self.player_list.update()
            self.player.update_animation()
            self.bad_list.update()
            self.bullet_list.update()

            # If we've collected all the games, then move to a "GAME_OVER" state.
            if len(self.coin_list) == 0:
                self.current_state = GAME_OVER
                arcade.play_sound(self.end_sound)
                self.set_mouse_visible(True)

        # -- MOVEMENT
        # Call update to move the sprite
        # If using a physics engine, call update on it instead of the sprite list.
        self.physics_engine.update()
        # --- Manage Scrolling ---
        # Track if we need to change the viewport
        changed = False
        # Scroll left
        left_boundry = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player.left < left_boundry:
            self.view_left -= left_boundry - self.player.left
            changed = True
        # Scroll right
        right_boundry = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player.right > right_boundry:
            self.view_left += self.player.right - right_boundry
            changed = True
        # Scroll up
        top_boundry = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player.top > top_boundry:
            self.view_bottom += self.player.top - top_boundry
            changed = True
        # Scroll down
        bottom_boundry = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundry:
            self.view_bottom -= bottom_boundry - self.player.bottom
            changed = True
        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # -- COINS
        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.kill()
            arcade.play_sound(self.coin_sound)
            self.score += 1

        # -- BULLETS
        # Loop through each bullet
        self.bullet_list.update()
        for bullet in hit_list:
            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.bad_list)
            bullet.kill()
        # For every coin we hit, add to the score and remove the coin
        for bad in hit_list:
            bad.kill()
            arcade.play_sound(self.hit_sound)
            arcade.play_sound(self.zombie_sound)

        for bullet in hit_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.wall_list)
            bullet.kill()
            arcade.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.kill()
                arcade.play_sound(self.hit_sound)



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
