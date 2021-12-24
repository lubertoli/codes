import pygame

def main():
    # initialize pygame -- this is required for rendering fonts
    pygame.init()
    
    # create the window and set its size to 500 width and 400 height
    size = (500, 400)
    screen = pygame.display.set_mode(size)
    
    # set the title of the window
    pygame.display.set_caption("Poke The Dots Prepration v0")
    
    # enter our main gameplay loop, repeating until the user clicks
    # the window's 'close' button
    close_clicked = False
    while not close_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                close_clicked = True
        
        # draw a green circle with radius 100 at position 150, 150 on screen 
        circle_color = pygame.Color('green')
        circle_pos = (150, 150)
        circle_radius = 100
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        
        # draw a blue rectangle with height 50 and with 200 at position 0, 0 on screen
        rect_color = pygame.Color('blue')
        rect_left = 0
        rect_top = 0
        rect_width = 200
        rect_height = 50
        rect_params = pygame.Rect(rect_left, rect_top, rect_width, rect_height)
        pygame.draw.rect(screen, rect_color, rect_params)
        
        # render all drawn objects to the screen
        pygame.display.flip()
        
main()

