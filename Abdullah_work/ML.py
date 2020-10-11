# Basic arcade program using objects
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"

PLAYER_SCALING = 0.5
SPRITE_SCALING_PLAYER = 0.2


# Classes
class Welcome(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.player_sprite = None

        # Set the background window
         # Background image will be stored in this variable
        self.background = None

    def setup(self):
        self.player_list = arcade.SpriteList()




        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("snail.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 45
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)







    def on_draw(self):
        """Called whenever you need to draw your window
        """
        self.background = arcade.load_texture("sample.jpeg")
        # Clear the screen and start drawing
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.player_list.draw()


        # Draw a blue circle
        for x in range(100,600,100):
            arcade.draw_line(0,x,600,x,arcade.color.WHITE_SMOKE,4)
        for y in range(100,600,100):
            arcade.draw_line(y,600,y,0,arcade.color.WHITE_SMOKE,4)




app = Welcome()
app.setup()
arcade.run()
