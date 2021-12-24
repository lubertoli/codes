# TTT Version 1

import pygame,random,time


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Memory')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 


# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      self.board_size = 4
      self.image_list = []
      self.load_images()
      self.image_list = self.image_list + self.image_list
      random.shuffle(self.image_list)
      self.board = [] # will be represented by a list of lists
      self.create_board()
      self.score = 0
      self.selected_tiles = []
      self.count = 0
   
   def load_images(self):
      # loads images and append to a list of images
      image1 = pygame.image.load('image1.bmp')
      self.image_list.append(image1)
      image2 = pygame.image.load('image2.bmp')
      self.image_list.append(image2)      
      image3 = pygame.image.load('image3.bmp')
      self.image_list.append(image3)
      image4 = pygame.image.load('image4.bmp')
      self.image_list.append(image4)
      image5 = pygame.image.load('image5.bmp')
      self.image_list.append(image5)
      image6 = pygame.image.load('image6.bmp')
      self.image_list.append(image6)
      image7 = pygame.image.load('image7.bmp')
      self.image_list.append(image7)
      image8 = pygame.image.load('image8.bmp')
      self.image_list.append(image8)      
   
   def create_board(self):
      #creates the board with the tiles
      for row_index in range(0,self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            image = self.image_list.pop()
            width = image.get_width()
            height = image.get_height()
            x = col_index *width
            y = row_index * height
            tile = Tile(x,y,width,height,image,self.surface)
            row.append(tile)
         self.board.append(row)
         
         
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
            self.handle_mouse_up(event.pos)
            
   def handle_mouse_up(self,position):
      # exposes the tile when the tile is clicked
      for row in self.board:
         for tile in row:
            if tile.select(position) and tile.is_hidden():
               tile.expose()
               self.selected_tiles.append(tile)
               
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.surface.fill(self.bg_color) # clear the display surface first
      # draw the board
      for row in self.board:
         for tile in row:
            tile.draw()
      self.draw_score()      
      pygame.display.update() # make the updated surface appear on the display

   def draw_score(self):
      score_string = str(self.score)
      # step 1 create a font object
      font_size = 70
      fg_color = pygame.Color('white')
      font = pygame.font.SysFont('',font_size)
      # step 2 render the font
      text_box = font.render(score_string, True,fg_color,self.bg_color)
      # step 3  compute the location 
      location = (self.surface.get_width() - text_box.get_width(),0)
      # step 4 blit the source surface on the target surface at the specified location
      self.surface.blit(text_box,location)   
   
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.score = pygame.time.get_ticks()//1000
      if len(self.selected_tiles) == 2:  
         if self.selected_tiles[1].is_equal(self.selected_tiles[0]) == True:
            self.count = self.count + 2
         else:
            time.sleep(0.5)
            self.selected_tiles[1].hide()
            self.selected_tiles[0].hide()
         self.selected_tiles = []             
         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.count == 16:
         self.continue_game = False

class Tile:
   # A class is a blueprint --- > Properties and behavior

   def __init__(self,x,y,width,height,image,surface):
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color('white')
      self.border_width= 3
      self.hidden_image = pygame.image.load('image0.bmp')
      self.content = image
      self.hidden = True
      self.surface = surface
      
   def select(self,position):
      # detects if the tile was clicked
      selected = False
      if self.rect.collidepoint(position):
         selected = True
      return selected
   
   def expose(self):
      # exposes the tile
         self.hidden = False
   
   def is_equal(self,other):
      # determines if the two tiles match or not
      # returns True or False 
      return self.content == other.content

   def hide(self):
      # hides the tile
         self.hidden = True
   
   def is_hidden(self):
      # returns if the tile is hidden or exposed
      return self.hidden

   def draw(self):
      # draws the tiles with either the hidden image or the exposed image
      location = (self.rect.x,self.rect.y)
      if self.hidden == True:
         self.surface.blit(self.hidden_image,location)
      else:
         self.surface.blit(self.content,location)
      pygame.draw.rect(self.surface,self.color,self.rect, self.border_width)
   
main()