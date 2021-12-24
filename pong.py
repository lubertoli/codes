
import pygame,random

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Pong')   
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
      self.paddle_increment = 10
      self.paddle1 = Paddle(50,175,10,50,'white',self.surface)
      self.paddle2 = Paddle(450,175,10,50,'white',self.surface)
      self.ball = Ball('white', 5, [250, 200], [4, 4], self.surface)
      self.score1 = 0
      self.score2 = 0
      
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
         elif event.type == pygame.KEYDOWN:
            self.handle_key_down(event)
         elif event.type == pygame.KEYUP:
            self.handle_key_up(event)
   
   def handle_key_down(self,event):
      # reponds to KEYDOWN event
      # - self is the Game object
      if event.key == pygame.K_l:
         self.paddle2.set_vertical_velocity(self.paddle_increment)
      elif event.key == pygame.K_p:
         self.paddle2.set_vertical_velocity(-self.paddle_increment)
      if event.key == pygame.K_a:
         self.paddle1.set_vertical_velocity(self.paddle_increment)
      elif event.key == pygame.K_q:
         self.paddle1.set_vertical_velocity(-self.paddle_increment)      
   
   def handle_key_up(self,event):
      # responds to KEYUP event
      # - self is the Game object
      if event.key == pygame.K_l:
         self.paddle2.set_vertical_velocity(0)
      elif event.key == pygame.K_p:
         self.paddle2.set_vertical_velocity(0) 
      if event.key == pygame.K_a:
         self.paddle1.set_vertical_velocity(0)
      elif event.key == pygame.K_q:
         self.paddle1.set_vertical_velocity(0)         
         

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.paddle1.draw()
      self.paddle2.draw()
      self.ball.draw()
      self.draw_score1()
      self.draw_score2()
      pygame.display.update() # make the updated surface appear on the display
      
   def draw_score1(self):
      score_string1 = str(self.score1)
      # step 1 create a font object
      font_size = 80
      fg_color = pygame.Color('white')
      font = pygame.font.SysFont('',font_size)
      # step 2 render the font
      text_box = font.render(score_string1, True,fg_color,self.bg_color)
      # step 3  compute the location 
      location = (0,0)
      # step 4 blit the source surface on the target surface at the specified location
      self.surface.blit(text_box,location)
      
   def draw_score2(self):
      score_string2 = str(self.score2)
      # step 1 create a font object
      font_size = 80
      fg_color = pygame.Color('white')
      font = pygame.font.SysFont('',font_size)
      # step 2 render the font
      text_box = font.render(score_string2, True,fg_color,self.bg_color)
      # step 3  compute the location 
      location = (self.surface.get_width() - text_box.get_width(),0)
      # step 4 blit the source surface on the target surface at the specified location
      self.surface.blit(text_box,location)
      
   def decide_continue(self):
      if self.score1 == 11 or self.score2 == 11:
         self.continue_game = False
         return self.continue_game
   
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.paddle1.move()
      self.paddle2.move()
      self.ball.move(self.paddle1,self.paddle2)
      if self.ball.center[0] < self.ball.radius:
         self.score2 = self.score2 + 1
      if self.ball.center[0] + self.ball.radius > (self.surface.get_size())[0]:
         self.score1 = self.score1 + 1
      
   
class Paddle:
   # An object in this class represents a Paddle that moves
   
   def __init__(self,x,y,width,height,color,surface):
      # - self is the Paddle object
      # - x, y are the top left corner coordinates of the rectangle of type int
      # - width is the width of the rectangle of type int
      # - height is the height of the rectangle of type int
      # - surface is the pygame.Surface object on which the rectangle is drawn
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color(color)
      self.surface = surface
      self.vertical_velocity = 0  # paddle is not moving at the start
   
   def draw(self):
      # -self is the Paddle object to draw
      pygame.draw.rect(self.surface,self.color,self.rect)
   
   def set_vertical_velocity(self,vertical_distance):
      # set the vertical velocity of the Paddle object
      # -self is the Paddle object
      # -vertical_distance is the int increment by which the paddle moves vertically
      self.vertical_velocity = vertical_distance
   def move(self):
      # moves the paddle such that paddle does not move outside the window
      # - self is the Paddle object
      self.rect.move_ip(0,self.vertical_velocity)
      if self.rect.bottom >= self.surface.get_height():
         self.rect.bottom = self.surface.get_height()
      elif self.rect.top  <= 0:
         self.rect.top = 0

class Ball:
   # An object in this class represents a Ball that moves 
   
   def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
      # Initialize a Ball.
      # - self is the Ball to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the ball
      # - radius is the int pixel radius of the ball
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(ball_color)
      self.radius = ball_radius 
      self.center = ball_center
      self.velocity = ball_velocity
      self.surface = surface
   
   def move(self,paddle1,paddle2):
      # Change the location of the Ball by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Ball
      size = self.surface.get_size() # get_size is a method in pygame.Surface class and it returns a tuple (width, height)
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])
         if self.center[i] < self.radius : # left or the top edge 
            self.velocity[i] = -self.velocity[i]
         if self.center[i] + self.radius > size[i]: # right or bottom edge
            self.velocity[i] = - self.velocity[i]
            size = self.surface.get_size() # get_size is a method in pygame.Surface class and it returns a tuple (width, height)
      # ball bounces back when colliding with paddles from the front
      if self.velocity[0] < 0:
         if paddle1.rect.collidepoint(self.center):
            self.velocity[0] = -self.velocity[0]
      if self.velocity[0] > 0:
         if paddle2.rect.collidepoint(self.center):
            self.velocity[0] = -self.velocity[0]
              
               
   def draw(self):
      # Draw the ball on the surface
      # - self is the Ball
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

main()         
      
      

