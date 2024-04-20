import random

import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Moving Dots")

bg = (255, 255, 255)

clock = pygame.time.Clock()


def random_number(minimum, maximum):
    return random.randint(minimum, maximum)


class Dot(object):

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def draw_dot(limit):
    for i in range(random_number(1, limit)):
        point = Dot(
            random_number(1, 500),
            random_number(1, 500),
            random_number(5, 10),
            (
                random_number(1, 255),
                random_number(1, 255),
                random_number(1, 255),
            ),
        )
        point.draw(win)
        pygame.display.update()


run = True

# main loop
while run:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_dot(100)
    win.fill((255, 255, 255))
