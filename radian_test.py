import math
import random

import pygame
import pygame.gfxdraw

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Radian Test")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NAVY = (20, 40, 70)
TEAL = (50, 160, 194)
RANDOM_COLOR = (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
)


class Bubble(object):
    def __init__(self, color):
        self.color = color
        self.radius = random.randint(4, 40)
        self.x = 250
        self.y = 250
        self.direction = random.randint(1, 360)
        self.vel = random.randint(2, 4)
        self.offset = 1

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, (int(self.x), int(self.y)), self.radius, 3
        )
        pygame.gfxdraw.aacircle(
            win, int(self.x), int(self.y), self.radius - 1, self.color
        )
        pygame.gfxdraw.aacircle(
            win, int(self.x), int(self.y), self.radius, self.color
        )
        pygame.gfxdraw.aacircle(
            win, int(self.x), int(self.y), self.radius - 3 - 1, self.color
        )
        pygame.gfxdraw.aacircle(
            win, int(self.x), int(self.y), self.radius - 3, self.color
        )

    def move(self):
        self.move_x = math.cos(self.direction) * self.vel
        self.move_y = math.sin(self.direction) * self.vel
        self.x += self.move_x
        self.y += self.move_y

        self.offset -= 1


bubbles = [Bubble(TEAL)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick(60)
    win.fill(NAVY)

    for bubble in bubbles:
        bubble.draw(win)
        bubble.move()

    if bubble.offset == 0:
        bubbles.append(Bubble(TEAL))

    if len(bubbles) >= 100:
        bubbles.pop(0)

    pygame.display.update()
