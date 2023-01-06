# game settings
import pygame
import os
import sys

width = 1200
height = 900
fps = 60
tile_width = tile_height = 50


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

lang_x = 34
lang_y = 50

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


tile_images = {
    'box': load_image('box.png'),
    'grass': load_image('trava.png'),
    'empty': load_image('grass.png'),
    'ship': load_image('ship2.png'),
    'green_slime': load_image('green_slime.png'),
    'door': load_image('door.png')
}

button = pygame.mixer.Sound('music/push_button.mp3')
button.set_volume(0.3)

die = pygame.mixer.Sound('music/die.mp3')
die.set_volume(0.1)

