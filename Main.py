import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480))
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

cuvets = pygame.sprite.RenderPlain(Cuvet(10, "A", (100, 10)), Cuvet(170, "B", (100, 50)), Cuvet(1, "C", (100, 100)), Cuvet(179, "D", (100, 150)))

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


    pygame.display.flip()
    clock.tick(60)

__author__ = 'luko'
