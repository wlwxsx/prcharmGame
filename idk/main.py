import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
#title, icon
pygame.display.set_caption("This Game")



#quit loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
