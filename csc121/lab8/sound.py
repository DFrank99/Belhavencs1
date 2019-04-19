import arcade


class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")

        # Load the sound when application starts
        self.laser_sound = arcade.load_sound("laser.ogg")

    def on_key_press(self, key, modifiers):

        # If user hits space sound plays
        
