import pygame.sprite

from player import *


def draw_walls():
    for y in range(len(map_world_lvl1)):
        for x in range(len(map_world_lvl1[y][0])):
            if map_world_lvl1[y][0][x] == '#':
                pygame.draw.rect(screen, pygame.Color('white'), ((x * 50, y * 50), (x * 50 + 50, y * 50 + 50)),
                                 width=1)


def start():
    right = True
    fon = pygame.transform.scale(load_image('custle_ras_r.png'), (width, height))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    color = '#00CC00'
    color2 = 'white'
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                right = False
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(450, 750) and event.pos[1] in range(400, 500):
                    button.play()
                    color = '#008500'
                    color2 = '#BFBFBF'
                    running = False
        pygame.draw.polygon(screen, pygame.Color(color), ((450, 400), (750, 400), (750, 500), (450, 500)))
        pygame.draw.polygon(screen, pygame.Color(color2), ((560, 410), (560, 490), (640, 445)))
        pygame.display.flip()
        clock.tick(5)

    return right


def menu():
    pass


def level_one():
    running = True
    check_etap = etap[0]
    try:
        player, level_x, level_y = generate_level(first_level[etap[0]])
    except FileNotFoundError:
        print('Файл не найден')
        return
    draw_walls()
    fon = pygame.transform.scale(load_image('fon.png'), (width, height))
    screen.blit(fon, (0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for element in tiles_group:
            element.update()
        if etap[0] != check_etap:
            fon = pygame.transform.scale(load_image('fon.png'), (width, height))
            screen.blit(fon, (0, 0))
            for el in all_sprites:
                all_sprites.remove(el)
            for el in tiles_group:
                tiles_group.remove(el)
            for el in player_group:
                player_group.remove(el)
            player, level_x, level_y = generate_level(first_level[etap[0]])
            check_etap = etap[0]

        screen.blit(fon, (0, 0))
        player.movement()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    no_close = start()
    if no_close:
        level_one()
