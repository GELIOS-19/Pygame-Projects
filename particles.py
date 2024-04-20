import pygame
import random
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("game base")
screen = pygame.display.set_mode((1920, 1080), 0, 32)

# a particle is...
# a thing that exists at a location
# typically moves around
# typically changes over time
# and typically disappears after a certain amount of time

# [loc, velocity, timer]
particles = []
particles2 = []
i = 0

# Loop ------------------------------------------------------- #
while i < 60:

    # Background --------------------------------------------- #
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    for i in range(3):
        particles.append(
            [[mx, my], [random.randint(-1, 1), -2], random.randint(15, 20)]
        )
        particles2.append(
            [
                [mx, my],
                [random.randint(-700, 700) / 100, 2],
                random.randint(15, 20),
            ]
        )

    for particle in particles:
        randc = random.randint(147, 150)
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.3
        particle[1][1] += 0.01
        pygame.draw.circle(
            screen,
            (randc, randc, randc),
            [int(particle[0][0]), int(particle[0][1])],
            int(particle[2]),
        )
        randc -= 5
        if particle[2] <= 0:
            particles.remove(particle)

    ##    for particle in particles2:
    ##        randc = random.randint(147, 150)
    ##        particle[0][0] += particle[1][0]
    ##        particle[0][1] += particle[1][1]
    ##        particle[2] += 0.3
    ##        particle[1][1] -= 0.1
    ##        pygame.draw.circle(screen, (randc, randc, randc), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
    ##        randc -= 5
    ##        if particle[2] >= 25:
    ##            particle[2] -= 0.2
    ##            if particle[2] <= 0:
    ##                particles.remove(particle)
    ##

    i += 1

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
