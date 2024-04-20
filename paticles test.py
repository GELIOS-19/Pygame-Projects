import math
import random

import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Particle Test")

clock = pygame.time.Clock()


class Particle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(6, 8)
        self.offset = 260
        self.color = random.randint(165, 170)
        self.up_vel = math.cos(self.radius) * -1
        self.side_vel = random.randint(-10, 10) / 10
        self.growth_rate = random.randint(6, 10) / 100
        self.shrink_rate = self.growth_rate + 1

        self.spawn_radius = 150
        self.stagx = x
        self.stagy = y

        self.bloom_effect_x = random.randint(
            int(self.stagx - 75), int(self.stagx + 75)
        )
        self.bloom_effect_y = random.randint(
            int(self.stagy - 70 - 75), int(self.stagy - 70 + 75)
        )
        self.bloom_effect_r = random.randint(20, 30)

    def draw(self, win):
        pygame.draw.circle(
            win,
            (self.color, self.color, self.color),
            (int(self.x), int(self.y)),
            int(self.radius),
        )

        pygame.draw.circle(
            win,
            (self.color, self.color, self.color),
            (int(self.bloom_effect_x), int(self.bloom_effect_y)),
            int(self.bloom_effect_r),
        )

        self.color -= 0.3
        if self.color <= 30:
            self.color = 30

    def movement(self):
        self.x += self.side_vel
        self.y += self.up_vel
        self.radius += self.growth_rate

        if self.offset <= 0:
            self.radius -= self.shrink_rate

    def bloom(self):
        self.move_bloom_x = random.randint(1000, 5000) / 10000
        self.move_bloom_y = random.randint(0, 5) / 10

        if self.bloom_effect_x > self.stagx:
            self.bloom_effect_x += self.move_bloom_x
        elif self.bloom_effect_x < self.stagx:
            self.bloom_effect_x -= self.move_bloom_x
        else:
            self.bloom_effect_x += 0

        self.bloom_effect_y -= self.move_bloom_y

        if self.offset <= 0:
            self.bloom_effect_r -= random.randint(7, 9)

    def do_offset_tick(self):
        self.offset -= 1


particles = [Particle(350, 350)]

while True:
    x, y = pygame.mouse.get_pos()

    particles.append(Particle(x, y))

    for particle in particles:
        particle.draw(win)
        particle.movement()
        particle.bloom()
        particle.do_offset_tick()

        if particle.radius <= 0:
            particles.remove(particle)

        if particle.bloom_effect_r <= 0:
            particle.bloom_effect_r = 0

    pygame.display.update()
    win.fill((0, 0, 0))
