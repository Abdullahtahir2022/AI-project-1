# Basic arcade program using objects
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"
PLAYER_SCALING = 0.5

# Classes
class Welcome(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
         # Background image will be stored in this variable
        self.background = None
        # Set up the player info
        self.player_sprite = None
        
        
        
    

    def on_draw(self):
        """Called whenever you need to draw your window
        """
        self.background = arcade.load_texture("sample.jpeg")
                
        
        self.player_sprite = arcade.Sprite("sample.jpeg", PLAYER_SCALING)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        

        # Clear the screen and start drawing
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        

        # Draw a blue circle
        for x in range(50,600,50):
            arcade.draw_line(0,x,600,x,arcade.color.WHITE_SMOKE,4)
        for y in range(50,600,50):
            arcade.draw_line(y,600,y,0,arcade.color.WHITE_SMOKE,4)

        

# Main code entry point
if __name__ == "__main__":
    app = Welcome()
    arcade.run()