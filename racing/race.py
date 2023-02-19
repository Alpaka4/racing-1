import pygame
import sys
from  config_3 import *
from  grass import Grass
from  road import Road
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
grass=Grass("grass.jpg",screen)
road=Road("road.jpg",screen)
scale = pygame.transform.scale(road.image,(road.image.get_width() // 2,road.image.get_height() // 2))
scale_rect = scale.get_rect()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        clock.tick(FPS)
        grass.update()
        screen.fill(BLACK)
        grass.draw()

        road.draw()
        pygame.display.update()
