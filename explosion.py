import math
import random

import pygame

pygame.init()

win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Particle Test")

clock = pygame.time.Clock()


class Particle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stagx = x
        self.stagy = y
        self.radius = random.randint(6, 8)
        self.offset = 400
        self.color = random.randint(165, 170)
        self.up_vel = math.cos(self.radius) * -1
        self.side_vel = random.randint(-10, 10) / 10
        self.growth_rate = random.randint(6, 10) / 100
        self.shrink_rate = self.growth_rate + 1

    def draw(self, win):
        pygame.draw.circle(
            win,
            (self.color, self.color, self.color),
            (int(self.x), int(self.y)),
            int(self.radius),
        )

        self.color -= 0.2
        if self.color <= 30:
            self.color = 30

    def movement(self):
        self.x += self.side_vel
        self.y += self.up_vel

        if self.offset <= 100 and not self.y > self.stagy:
            self.up_vel += 0.007

        self.radius += self.growth_rate

        if self.offset <= 0:
            self.radius -= self.shrink_rate

        self.offset -= 1


class Bloom_Particle(object):
    def __init__(self, x, y):
        self.spawn_radius = 50
        self.stagx = x
        self.stagy = y

        self.offset = 400
        self.color = random.randint(165, 170)

        self.growth_rate = random.randint(6, 10) / 100
        self.shrink_rate = self.growth_rate + 1

        self.bloom_theta = random.randint(1, 360)
        self.bloom_effect_x = (
            random.randint(0, self.spawn_radius) * math.cos(self.bloom_theta)
            + self.stagx
        )
        self.bloom_effect_y = (
            random.randint(0, self.spawn_radius) * math.sin(self.bloom_theta)
            + self.stagy
        )
        self.bloom_effect_r = random.randint(25, 35)

        self.bloom_up_vel = math.cos(self.bloom_effect_r) * -1

    def bloom(self):
        pygame.draw.circle(
            win,
            (self.color, self.color, self.color),
            (int(self.bloom_effect_x), int(self.bloom_effect_y)),
            int(self.bloom_effect_r),
        )

        angles = math.atan2(
            self.stagy - self.bloom_effect_y, self.stagx - self.bloom_effect_x
        )
        self.move_bloom_x = math.cos(angles)
        self.move_bloom_y = math.sin(angles)

        self.bloom_effect_x -= self.move_bloom_x * random.randint(7, 9) / 10
        self.bloom_effect_y -= self.move_bloom_y * random.randint(7, 9) / 10

        self.color -= 0.2
        if self.color <= 30:
            self.color = 30

        if self.offset <= 200:
            self.bloom_effect_y += self.bloom_up_vel
            self.bloom_up_vel += 0.007

        if self.offset <= 0:
            self.bloom_effect_r -= self.shrink_rate

        self.offset -= 1


particles = [Particle(500, 500)]
bloom_particles = [Bloom_Particle(500, 500)]


def explode(duration):
    while duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        particles.append(Particle(500, 500))
        bloom_particles.append(Bloom_Particle(500, 500))

        for particle in particles:
            particle.draw(win)
            particle.movement()

            if particle.radius <= 0:
                particles.remove(particle)

        for bloom_particle in bloom_particles:
            bloom_particle.bloom()

            if bloom_particle.bloom_effect_y >= bloom_particle.stagy:
                bloom_particle.bloom_effect_r -= 2

            if bloom_particle.bloom_effect_r <= 0:
                bloom_particles.remove(bloom_particle)

        pygame.display.update()
        win.fill((0, 0, 0))
        clock.tick(60)


duration_timer = 1

if duration_timer == 1:
    duration = True
    duration_timer += 1

explode(duration)
