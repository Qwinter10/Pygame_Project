import pygame.sprite
from player import *


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
    if int(colvo_level) < 1:
        locker1 = Lock(570, 420)
    if int(colvo_level) < 2:
        locker2 = Lock(970, 420)
    fon = pygame.transform.scale(load_image('custle_ras_wo.png'), (width, height))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    color = 'white'
    color2 = 'white'
    color3 = 'white'
    level = None
    running = True

    font = pygame.font.Font(None, 100)
    text = font.render('?', True, ('white'))

    while running:
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(150, 250) and event.pos[1] in range(400, 500):
                    level = 0
                    color = '#BFBFBF'
                if event.pos[0] in range(550, 650) and event.pos[1] in range(400, 500):
                    if int(colvo_level) >= 1:
                        level = 1
                        color2 = '#BFBFBF'
                    else:
                        zamok.stop()
                        zamok.play()
                        locker1.settimes()
                if event.pos[0] in range(950, 1050) and event.pos[1] in range(400, 500):
                    if int(colvo_level) >= 2:
                        level = 2
                        color3 = '#BFBFBF'
                    else:
                        zamok.stop()
                        zamok.play()
                        locker2.settimes()
                if event.pos[0] in range(1100, 1180) and event.pos[1] in range(800, 880):
                    level = 4

        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, pygame.Color('brown'), ((150, 400), (100, 100)))
        pygame.draw.polygon(screen, pygame.Color(color), ((170, 420), (170, 480), (230, 450)))
        pygame.draw.rect(screen, pygame.Color('brown'), ((550, 400), (100, 100)))
        pygame.draw.polygon(screen, pygame.Color(color2), ((570, 420), (570, 480), (630, 450)))
        pygame.draw.rect(screen, pygame.Color('brown'), ((950, 400), (100, 100)))
        pygame.draw.polygon(screen, pygame.Color(color3), ((970, 420), (970, 480), (1030, 450)))
        pygame.draw.rect(screen, pygame.Color('brown'), ((1100, 800), (80, 80)))
        screen.blit(text, (1120, 810))

        for el in locks_group:
            locks_group.remove(el)
            el.update()

        if level == 0 and int(colvo_level) >= 0:
            for el in locks_group:
                locks_group.remove(el)
            button.play()
            right, esc = create_level(first_level, backgrounds['forest'], background_forest)
            if int(colvo_level) == 0 and not esc:
                colvo_level = str(int(colvo_level) + 1)
                locks_group.remove(locker1)
            color = 'white'
            if not right:
                return
        elif level == 1 and int(colvo_level) >= 1:
            button.play()
            right, esc = create_level(second_lvl, backgrounds['cave'], background_cave)
            if int(colvo_level) == 1 and not esc:
                colvo_level = str(int(colvo_level) + 1)
                locks_group.remove(locker2)
            color2 = 'white'
            if not right:
                return
        elif level == 2 and int(colvo_level) >= 2:
            button.play()
            right, esc = create_level(third_lvl, backgrounds['desert'], background_desert)
            if int(colvo_level) == 2 and not esc:
                colvo_level = str(int(colvo_level) + 1)
            color3 = 'white'
            if not right:
                return
        elif level == 4:
            button.play()
            right = rules()
            if not right:
                return

        level = None
        file = open('level.txt', mode='wt', encoding='utf8')
        file.write(colvo_level)
        file.close()

        if int(colvo_level) < 1:
            locker1 = Lock(570, 420)
        if int(colvo_level) < 2:
            locker2 = Lock(970, 420)

        locks_group.draw(screen)
        pygame.display.flip()
        locks_group.draw(screen)
        clock.tick(30)


def rules():
    running = True
    right = False
    fon = pygame.transform.scale(load_image('rules.png'), (width, height))
    screen.blit(fon, (0, 0))
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
                    right = True

    return right


def create_level(lev, fons, music):
    pygame.mouse.set_visible(False)
    music.play(-1)
    running = True
    esc = False
    open_menu = False
    check_etap = etap[0]
    try:
        player, level_x, level_y = generate_level(lev[etap[0]])
    except FileNotFoundError:
        print('Файл не найден')
        return
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
                    esc = True
                elif event.key == 114:
                    diing(player, True)

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
        return True, esc
    return False, esc


if __name__ == '__main__':
    no_close = start()
    if no_close:
        menu()
