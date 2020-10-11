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
        arcade.draw_line(0,50,600,50,arcade.color.BLUE,4)
        arcade.draw_line(0,100,600,100,arcade.color.BLUE,4)
        arcade.draw_line(0,150,600,150,arcade.color.BLUE,4)
        arcade.draw_line(0,200,600,200,arcade.color.BLUE,4)
        arcade.draw_line(0,250,600,250,arcade.color.BLUE,4)
        arcade.draw_line(0,300,600,300,arcade.color.BLUE,4)
        arcade.draw_line(0,350,600,350,arcade.color.BLUE,4)
        arcade.draw_line(0,400,600,400,arcade.color.BLUE,4)
        arcade.draw_line(0,450,600,450,arcade.color.BLUE,4)
        arcade.draw_line(0,500,600,500,arcade.color.BLUE,4)
        arcade.draw_line(0,550,600,550,arcade.color.BLUE,4)
        arcade.draw_line(0,550,600,550,arcade.color.BLUE,4)
        arcade.draw_line(50,600,50,0,arcade.color.BLUE,4)
        arcade.draw_line(100,600,100,0,arcade.color.BLUE,4)
        arcade.draw_line(150,600,150,0,arcade.color.BLUE,4)
        arcade.draw_line(200,600,200,0,arcade.color.BLUE,4)
        arcade.draw_line(250,600,250,0,arcade.color.BLUE,4)
        arcade.draw_line(300,600,300,0,arcade.color.BLUE,4)
        arcade.draw_line(350,600,350,0,arcade.color.BLUE,4)
        arcade.draw_line(400,600,400,0,arcade.color.BLUE,4)
        arcade.draw_line(450,600,450,0,arcade.color.BLUE,4)
        arcade.draw_line(500,600,500,0,arcade.color.BLUE,4)
        arcade.draw_line(550,600,550,0,arcade.color.BLUE,4)
        

# Main code entry point
if __name__ == "__main__":
    app = Welcome()
    arcade.run()