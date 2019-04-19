class Address():
    def __init__(self, name):
        self.name = ' '.join(s.capitalize() for s in name.split())
        self.line1 = line1
        self.line2 = line2
        self.city = city.capitalized()
        self.state = state
        if not sip.isdigit():
            print("Problem! Zip code is not a digit.")
            self.zip = zip

# Print address to screen
def print_address(self):
    print(address.name)
    # If there is a line1 in address, print it
    if len(address.line1) > 0:
        print(self.line1)
    # If there is a line2 in address, print it
    if len(address.line2) > 0:
        print(self.line2)
    print(self.city + "," + self.state + " " + self.zip)

# Drawing windows
import random

import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#random ball
def random_color():
    return(
        rng.randrange(0, 256)
        rng.randrange(0, 256)
        rng.randrange(0, 256)
    )
def random_ball():
    rng = random.Random()

    radius = rng.randrange(5, 31)
    x = random.randrange(raidus, SCREEN_WIDTH - radius)
    y = random.randrange(raidus, SCREEN_HEIGHT - radius)

    dx = rng.randrange(1,11)
    if rng.random() < 0.5:
        dx *= -1
    dy = rng.randrange(1, 11)
    if rng.random() < 0.5:
        dx *= -1

    color = random_color(rng)
    return Ball(x, y, dx, dy, radius, color)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call parent class's init function
        super().__itit__(width, height, title)

        # Background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        # Called to draw window
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def update(self, delta_time):
        # called update our objects; 60 tiems per second
        self.ball_x += 1
        self_call_y += 1
def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()

    self.balls = [
        random_ball() for i in range(50)
    ]
    def on_draw():
main()
