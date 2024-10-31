import pygame

# Initial Pygame
pygame.init()

# The display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day and Night Cycle")

# Colors
BLUE = (135, 206, 235)  # day sky 
DARK_BLUE = (25, 25, 112)  # night sky
YELLOW = (255, 255, 0)  # Yellow sun
WHITE = (255, 255, 255)  # White moon
BROWN = (139, 69, 19)    # Brown house
RED = (255, 0, 0)        # Red roof
YELLOW_WINDOW = (255, 255, 0)  # Yellow for the open window

# Initial positions and sizes
sun_x = 0
sun_y = 100
sun_size = 40  # Initial sun size
moon_x = -100  # Start the moon off-screen
moon_size = 40  # Initial moon size
night = False

#loopa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background
    if not night:
        screen.fill(BLUE)  # Daytime sky
    else:
        screen.fill(DARK_BLUE)  # Nighttime sky

    # house
    pygame.draw.rect(screen, BROWN, (350, 400, 100, 100))  # House body
    pygame.draw.polygon(screen, RED, [(350, 400), (450, 400), (400, 350)])  # Roof

    # window
    if not night:  # Open window during the day
        pygame.draw.rect(screen, YELLOW_WINDOW, (375, 450, 50, 50))  # Open window
    else:  # Closed window at night
        pygame.draw.rect(screen, BROWN, (375, 450, 50, 50))  # Closed window

    # changes positions and sizes
    if not night:
        sun_x += 4  # Move the sun to the right
        sun_size += 0.1  # Increase the size of the sun
        if sun_x > WIDTH:  
            sun_x = WIDTH  # Stop the sun 
            night = True  # Switch to night
            sun_size = 40  # Reset sun's size
    else:
        moon_x += 4  # Move the moon to the right
        moon_size += 0.1  # Increase the size of the moon
        if moon_x > WIDTH:  
            sun_x = 0  # Reset sun position
            moon_x = -100  # Reset moon 
            night = False  # Switch back to day
            moon_size = 40  # Reset moon's size 

    # Draw the sun or moon
    if not night:
        pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), int(sun_size))  # Draw the sun
    else:
        pygame.draw.circle(screen, WHITE, (moon_x, 100), int(moon_size))  # Draw the moon

    # The display
    pygame.display.flip()
    pygame.time.delay(30)  # Control the speed of the animation


pygame.quit()

