import pygame.sprite

from player import *


def draw_walls():
    for y in range(len(map_world)):
        for x in range(len(map_world[y][0])):
            if map_world[y][0][x] == '#':
                pygame.draw.rect(screen, pygame.Color('white'), ((x * 50, y * 50), (x * 50 + 50, y * 50 + 50)),
                                 width=1)


def main():
    running = True
    try:
        player, level_x, level_y = generate_level(map_world)
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

        screen.blit(fon, (0, 0))
        player.movement()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()
