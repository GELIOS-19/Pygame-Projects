import pygame

pygame.init()
clock = pygame.time.Clock(60)

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game")
win_width = 1280
win_height = 720

main_game = False
main_menu = True
pause_menu = False


class Player(object):

    def __init__(self, player_x, player_y, player_direction, player_velocity):
        self.player_x = player_x
        self.player_y = player_y
        self.player_direction = player_direction
        self.player_velocity = player_velocity
        self.player_width = 64
        self.player_height = 64
