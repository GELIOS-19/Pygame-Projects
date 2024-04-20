import random

import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("bubbles")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
NAVY = (30, 40, 70)


class Bubble(object):

    def __init__(self):
        self.x = 250
        self.y = 250
        self.color = WHITE
        self.radius = random.randrange(10, 50)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y


def draw_environment(bubble):
    win.fill(BLACK)
    bubble.draw(win)
    pygame.display.update()
    bubble.move()


def main():
    bubble1 = Bubble()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(bubble1)
        clock.tick(60)


if __name__ == "__main__":
    main()
