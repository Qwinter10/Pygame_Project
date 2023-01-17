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
locks_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


with open('level.txt', mode='rt', encoding='utf8') as f:
    colvo_level = f.readline()
    f.close()


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


fon = pygame.transform.scale(load_image('custle_ras_r.png'), (width, height))
screen.blit(fon, (0, 0))
pygame.draw.polygon(screen, pygame.Color('#00CC00'), ((450, 400), (750, 400), (750, 500), (450, 500)))
pygame.draw.polygon(screen, pygame.Color('white'), ((560, 410), (560, 490), (640, 445)))
pygame.display.flip()

tile_images = {
    'box': load_image('box.png'),
    'grass': load_image('grass_new.png'),
    'empty': load_image('grass.png'),
    'ship': load_image('ship2.png'),
    'green_slime': load_image('green_slime.png'),
    'door': load_image('door.png'),
    'obrat_door': load_image('door.png'),
    'stone':  load_image('stone.png'),
    'exit': load_image('exit_door.png'),
    'lock': load_image('lock.png'),
    'tree': load_image('tree.png'),
    'glay': load_image('glay.png'),
    'listva': load_image('listva.png'),
    'board': load_image('board.png'),
    'spike': load_image('spayk_ship.png'),
    'stone_ideal': load_image('stone_ideal.png'),
    'stone_ne_ideal': load_image('stone_ne_ideal.png'),
    'diamond': load_image('diamond.png'),
    'iron': load_image('iron.png'),
    'coal': load_image('coal.png'),
    'sand': load_image('sand.png'),
    'kaktus': load_image('kaktus.png'),
    'peschan': load_image('peschan.png')
}

backgrounds = {
    'forest': load_image('fon.png'),
    'cave': load_image('cave_background.png'),
    'desert': load_image('desert.png')
}

button = pygame.mixer.Sound('music/push_button.mp3')
button.set_volume(0.3)

die = pygame.mixer.Sound('music/die.mp3')
die.set_volume(0.1)

background_forest = pygame.mixer.Sound('music/forest.wav')
background_forest.set_volume(0.1)

background_cave = pygame.mixer.Sound('music/cave.wav')
background_cave.set_volume(0.3)

background_desert = pygame.mixer.Sound('music/Arabic_music.wav')
background_desert.set_volume(0.05)

zamok = pygame.mixer.Sound('music/zamok.mp3')
zamok.set_volume(0.2)

jump_sound = pygame.mixer.Sound('music/jump.mp3')
jump_sound.set_volume(0.1)
