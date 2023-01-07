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
    global colvo_level
    right = False
    fon = pygame.transform.scale(load_image('custle_ras_wo.png'), (width, height))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    color = '#00CC00'
    color2 = 'white'
    level = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(150, 250) and event.pos[1] in range(400, 500):
                    button.play()
                    level = 0
                if event.pos[0] in range(550, 650) and event.pos[1] in range(400, 500):
                    button.play()
                    level = 1
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, pygame.Color('brown'), ((150, 400), (100, 100)))
        pygame.draw.polygon(screen, pygame.Color('white'), ((170, 420), (170, 480), (230, 450)))
        pygame.draw.rect(screen, pygame.Color('brown'), ((550, 400), (100, 100)))
        pygame.draw.polygon(screen, pygame.Color('white'), ((570, 420), (570, 480), (630, 450)))
        pygame.display.flip()

        clock.tick(5)

        if level == 0 and int(colvo_level) >= 0:
            right = create_level(first_level, backgrounds['forest'], background_forest)
            colvo_level = int(colvo_level) + 1
            if not right:
                return
        elif level == 1 and int(colvo_level) >= 1:
            right = create_level(second_lvl, backgrounds['cave'], background_cave)
            colvo_level = int(colvo_level) + 1
            if not right:
                return
        level = None


def create_level(lev, fons, music):
    music.play(-1)
    running = True
    open_menu = False
    check_etap = etap[0]
    try:
        player, level_x, level_y = generate_level(lev[etap[0]])
    except FileNotFoundError:
        print('Файл не найден')
        return
    draw_walls()
    fon = pygame.transform.scale(fons, (width, height))
    screen.blit(fon, (0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
                    open_menu = True

        for element in tiles_group:
            element.update()
        if etap[0] != check_etap:
            fon = pygame.transform.scale(fons, (width, height))
            screen.blit(fon, (0, 0))
            for el in all_sprites:
                all_sprites.remove(el)
            for el in tiles_group:
                tiles_group.remove(el)
                if el.type == 'door' and etap[0] > check_etap:
                    cord = (el.rect.x - 50, el.rect.y)
            for el in player_group:
                player_group.remove(el)
            player, level_x, level_y = generate_level(lev[etap[0]])
            if etap[0] < check_etap:
                player.rect.x, player.rect.y = cord[0], cord[1]
            check_etap = etap[0]

        if player.end:
            etap[0] = 0
            for el in all_sprites:
                all_sprites.remove(el)
            for el in tiles_group:
                tiles_group.remove(el)
            for el in player_group:
                player_group.remove(el)
            running = False
            open_menu = True

        screen.blit(fon, (0, 0))
        player.movement()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(fps)

    music.stop()
    etap[0] = 0
    for el in all_sprites:
        all_sprites.remove(el)
    for el in tiles_group:
        tiles_group.remove(el)
    for el in player_group:
        player_group.remove(el)
    if open_menu:
        return True
    return False


if __name__ == '__main__':
    no_close = start()
    if no_close:
        menu()
