import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption('Filter the light')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


class Cuvet(pygame.sprite.Sprite):
    def __init__(self, value, letter, pos):
        pygame.sprite.Sprite.__init__(self)
        self.value = value
        self.letter = letter
        self.down = False

        self.font = pygame.font.Font(None, 20)
        self.text = self.font.render(self.letter, 1, (0, 0, 0))
        self.image = pygame.Surface([20, 40]).convert_alpha()
        self.image.fill((147, 202, 250, 100))
        pygame.draw.lines(self.image, (32, 101, 161), False, ((1, 0), (1, 39), (18, 39), (18, 0)), 3)
        self.image.blit(self.text, (6, 20))

        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        if self.down:
            pos = pygame.mouse.get_pos()
            self.rect.center = pos

    def click(self, target):
        if self.rect.collidepoint(target) and self.down == False:
            self.down = True
        elif self.rect.collidepoint(target) and self.down:
            self.down = False

clock = pygame.time.Clock()
run = True

cuvets = pygame.sprite.RenderPlain(Cuvet(10, "A", (100, 150)), Cuvet(170, "B", (130, 150)), Cuvet(1, "C", (160, 150)), Cuvet(179, "D", (190, 150)))

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
        if event.type == MOUSEBUTTONDOWN:
            for cuvet in cuvets.sprites():
                cuvet.click(event.pos)
        if event.type == MOUSEBUTTONUP:
            for cuvet in cuvets.sprites():
                cuvet.click(event.pos)

    cuvets.update()

    screen.blit(background, (0, 0))
    cuvets.draw(screen)

    #drawing other stuff
    pygame.draw.circle(screen, (222, 207, 0), (30, 100), 10)
    pygame.draw.lines(screen, (0, 0, 0), True, ((70, 130), (70, 110), (75, 110), (75, 90), (65, 90), (65, 110), (70, 110)), 3)
    pygame.draw.lines(screen, (0, 0, 0), False, ((101, 110), (101, 120), (124, 120), (124, 110)), 3)
    pygame.draw.lines(screen, (0, 0, 0), False, ((131, 110), (131, 120), (154, 120), (154, 110)), 3)

    pygame.display.flip()
    clock.tick(60)

__author__ = 'luko'
