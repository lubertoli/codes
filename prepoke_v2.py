# Pre-Poke The Dots Version Two
# we are learning how to do the following things:
#
# learn how to animate an object on the screen
#
# Some of the source code contained in this program is not original. It was borrowed from
# a tutorial found on pygame's website. Specifically, we used portions of this tutorial
# to respond to QUIT events and close the PyGame grapical window, to create a
# game window, and to understand how to use the flip() function to render graphics.
# https://www.pygame.org/docs/tut/PygameIntro.html
import pygame


def main():
    # initialize pygame -- this is required for rendering fonts
    pygame.init()
    
    # create the window and set its size to 500 width and 400 height
    size = (500, 400)
    screen = pygame.display.set_mode(size)
    
    # set the title of the window
    pygame.display.set_caption("Poke The Dots Prepration v2")
    
    # initialize game objects
    bg_color = pygame.Color('black')
    
    game_clock = pygame.time.Clock()
    FPS = 30
    
    circle_color = pygame.Color('green')
    circle_pos = [150, 150]
    circle_velocity = [ 1, 1 ]
    circle_radius = 30    
    
    # ===Main Animation Loop
    # Each iteration over the loop will draw the dot at a static location.
    # We will then move the dot a small amount, redraw the dot, and repeat
    # many times a second to give the appearance of motion.
    #
    # This will repeat until the user clikcs the window's 'close' button
    close_clicked = False
    while not close_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                close_clicked = True

        # clear our screen before we draw game objects        
        screen.fill(bg_color)

        # draw our dot to screen and then move its location for next time, to create
        # the illusion of motion
        #circle_pos[0] = circle_pos[0] + circle_velocity[0]
        #circle_pos[1] = circle_pos[1] + circle_velocity[1]
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        for index in range(0,2):
            circle_pos[index] = (circle_pos[index] + circle_velocity[index])        
        
        # render all drawn objects to the screen
        pygame.display.flip()
        game_clock.tick(FPS)
        
main()