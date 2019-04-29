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
BULLET_SCALING = 0.1
COIN_SCALING = 0.3
COIN_COUNT = 20
BAD_COUNT = 10
TEXTURE_RIGHT = 1
TEXTURE_LEFT = 0
NATIVE_SIZE = 128
SPRITE_SIZE = int(NATIVE_SIZE * CHARACTER_SCALING)
EXPLOSION_COUNT = 30

# -- Movement
MOVEMENT_SPEED = 6
GRAVITY = 6
JUMP_SPEED = 15
BULLET_SPEED = 6

# -- INSTRUCTIONS (states game will be in)
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3
window = None

class Explosion(arcade.Sprite):
    """ Explosion animation """
    # Static variable that holds all explosion textures
    explosion_textures = []
    def __init__(self, texture_list):
        super().__init__("images/explosion.png")
        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):
        # Update to the next frame of animation. If we are at the end
        # of our frames, then delete sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()

class Splat(arcade.Sprite):
    """ Explosion animation """
    # Static variable that holds all explosion textures
    explosion_textures = []
    def __init__(self, texture_list):
        super().__init__("images/splat.png")
        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):
        # Update to the next frame of animation. If we are at the end
        # of our frames, then delete sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()

class MyGame(arcade.Window):
    """ Main application"""
    def __init__(self):
    # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "DEMI-lition")

        # BACKGROUND & INSTRUCTIONS
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
        self.background = None
        self.current_room = 0
        self.frame_count = 0
        self.game_over = False

        # SPRITE LIST
        self.all_sprites_list = None
        self.wall_list = None
        self.coin_list = None
        self.bullet_list = None
        self.physics_engine = None
        self.player_list = None
        self.explosions_list = None

        # PLAYER SPRITE
        self.player = None
        self.score = 0
        self.player_sprite = None
        self.bad_list = None

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

    def setup(self):

        # SCORE
        self.score = 0

        # CREATE SPRITE LIST
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()
        self.player = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()

        # SETUP PLAYER
        self.player = arcade.AnimatedWalkingSprite()

        character_scale = 0.5
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
        self.player.scale = 0.4
        self.player_list.append(self.player)

        # -- ZOMBIE
        # Loop to place some enemies
        for bad in range(BAD_COUNT):
            # -- Draw an enemy on the ground
            bad = arcade.Sprite("zombie/idle/idle_01.png", CHARACTER_SCALING)

            bad.bottom = SPRITE_SIZE
            bad.left = SPRITE_SIZE * 2

            # Set enemy initial speed
            bad.change_x = 2
            self.bad_list.append(bad)

            # -- Draw a enemy on the platform
            bad = arcade.Sprite("zombie/idle/idle_01.png", CHARACTER_SCALING)

            bad.bottom = SPRITE_SIZE * 4
            bad.left = SPRITE_SIZE * 4

            # Set boundaries on the left/right the enemy can't cross
            bad.boundary_right = SPRITE_SIZE * 8
            bad.boundary_left = SPRITE_SIZE * 3
            bad.change_x = 2
            self.bad_list.append(bad)

            # -- Avoid walls
            # Boolean variable if we successfully placed the coin
            bad_placed_successfully = False

            # Keep trying until success
            while not bad_placed_successfully:
                # Position coin
                bad.center_x = random.randrange(SCREEN_WIDTH)
                bad.center_y = random.randrange(SCREEN_HEIGHT)

                # See if coin is hitting wall
                wall_hit_list = arcade.check_for_collision_with_list(bad, self.wall_list)

                # See if coin is hitting another coin
                bad_hit_list = arcade.check_for_collision_with_list(bad, self.bad_list)

                if len(wall_hit_list) == 0 and len(bad_hit_list) == 0:
                    # It is!
                    bad_placed_successfully = True

            # Add the coin to the lists
            self.bad_list.append(bad)

        # Loop to place some coins to pick up
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("images/coin.png", COIN_SCALING)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            # set up angle to spin
            coin.angle = random.randrange(360)
            coin.change_angle = random.randrange(-5, 6)


            # -- Avoid walls
            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if coin is hitting wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        # -- WALLS
        # Loop floor horizontal
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)

            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)

        # platforms
         # Create a row of boxes
        for x in range(373, 650, 50):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
        for x in range(950, 1000, 50):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
        for x in range(373, 650, 50):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)
        for x in range(50, 200, 50):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)
        for x in range(373, 650, 50):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)
        for x in range(775, 1000, 50):
            wall = arcade.Sprite("images/blue.png", WALL_SCALING)
            wall.center_x = x
            wall.center_y = 450
            self.wall_list.append(wall)



        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render screen """
        # Has to render before anything can happen
        arcade.start_render()
        # Sprites
        self.wall_list.draw()
        self.player.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.bad_list.draw()
        self.explosions_list.draw()

        # Render tests
        arcade.draw_text(f"Starie Stars: {self.score}", 10, 20, arcade.color.BLACK, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        """click mouse button"""
        # sound
        arcade.play_sound(self.shoot_sound)
        # bullet
        bullet = arcade.Sprite("images/bullet.png", BULLET_SCALING)
         # Position bullet at player
        start_x = self.player.center_x
        start_y = self.player.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need
        # add self.view_bottom and self.view_left.
        dest_x = x
        dest_y = y

        #math to calculate bullet to the destination.
        # Calculate angle in radians between the start points
        # and end points. angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Angle the bullet so it doesn't look like it is flying sideways.
        bullet.angle = math.degrees(angle)

        # accounting angle, calculate change_x and change_y. Velocity=how fast the bullet travels.
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        # Add bullet to lists
        self.bullet_list.append(bullet)

    def on_key_press(self, key, modifiers):
        """Key is pressed """
        # Regular Movement
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """User releases key """
        # Regular movement
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0

    def update(self, delta_time):
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.wall_list.update()
        self.player.update_animation()
        self.coin_list.update()
        self.explosions_list.update()
        self.physics_engine.update()

        # Generate a list of all sprites that collided with the player.
        for bullet in self.bullet_list:
        # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.bad_list)
            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                explosion = Explosion(self.explosion_texture_list)
                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y
                self.explosions_list.append(explosion)
                arcade.play_sound(explosion)
                bullet.kill()

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.kill()

            #zombie we hit dies
            for bad in hit_list:
                bad.kill()
                # play sound
                arcade.play_sound(self.hit_sound)

            bullet_hit_list = arcade.check_for_collision_with_list(bullet, self.wall_list)
            if len(bullet_hit_list) > 0:
                bullet.kill()

            hit_list = arcade.check_for_collision_with_list(bullet, self.player)
            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                explosion = Splat(self.explosion_texture_list)
                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y
                self.explosions_list.append(explosion)
                arcade.play_sound(explosion)
                bullet.kill()

                # Get rid of the bullet when it hits wall
                bullet_hit_list = arcade.check_for_collision_with_list(bullet, self.wall_list)
                if len(bullet_hit_list) > 0:
                    bullet.kill()

        self.frame_count += 1
        for bad in self.bad_list:
            # First, calculate angle to player
            # only when the bullet fires rotate the enemy to face the player each frame
            # Position the start at the enemy's current location
            start_x = bad.center_x
            start_y = bad.center_y

            # Get the destination location for the bullet
            dest_x = self.player.center_x
            dest_y = self.player.center_y

            #calculate how to get the bullet to destination
            #in radians between the start points and end points
            #angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            bad.angle = math.degrees(angle)

        self.bullet_list.update()

        # Update the player based on the physics engine
        if not self.game_over:
            # Move the enemies
            self.bad_list.update()
            # Check each enemy
            for bad in self.bad_list:
                # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(bad, self.wall_list)) > 0:
                    bad.change_x *= -1
                # If the enemy hit the left boundary, reverse
                elif bad.boundary_left is not None and bad.left < bad.boundary_left:
                    bad.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif bad.boundary_right is not None and bad.right > bad.boundary_right:
                    bad.change_x *= -1
            # Update the player using the physics engine
            self.physics_engine.update()

            # See if the player hit a zombie. If so, game over.
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.bad_list)) > 0:
                self.game_over = True


def main():
    """Main Method"""
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
