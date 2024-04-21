import random
import time

import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bubble Draw v1.0")
clock = pygame.time.Clock()

PINK = (255, 194, 245)
BLACK = (0, 0, 0)
MAGENTA = (252, 45, 156)
DARK_MAGENTA = (173, 33, 108)
WHITE = (255, 255, 255)
LIGHT_BLUE = (150, 215, 255)
BLUE = (59, 111, 143)


def print_to_display(text, font_name, font_size, color, x, y, width, height):
    text_parameters = pygame.font.Font(font_name, font_size)
    text_surface = text_parameters.render(text, True, color)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = ((x + width / 2), (y + height / 2))
    win.blit(text_surface, text_rectangle)


class Bubble(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 17
        self.color = LIGHT_BLUE
        self.life = 500

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, 3)

    def move(self):
        self.move_x = random.randint(-1, 2)
        self.move_y = random.randint(-1, 2)
        self.x += self.move_x
        self.y += self.move_y


class Button(object):
    def __init__(
        self,
        label,
        label_size,
        label_color,
        button_x,
        button_y,
        button_width,
        button_height,
        inactive_color,
        active_color,
    ):
        self.label = label
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.label_size = label_size
        self.label_color = label_color

    def create(self, win):
        self.mouse_click = pygame.mouse.get_pressed()
        self.mouse_position = pygame.mouse.get_pos()

        if (self.button_x + self.button_width) > self.mouse_position[0] > (
            self.button_x
        ) and (self.button_y + self.button_height) > self.mouse_position[1] > (
            self.button_y
        ):
            pygame.draw.rect(
                win,
                self.active_color,
                (
                    self.button_x,
                    self.button_y,
                    self.button_width,
                    self.button_height,
                ),
            )
        else:
            pygame.draw.rect(
                win,
                self.inactive_color,
                (
                    self.button_x,
                    self.button_y,
                    self.button_width,
                    self.button_height,
                ),
            )

        print_to_display(
            self.label,
            "freesansbold.ttf",
            self.label_size,
            self.label_color,
            self.button_x,
            self.button_y,
            self.button_width,
            self.button_height,
        )

    def is_clicked(self):
        if (
            self.button_x + self.button_width
            > self.mouse_position[0]
            > self.button_x
            and self.button_y + self.button_height
            > self.mouse_position[1]
            > self.button_y
            and mouse_click[0] == 1
        ):
            return True
        else:
            return False


bubbles = []
POPbutton = Button("POP", 20, WHITE, 693, 10, 100, 50, MAGENTA, DARK_MAGENTA)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick(60)
    win.fill(BLUE)

    # Everything must be drawn after this point
    POPbutton.create(win)
    if POPbutton.is_clicked() == True:
        bubbles = []
        print_to_display(
            "POP!", "freesansbold.ttf", 115, MAGENTA, 200, 150, 400, 300
        )
        pygame.display.update()
        time.sleep(1)

    # Buttons should be created before this point
    for bubble in bubbles:
        bubble.draw(win)
        bubble.move()
        bubble.life -= 1

    mouse_click = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()

    if mouse_click[0] == 1 and not POPbutton.is_clicked() == True:
        bubbles.append(Bubble(mouse_position[0], mouse_position[1]))

    for index, bubble in enumerate(bubbles):
        if bubble.life == 0:
            bubbles.pop(index)

    pygame.display.update()
