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
        theta = random.uniform(1, 360) * math.pi / 180
        self.radius = random.randint(4, 40)
        self.x = random.randint(0, 100) * math.cos(theta) + 400
        self.y = random.randint(0, 100) * math.sin(theta) + 300
        self.offset = 1

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, (int(self.x), int(self.y)), self.radius, 3
        )

    def move(self):
        angles = math.atan2(300 - self.y, 400 - self.x)
        speed = random.randint(1, 2)
        self.distance = math.hypot(400 - self.x, 300 - self.y)
        self.distance = int(self.distance)

        self.move_x = math.cos(angles)
        self.move_y = math.sin(angles)

        if self.distance != 0:
            self.x -= self.move_x * speed
            self.y -= self.move_y * speed

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
    pygame.draw.circle(win, TEAL, (400, 300), 300, 2)

    if bubble.offset == 0:
        bubbles.append(Bubble(WHITE))

    if len(bubbles) >= 100:
        bubbles.pop(0)

    pygame.display.update()
