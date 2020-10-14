import arcade
import os
import random

MENU_SCREEN_WIDTH = 700
MENU_SCREEN_HEIGHT = 600

SPRITE_SCALING = 0.13
COIN_SCALE = 0.13
COIN_START_SCALE = 35 # like x= 35 and y = 35 of starting

# i have decided to keep each block of width = 70 and height = 70
# now if user want 3 * 3 board , we will simply do, 3*70 = 210 size 

# We can go till 10 X 10
# Grid is made using lines, not actual Grid 

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Sprite Bouncing Coins"
GRID_GAP = 70



class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)
    def on_draw(self):
        arcade.start_render()
        back = arcade.load_texture("b.jpeg")
        arcade.draw_lrwh_rectangle_textured(0, 0, MENU_SCREEN_WIDTH, MENU_SCREEN_HEIGHT,back)
        # arcade.draw_rectangle_filled(WIDTH //2 , HEIGHT//2,WIDTH - (WIDTH//4),HEIGHT- (HEIGHT//4),arcade.color.LIGHT_RED_OCHRE)
        arcade.draw_text("Snails Game", MENU_SCREEN_WIDTH/2, MENU_SCREEN_HEIGHT-100,
                         arcade.color.ANTIQUE_WHITE, font_size=40, anchor_x="center",bold=True)
        arcade.draw_text("Click Here TO Play The Game", MENU_SCREEN_WIDTH//2, MENU_SCREEN_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyGame()
        self.window.show_view(game_view)
        game_view.setup()

class MyGame(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.background = None
        self.coin_list = None
        self.splash_list = None
        # self.wall_list = None
    
    def setup(self):

        # Sprite lists
        # self.wall_list = arcade.SpriteList()
        # self.coin_list = arcade.SpriteList()
        self.background = arcade.load_texture("back.jpg")
        self.coin_list = arcade.SpriteList()
        self.splash_list = arcade.SpriteList()
        
        # Here is First snail creaeted at x = 35 , y =35
        coin = arcade.Sprite("snailone.png")
        # Creating a splash
        splash = arcade.Sprite("splash.png")

        """ x = 35 , y = 35 
            and add 70 to loop through
        """
        coin.center_x = COIN_START_SCALE
        coin.center_y = COIN_START_SCALE
        splash.center_x = COIN_START_SCALE
        splash.center_y = COIN_START_SCALE
        splash.scale = 0.131
        coin.scale = 0.13
        print(coin.bottom)
        print(coin.left)
        
        print(coin.width)
        print(coin.height)
        self.coin_list.append(coin)
        self.splash_list.append(splash)

         #  First snail done


        # Here is Oponent snail created 
        coin = arcade.Sprite("snailone.png",mirrored= True)
        # Creating a splash
        splash = arcade.Sprite("splash.png" , mirrored=True)

        """ x = 35 , y = 35 
            and add 70 to loop through
        """
        coin.center_x = splash.center_x= SCREEN_WIDTH- COIN_START_SCALE
        coin.center_y = splash.center_y = SCREEN_HEIGHT - COIN_START_SCALE
        
        splash.scale = 0.131
        coin.scale = 0.13
        print(coin.bottom)
        print(coin.left)
        
        print(coin.width)
        print(coin.height)
        self.coin_list.append(coin)
        self.splash_list.append(splash)


        # # Generate Sprite in loop in x axis
        # self.coin_list.append(coin)
        # for x in range(35,SCREEN_WIDTH,70):
        #     coin = arcade.Sprite("snailone.png")
        #     coin.scale = 0.13
        #     coin.center_x = x
        #     coin.center_y = 35
        #     self.coin_list.append(coin)
        # # Generate Sprite in loop in y axis
        # for x in range(SCREEN_WIDTH-35 , 0, -70):
        #     coin = arcade.Sprite("snailtwo.png",mirrored=True)
        #     coin.scale = 0.13
        #     coin.center_x = x
        #     coin.center_y = SCREEN_HEIGHT - 35
        #     self.coin_list.append(coin)



        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        

        # list for all possible x places for sprite    
        list_for_x = []
        for x in range(COIN_START_SCALE,SCREEN_WIDTH,70):
            list_for_x.append(x)
        print(list_for_x)

        # list for all possible y places for sprite    
        list_for_y = []
        for y in range(COIN_START_SCALE,SCREEN_HEIGHT,70):
            list_for_y.append(y)
        print(list_for_y)      

        # Make random moves
        # coin = arcade.Sprite("snailone.png")
        # splash = arcade.Sprite("splash.png")
        # coin.center_x = splash.center_x = random.choice(list_for_x)
        # coin.center_y = splash.center_y= random.choice(list_for_y)
       
        # coin.scale = 0.13
        # splash.scale = 0.13
        # self.coin_list.append(coin)
        # self.splash_list.append(splash)
        
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.set_viewport(0, SCREEN_WIDTH , 0, SCREEN_HEIGHT )
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        # Drawing Lines
        
        for x in range(0, SCREEN_WIDTH+1, GRID_GAP):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, arcade.color.WHITE_SMOKE, 3)

        for x in range(0,SCREEN_HEIGHT+1, GRID_GAP):
            arcade.draw_line(0, x, SCREEN_WIDTH, x, arcade.color.WHITE_SMOKE, 3)
        self.splash_list.draw()
        self.coin_list.draw()
        
        # Draw all the sprites.
        # self.wall_list.draw()
        # self.coin_list.draw()
        # myText = "Arsalan"
        # for rows in range(0,SCREEN_WIDTH,GRID_GAP):
        #     for columns in range(0,SCREEN_HEIGHT,GRID_GAP):
        #         arcade.draw_text(myText,rows,columns,arcade.color.AERO_BLUE,bold=True)
        
    def on_update(self, delta_time):
        self.coin_list.update()
        self.splash_list.update()
        """ Movement and game logic """
        for x in range(COIN_START_SCALE,SCREEN_WIDTH,GRID_GAP):
            self.coin_list[0].center_x = x
            splash = arcade.Sprite("splash.png" ) 
            splash.center_x = x
            splash.center_y = COIN_START_SCALE
            splash.scale = 0.131
            self.splash_list.append(splash)
            self.splash_list.draw()
       


def main():
    """ Main method """

    window =  arcade.Window(MENU_SCREEN_WIDTH, MENU_SCREEN_HEIGHT ,"Different Views Example")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()


