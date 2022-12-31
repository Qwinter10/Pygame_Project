from player import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


def draw_walls():
    for y in range(len(map_world)):
        for x in range(len(map_world[y][0])):
            if map_world[y][0][x] == '#':
                pygame.draw.rect(screen, pygame.Color('white'), ((x * 50, y * 50), (x * 50 + 50, y * 50 + 50)),
                                 width=1)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y][0])):
            if level[y][0][x] == '#':
                Tile('wall', x, y)
            elif level[y][0][x] == '@':
                new_player = Player(x * 50, y * 50 - 20, all_sprites)
    return new_player, x, y


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
