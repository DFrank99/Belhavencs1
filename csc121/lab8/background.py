import arcade

# window
arcade.open_window(800, 600, "Background")

arcade.set_background_color(arcade.color.DARK_VIOLET)
# AMARANTH_PURPLE
arcade.start_render()

# Floor CAPUT_MORTUUM
arcade.draw_lrtb_rectangle_filled(0, 800, 600 / 3, 0,
arcade.color.DARK_SCARLET)
arcade.draw_lrtb_rectangle_filled(0, 800, 570 / 3, 0,
arcade.color.CAPUT_MORTUUM)
# Moon and stars
arcade.draw_circle_filled(125, 505, 50, arcade.color.CREAM)
point_list = ((565, 470),
              (460, 340),
              (600, 460),
              (250, 274),
              (670, 500),
              (500, 400),
              (676, 460),
              (270, 300),
              (300, 370),
              (200, 540),
              (170, 330),
              (360, 270),
              (170, 430),
              (150, 600),
              (50, 550),
              (70, 400),
              (370, 560),
              (440, 500),
              (510, 510))
arcade.draw_points(point_list, arcade.color.WHITE, 10)
# House
texture1 = arcade.load_texture("house.png")
scale = .3
arcade.draw_texture_rectangle(650, 329, scale * texture1.width,
                              scale * texture1.height, texture1, 0)
# Underground tomb
texture2 = arcade.load_texture("coffin.png")
scale = .1
arcade.draw_texture_rectangle(170, 70, scale * texture2.width,
                              scale * texture2.height, texture2, 50)
# finish then remain til closed
arcade.finish_render()
arcade.run()
