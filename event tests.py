import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)


##def text_objects(text, font):
##    textSurface = font.render(text, True, BLACK)
##    return textSurface, textSurface.get_rect()
##
##def message_display(text):
##    largeText = pygame.font.Font('Menlo.ttf', 115)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = ((800/2), (600/2))
##    win.blit(TextSurf, TextRect)


##def print_to_display(text, font_name, font_size, color, x, y, width, height):
##    text_parameters = pygame.font.Font(font_name, font_size)
##    text_surface = text_parameters.render(text, True, color)
##    text_rectangle = text_surface.get_rect()
##    pygame.draw.rect(win, WHITE, (x, y, text_rectangle[2], text_rectangle[3]), 1)
##    if width == 1 and height == 1:
##        text_rectangle.center = ((x + text_rectangle[2]/2), (y + text_rectangle[3]/2))
##    else:
##        text_rectangle.center = ((x + width/2), (y + height/2))
##    win.blit(text_surface, text_rectangle)
##
##
##
##
##print_to_display('hello, nice to meet you', 'freesansbold.ttf', 22, WHITE, 255, 254, 0, 0)
##pygame.draw.circle(win, WHITE, (255, 254), 10, 1)
##pygame.display.update()


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
    custom_dim_height,
):
    text_parameters = pygame.font.Font(font_name, font_size)
    rendered_text = text_parameters.render(text, True, color)
    text_dimensions = rendered_text.get_rect()
    if center_around_point == True:
        text_dimensions.center = ((posx), (posy))
    elif center_around_point == False:
        text_dimensions.center = (
            (posx + text_dimensions[2] / 2),
            (posy + text_dimensions[3] / 2),
        )
    elif center_around_point == False and set_custom_dimensions == True:
        text_dimensions.center = (
            (posx + custom_dimension_width / 2),
            (posy + custom_dimension_height / 2),
        )
    display.blit(rendered_text, text_dimensions)
    pygame.display.update()


print_to_display(
    win, "hi", "freesansbold.ttf", 115, WHITE, 400, 300, True, False, 0, 0
)
