#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame
import random
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("game base")
screen = pygame.display.set_mode((500, 500), 0, 32)

# a particle is...
# a thing that exists at a location
# typically moves around
# typically changes over time
# and typically disappears after a certain amount of time

# [loc, velocity, timer]
particles = []
particles2 = []

# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()
    particles.append(
        [
            [mx, my],
            [(random.randint(0, 20) / 10 - 1) * 5, -20],
            random.randint(6, 8),
        ]
    )
    particles2.append(
        [[mx, my], [random.randint(-20, 20) / 2, -10], random.randint(3, 4), 3]
    )

    for particle in particles:
        particle[0][0] += particle[1][0] / particle[2] * 2
        particle[0][1] += particle[1][1] / particle[2] / 2
        particle[2] -= random.randint(4, 10) / 100
        particle[1][1] += 0.1
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            [int(particle[0][0]), int(particle[0][1])],
            int(particle[2]),
        )
        if particle[2] <= 2:
            particles.remove(particle)

    for particle in particles2:
        particle[0][0] += particle[1][0] / 10
        particle[0][1] += particle[1][1] / 10
        particle[2] += random.randint(5, 10) / 10
        particle[1][1] -= 0.1
        particle[3] -= 1
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            [int(particle[0][0]), int(particle[0][1])],
            int(particle[2]),
        )
        if particle[2] <= 2:
            particles2.remove(particle)
        if particle[3] <= 0:
            particle[2] -= 1

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
