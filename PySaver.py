import datetime
import pygame
import sys
from pygame.locals import *
import time

pygame.init()

# colours
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# config stuff

image_name = "splatoon-test-patt.webp" # change this to the name of the image you want to use in the images folder

screen = pygame.display.set_mode((0, 0)) # PyGame display

screen_width, screen_height = screen.get_size() # propper image sizing

title = pygame.display.set_caption("PySaver") # Title of app

image = pygame.image.load(f"Images/{image_name}")
image = pygame.transform.scale(image, (screen_width, screen_height))

font = pygame.font.SysFont("segoeui", 85) # set this to whatever font you want it to be

running = True

# actually running
while running: # lol

    time = datetime.datetime.now() # do i even need to explain?
    formatted_time = time.strftime("%I:%M %p") # for 12 hour time
    # formatted_time = time.strftime("%H:%M") # for 24 hour time

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.blit(image, (0, 0)) # i have no idea if this is gonna work
    txtsurf = font.render(f"{formatted_time}", True, white) # set this to a colour that could be used without issue with the image chosen
    screen.blit(txtsurf, (1670, 1000))
    pygame.display.update() # updating :3