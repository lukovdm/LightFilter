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
        self.active = False
        self.holding = 2

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
        if (not self.down) and self.rect.collidepoint((113, 100)):
            self.rect.center = (113, 100)
            self.active = True
            self.holding = 0
        elif (not self.down) and self.rect.collidepoint((143, 99)):
            self.rect.center = (143, 99)
            self.active = True
            self.holding = 1
        if not (self.rect.collidepoint((143, 99)) or self.rect.collidepoint((113, 100))):
            self.active = False
            self.holding = 2

    def click(self, target):
        if self.rect.collidepoint(target) and self.down == False:
            self.down = True
        elif self.rect.collidepoint(target) and self.down:
            self.down = False

clock = pygame.time.Clock()
run = True
value = 0
cuHo = [0, 0]
schuifValue = 0
valSrf = pygame.Surface((16, 20)).convert_alpha()
font = pygame.font.Font(None, 20)

cuvets = pygame.sprite.RenderPlain(Cuvet(10, "A", (85, 170)), Cuvet(-10, "B", (115, 170)), Cuvet(1, "C", (145, 170)), Cuvet(-1, "D", (175, 170)))

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
    cuHold = [0, 0]
    for cuvet in cuvets.sprites():
        if cuvet.active == True:
            cuHold[cuvet.holding] += 1
            cuHo[cuvet.holding] = cuvet.value
    for i in range(2):
        if cuHold[i] == 0:
            cuHo[i] = 0

    value = abs(abs(schuifValue-cuHo[0]-cuHo[1]) - 90) / 90
    print value * 100

    text1 = font.render(str(int(value * 100)) + "%", True, (0, 0, 0), (255, 255, 255))

    screen.blit(background, (0, 0))
    cuvets.draw(screen)
    screen.blit(text1, (225, 90))

    #drawing other stuff
    pygame.draw.rect(screen, (222, 0, 0), pygame.Rect(20, 90, 20, 20), 0)
    pygame.draw.lines(screen, (0, 0, 0), True, ((70, 130), (70, 110), (75, 110), (75, 90), (65, 90), (65, 110), (70, 110)), 3)
    pygame.draw.lines(screen, (0, 0, 0), False, ((101, 110), (101, 120), (124, 120), (124, 110)), 3)
    pygame.draw.lines(screen, (0, 0, 0), False, ((131, 110), (131, 120), (154, 120), (154, 110)), 3)
    pygame.draw.lines(screen, (0, 0, 0), True, ((180, 130), (180, 110), (185, 110), (185, 90), (175, 90), (175, 110), (180, 110)), 3)
    valSrf.fill((255, 0, 0, value * 255))
    screen.blit(valSrf, (201, 90))
    displayScreen = pygame.draw.lines(screen, (0, 0, 0), True, ((210, 130), (210, 110), (218, 110), (218, 90), (202, 90), (202, 110), (210, 110)), 3)

    pygame.display.flip()
    clock.tick(60)

__author__ = 'luko'
