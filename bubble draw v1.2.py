import random
import time

import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bubble Draw v1.2")
clock = pygame.time.Clock()

PINK = (255, 194, 245)
BLACK = (0, 0, 0)
MAGENTA = (252, 45, 156)
DARK_MAGENTA = (173, 33, 108)
WHITE = (255, 255, 255)
LIGHT_BLUE = (150, 215, 255)
BLUE = (59, 111, 143)
BRIGHT_YELLOW = (246, 255, 0)
DARK_YELLOW = (178, 181, 81)
DARK_CYAN = (50, 166, 168)
CYAN = (117, 223, 224)

radius = 17
thickness = 3
physics_minimum = -1
physics_maximum = 1
bubble_life = 500
bubble_physics = "Stagnant"


def print_to_display(
    display,
    text,
    font_name,
    font_size,
    color,
    posx,
    posy,
    center_around_point,
    set_custom_dimensions,
    custom_dimension_width,
    custom_dimension_height,
):
    text_parameters = pygame.font.Font(font_name, font_size)
    rendered_text = text_parameters.render(text, True, color)
    text_dimensions = rendered_text.get_rect()
    if center_around_point == True and set_custom_dimensions == False:
        text_dimensions.center = ((posx), (posy))
        display.blit(rendered_text, text_dimensions)
    elif center_around_point == False and set_custom_dimensions == False:
        text_dimensions.center = (
            (posx + text_dimensions[2] / 2),
            (posy + text_dimensions[3] / 2),
        )
        display.blit(rendered_text, text_dimensions)
    elif center_around_point == False and set_custom_dimensions == True:
        text_dimensions.center = (
            (posx + custom_dimension_width / 2),
            (posy + custom_dimension_height / 2),
        )
        display.blit(rendered_text, text_dimensions)
    else:
        print(
            "error, can not set custom text dimensions when center around point is True"
        )


class Bubble(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = LIGHT_BLUE
        self.life = bubble_life
        self.thickness = thickness
        self.physics_minimum = physics_minimum
        self.physics_maximum = physics_maximum

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, (self.x, self.y), self.radius, self.thickness
        )

    def move(self):
        self.move_x = random.randint(physics_minimum, physics_maximum)
        self.move_y = random.randint(physics_minimum, physics_maximum)
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

        pygame.draw.rect(
            win,
            BLACK,
            (
                self.button_x - 2,
                self.button_y - 2,
                self.button_width + 4,
                self.button_height + 4,
            ),
            3,
        )
        # print_to_display(display, text, font_name, font_size, color, posx, posy, center_around_point, set_custom_dimensions, custom_dimension_width, custom_dim_height)
        print_to_display(
            win,
            self.label,
            "freesansbold.ttf",
            self.label_size,
            self.label_color,
            self.button_x,
            self.button_y,
            False,
            True,
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
            and self.mouse_click[0] == 1
        ):
            return True


# main loop and required variables:

main_game = True

bubbles = []

POPbutton = Button("POP", 20, WHITE, 693, 10, 100, 50, MAGENTA, DARK_MAGENTA)

radius_plus = Button("+", 30, WHITE, 693, 110, 100, 50, MAGENTA, DARK_MAGENTA)
radius_minus = Button("-", 30, WHITE, 693, 170, 100, 50, MAGENTA, DARK_MAGENTA)
radius_reset = Button(
    "Reset", 20, WHITE, 693, 230, 100, 50, MAGENTA, DARK_MAGENTA
)

thickness_plus = Button(
    "+", 30, WHITE, 693, 320, 100, 50, MAGENTA, DARK_MAGENTA
)
thickness_minus = Button(
    "-", 30, WHITE, 693, 380, 100, 50, MAGENTA, DARK_MAGENTA
)
thickness_reset = Button(
    "Reset", 20, WHITE, 693, 440, 100, 50, MAGENTA, DARK_MAGENTA
)

bubble_physics_fall = Button(
    "Fall", 20, WHITE, 122, 537, 100, 50, CYAN, DARK_CYAN
)
bubble_physics_rise = Button(
    "Rise", 20, WHITE, 322, 537, 100, 50, CYAN, DARK_CYAN
)
bubble_physics_stay = Button(
    "Stagnant", 20, WHITE, 522, 537, 100, 50, CYAN, DARK_CYAN
)

life_button_plus = Button(
    "+", 30, WHITE, 20, 160, 100, 50, MAGENTA, DARK_MAGENTA
)
life_button_minus = Button(
    "-", 30, WHITE, 20, 240, 100, 50, MAGENTA, DARK_MAGENTA
)
life_button_reset = Button(
    "Reset", 20, WHITE, 20, 320, 100, 50, MAGENTA, DARK_MAGENTA
)

exit_button = Button(
    "EXIT", 30, BLUE, 693, 530, 100, 50, BRIGHT_YELLOW, DARK_YELLOW
)

while main_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick(60)
    win.fill(BLUE)

    # everything must be drawn after this point

    print_to_display(
        win,
        "If thickness is equal to 0, then the bubbles will be solid",
        "freesansbold.ttf",
        20,
        PINK,
        350,
        30,
        True,
        False,
        0,
        0,
    )
    print_to_display(
        win,
        "Radius : " + str(radius),
        "freesansbold.ttf",
        15,
        LIGHT_BLUE,
        693,
        60,
        False,
        True,
        100,
        50,
    )
    print_to_display(
        win,
        "Thickness : " + str(thickness),
        "freesansbold.ttf",
        15,
        LIGHT_BLUE,
        693,
        275,
        False,
        True,
        100,
        50,
    )
    print_to_display(
        win,
        "Bubble Life : " + str(bubble_life),
        "freesansbold.ttf",
        15,
        LIGHT_BLUE,
        20,
        100,
        False,
        True,
        100,
        50,
    )
    print_to_display(
        win,
        "Bubble Physics : " + bubble_physics,
        "freesansbold.ttf",
        15,
        LIGHT_BLUE,
        387,
        507,
        True,
        False,
        0,
        0,
    )

    POPbutton.create(win)
    if POPbutton.is_clicked() == True:
        bubbles = []
        # print_to_display(display, text, font_name, font_size, color, posx, posy, center_around_point, set_custom_dimensions, custom_dimension_width, custom_dim_height)
        print_to_display(
            win,
            "POP!",
            "freesansbold.ttf",
            115,
            MAGENTA,
            400,
            300,
            True,
            False,
            0,
            0,
        )
        pygame.display.update()
        time.sleep(0.5)

    radius_plus.create(win)
    if radius_plus.is_clicked() == True:
        radius += 1
        time.sleep(0.1)

    radius_minus.create(win)
    if radius_minus.is_clicked() == True:
        radius -= 1
        time.sleep(0.1)
        if radius <= 4:
            radius = 4

    radius_reset.create(win)
    if radius_reset.is_clicked() == True:
        radius = 17

    thickness_plus.create(win)
    if thickness_plus.is_clicked() == True:
        thickness += 1
        time.sleep(0.1)
        if thickness >= radius:
            thickness = radius - 1

    thickness_minus.create(win)
    if thickness_minus.is_clicked() == True:
        thickness -= 1
        time.sleep(0.1)
        if thickness <= 0:
            thickness = 0

    thickness_reset.create(win)
    if thickness_reset.is_clicked() == True:
        thickness = 3

    bubble_physics_fall.create(win)
    if bubble_physics_fall.is_clicked() == True:
        bubble_physics = "Fall"
        physics_minimum = -1
        physics_maximum = 2

    bubble_physics_rise.create(win)
    if bubble_physics_rise.is_clicked() == True:
        bubble_physics = "Rise"
        physics_minimum = -2
        physics_maximum = 1

    bubble_physics_stay.create(win)
    if bubble_physics_stay.is_clicked() == True:
        bubble_physics = "Stagnant"
        physics_minimum = -1
        physics_maximum = 1

    life_button_plus.create(win)
    if life_button_plus.is_clicked() == True:
        bubble_life += 100
        time.sleep(0.1)

    life_button_minus.create(win)
    if life_button_minus.is_clicked() == True:
        bubble_life -= 100
        time.sleep(0.1)

    life_button_reset.create(win)
    if life_button_reset.is_clicked() == True:
        bubble_life = 500
        time.sleep(0.1)

    exit_button.create(win)
    if exit_button.is_clicked() == True:
        # print_to_display(display, text, font_name, font_size, color, posx, posy, center_around_point, set_custom_dimensions, custom_dimension_width, custom_dim_height)
        print_to_display(
            win,
            "Bye ;(",
            "freesansbold.ttf",
            115,
            BRIGHT_YELLOW,
            400,
            300,
            True,
            False,
            0,
            0,
        )
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()

    # buttons should be created before this point

    for bubble in bubbles:
        bubble.draw(win)
        bubble.move()
        if bubble.x >= 670:
            bubble.x = 670
        if bubble.y <= 60:
            bubble.y = 60
        if bubble.x <= 150:
            bubble.x = 150
        if bubble.y >= 477:
            bubble.y = 477
        bubble.life -= 1

    mouse_click = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()

    if (
        mouse_click[0] == 1
        and not POPbutton.is_clicked()
        and not radius_plus.is_clicked()
        and not radius_minus.is_clicked()
        and not radius_reset.is_clicked()
        and not thickness_plus.is_clicked()
        and not thickness_minus.is_clicked()
        and not thickness_reset.is_clicked()
        and not exit_button.is_clicked()
        and not bubble_physics_rise.is_clicked()
        and not bubble_physics_fall.is_clicked()
        and not bubble_physics_stay.is_clicked()
        and not life_button_plus.is_clicked()
        and not life_button_minus.is_clicked()
        and not life_button_reset.is_clicked()
    ):
        bubbles.append(Bubble(mouse_position[0], mouse_position[1]))

    for index, bubble in enumerate(bubbles):
        if bubble.life == 0:
            bubbles.pop(index)

    pygame.display.update()
