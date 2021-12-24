# TTT Version 2 - two player game

import pygame


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Tic Tac Toe')   
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
      self.board_size = 3
      self.board = [] # will be represented by a list of lists
      self.player_1 = 'X'
      self.player_2 = 'O'
      self.turn = self.player_1
      self.create_board()
   
   def create_board(self):
      width = self.surface.get_width()//self.board_size
      height = self.surface.get_height()//self.board_size
      for row_index in range(0,self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            x = col_index *width
            y = row_index * height
            tile = Tile(x,y,width,height,self.surface)
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
            self.handle_mouse_up(event.pos) # event.pos is the (x,y) location of the click
   def handle_mouse_up(self,position):
      # position is bound to event.pos
      #position is the (x,y) location of the click
      for row in self.board:
         for tile in row:
            if tile.select(position, self.turn): # asking the tile have you been selected?
               self.change_turn()
   def change_turn(self):
      if self.turn == self.player_1 :
         self.turn = self.player_2
      else:
         self.turn = self.player_1
      
      
      
            

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      # draw the board
      for row in self.board:
         for tile in row:
            tile.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      pass
   def is_win(self):
      win = False
      row_win = self.is_row_win()
      if row_win:
         win = True
      rerurn win
      
   def is_tie(self):
      pass

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.is_win() or self.is_tie():
         self.continue_game = False

class Tile:
   # A class is a blueprint --- > Properties and behavior

   def __init__(self,x,y,width,height,surface):
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color('white')
      self.border_width= 3
      self.content = ''
      self.flashing = False
      self.surface = surface
   
   def select(self,position, current_player):
      # position is the (x,y) of the location of the click
      selected = False
      if self.rect.collidepoint(position): # Q1 is there a click?
         if self.content == '': # Q2 is the tile unoccupied?
            self.content = current_player
            selected = True
         else:
            self.flashing = True
      return selected
      
   def draw(self):
      # draw the coordinates of each Tile objects
      #string = str(self.rect.x) + ','+ str(self.rect.y)
      #font = pygame.font.SysFont('',40)
      #text_box = font.render(string,True, self.color)
      #location = (self.rect.x,self.rect.y)
      #self.surface.blit(text_box,location)
      if self.flashing:
         pygame.draw.rect(self.surface,self.color,self.rect, 0)
         self.flashing = False
      else:
         pygame.draw.rect(self.surface,self.color,self.rect, self.border_width)
      self.draw_content()
   def draw_content(self):
      font = pygame.font.SysFont('',133) # height of the surface is 400 //3 = 133
      text_box = font.render(self.content,True,self.color)
      # text_box is a pygame.Surface object - get the rectangle from the surface
      rect1 = text_box.get_rect()
      #rect1  <---->  self.rect
      rect1.center = self.rect.center
      location = (rect1.x,rect1.y)
      self.surface.blit(text_box,location)

main()