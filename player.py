# player settings
from settings import *
from map import *


def diing(self, sound):
    if sound:
        die.play()
    x, y = 0, 0
    self.rect.x, self.rect.y = self.star_pos[0], self.star_pos[1]
    for el in tiles_group:
        el.rect.x = el.star_pos[0]
        el.rect.y = el.star_pos[1]
        if el.type == 'ship':
            el.rect.y = el.star_pos[1] + 25
        if el.type == 'door' or el.type == 'obrat_door':
            el.rect.y = el.star_pos[1] + 9
        if el.type == 'green_slime':
            el.naprav = 'right'
            el.image = tile_images[el.type]
        if el.type == 'spike':
            if el.vertical:
                el.naprav = 'up'
            else:
                el.naprav = 'right'
            el.rect.x, el.rect.y = el.star_pos[0], el.star_pos[1]
    self.live = False
    return x, y


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y][0])):
            if level[y][0][x] == '#':
                Tile('grass', x, y)
            elif level[y][0][x] == 'B':
                Tile('box', x, y)
            elif level[y][0][x] == 'S':
                Tile('ship', x, y)
            elif level[y][0][x] == 'G':
                Tile('green_slime', x, y)
            elif level[y][0][x] == 'D':
                Tile('door', x, y)
            elif level[y][0][x] == 'O':
                Tile('obrat_door', x, y)
            elif level[y][0][x] == 'E':
                Tile('exit', x, y)
            elif level[y][0][x] == 'K':
                Tile('stone', x, y)
            elif level[y][0][x] == 'T':
                Tile('tree', x, y)
            elif level[y][0][x] == '1':
                Tile('glay', x, y)
            elif level[y][0][x] == 'L':
                Tile('listva', x, y)
            elif level[y][0][x] == 'Q':
                Tile('board', x, y)
            elif level[y][0][x] == '2':
                Tile('spike', x, y)
            elif level[y][0][x] == '3':
                Tile('spike', x, y, True)
            elif level[y][0][x] == '4':
                Tile('spike', x, y, False, 5)
            elif level[y][0][x] == '5':
                Tile('spike', x, y, True, 5)
            elif level[y][0][x] == '6':
                Tile('stone_ideal', x, y)
            elif level[y][0][x] == '7':
                Tile('stone_ne_ideal', x, y)
            elif level[y][0][x] == '8':
                Tile('diamond', x, y)
            elif level[y][0][x] == '9':
                Tile('iron', x, y)
            elif level[y][0][x] == '!':
                Tile('coal', x, y)
            elif level[y][0][x] == '$':
                Tile('sand', x, y)
            elif level[y][0][x] == '%':
                Tile('kaktus', x, y)
            elif level[y][0][x] == '^':
                Tile('peschan', x, y)
            elif level[y][0][x] == '@':
                new_player = Player(x * 50, y * 50 - 20, all_sprites)
    return new_player, x, y


class Lock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(locks_group)
        self.image = tile_images['lock']
        self.rect = self.image.get_rect()
        self.star_pos = (x, y)
        self.rect.x = x
        self.rect.y = y
        self.naprav = True
        self.counter = 9

    def update(self):
        if self.counter < 9:
            if self.naprav:
                self.rect.x += 2
                self.naprav = False
            else:
                self.rect.x -= 2
                self.naprav = True
            self.counter += 1

    def settimes(self):
        self.counter = 0


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, vertically=False, speed=1):
        super().__init__(tiles_group, all_sprites)
        self.star_pos = (tile_width * pos_x, tile_height * pos_y)
        self.image = tile_images[tile_type]
        self.kill = False
        self.type = tile_type
        self.speed = speed
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        if tile_type == 'ship':
            self.rect.y += 25
            self.kill = True
        if tile_type == 'green_slime':
            self.kill = True
            self.naprav = 'right'
        if tile_type == 'door' or tile_type == 'obrat_door':
            self.rect.y += 9
        if tile_type == 'spike':
            self.vertical = vertically
            self.kill = True
            if vertically:
                self.naprav = 'up'
            else:
                self.naprav = 'right'
        if tile_type == 'kaktus':
            self.kill = True

    def update(self):
        # Движение зелёного слайма
        if self.type == 'green_slime':
            if self.naprav == 'left':
                self.rect.x -= 1
                if self.rect.x + 50 < self.star_pos[0]:
                    self.image = tile_images[self.type]
                    self.naprav = 'right'
            else:
                self.rect.x += 1
                if self.rect.x - 50 > self.star_pos[0]:
                    self.naprav = 'left'
                    self.image = pygame.transform.flip(tile_images[self.type], True, False)

        # движение колючек
        if self.type == 'spike':
            if self.vertical:
                if self.naprav == 'up':
                    self.rect.y -= self.speed
                    right = 0
                    if self.speed >= 5:
                        self.image = pygame.transform.rotate(self.image, 90)
                    for element in tiles_group:
                        if element.rect.colliderect(self.rect.x, self.rect.y - self.speed, 50, 50):
                            right += 1
                    if self.rect.y + 150 <= self.star_pos[1] or right >= 2 or self.rect.y - self.speed == 0:
                        self.naprav = 'down'
                else:
                    self.rect.y += self.speed
                    right = 0
                    if self.speed >= 5:
                        self.image = pygame.transform.rotate(self.image, 90)
                    for element in tiles_group:
                        if element.rect.colliderect(self.rect.x, self.rect.y + self.speed, 50, 50):
                            right += 1
                    if self.rect.y - 150 >= self.star_pos[1] or right >= 2 or self.rect.y + self.speed == 900:
                        self.naprav = 'up'
            else:
                if self.naprav == 'left':
                    self.rect.x -= self.speed
                    if self.speed >= 5:
                        self.image = pygame.transform.rotate(self.image, 90)
                    right = False
                    for element in tiles_group:
                        if element.rect.colliderect(self.rect.x - self.speed, self.rect.y, 50, 50):
                            right += 1
                    if self.rect.x + 150 <= self.star_pos[0] or right >= 2 or self.rect.x - self.speed == 0:
                        self.naprav = 'right'
                else:
                    self.rect.x += self.speed
                    if self.speed >= 5:
                        self.image = pygame.transform.rotate(self.image, 90)
                    right = False
                    for element in tiles_group:
                        if element.rect.colliderect(self.rect.x + self.speed, self.rect.y, 50, 50):
                            right += 1
                    if self.rect.x - 150 >= self.star_pos[0] or right >= 2 or self.rect.y + 50 + self.speed == 1200:
                        self.naprav = 'left'


class Player(pygame.sprite.Sprite):
    image_stand = load_image('player_stand1.png')
    image_run_r1 = load_image('run_r1_1.png')
    image_run_r2 = load_image('run_r2_2.png')
    image_run_r3 = load_image('run_r3_3.png')
    image_run_r4 = load_image('run_r4_4.png')
    image_run_r5 = load_image('run_r5_5.png')
    image_run_r6 = load_image('run_r6_6.png')

    image_jump = load_image('jump.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Player.image_stand
        self.star_pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.run_right = [Player.image_run_r1, Player.image_run_r2, Player.image_run_r3, Player.image_run_r4,
                          Player.image_run_r5, Player.image_run_r6]
        self.jump = False
        self.stoit = True
        self.count = 21
        self.naprav = None
        self.speed = 1
        self.poden = 0
        self.dwiz = -1
        self.moving = False
        self.jumping = 0
        self.counter = 0
        self.end = False
        self.live = True

    def movement(self):
        keys = pygame.key.get_pressed()
        sdwig = False
        self.moving = False
        pribav = True
        x = 0
        y = 0

        # За что отвечают клавиши
        if keys[pygame.K_SPACE] and self.jumping < 2 and not self.jump:
            jump_sound.stop()
            jump_sound.play()
            self.jump = True
            sdwig = True
            self.stoit = False
            self.jumping += 1
            self.poden = -15
        if not keys[pygame.K_SPACE]:
            sdwig = True
            self.jump = False
        if keys[pygame.K_d] and self.rect.x + 50 <= width:
            x += 5
            self.dwiz += 1
            self.naprav = 'right'
            sdwig = True
            self.moving = True
        if keys[pygame.K_a] and self.rect.x >= 0:
            x -= 5
            self.dwiz += 1
            self.naprav = 'left'
            sdwig = True
            self.moving = True
        if not keys[pygame.K_a] and not keys[pygame.K_d] and self.live:
            self.dwiz = -1
        if not keys[pygame.K_r]:
            self.live = True

        # отвечает за падение
        self.poden += 1
        if self.poden > 10:
            self.poden = 10
        self.rect.y += self.poden
        if self.rect.y <= 0:
            self.rect.y = 0
            self.poden = 0

        if self.rect.bottom > height - 50:
            self.rect.bottom = height - 50

        # анимация ходьбы
        if self.dwiz >= 0:
            if self.dwiz >= 60 or not sdwig:
                self.dwiz = -1
            a = self.dwiz // 10
            if self.naprav == 'right':
                self.image = self.run_right[a]
            else:
                self.image = pygame.transform.flip(self.run_right[a], True, False)
        else:
            self.image = Player.image_stand

        # анимация прыжка
        if self.poden < 0:
            if self.naprav == 'left':
                self.image = pygame.transform.flip(Player.image_jump, True, False)
            else:
                self.image = Player.image_jump

        # проверка пересечений
        for element in tiles_group:
            if element.rect.colliderect(self.rect.x + x, self.rect.y - 1, lang_x, lang_y):
                x = 0
                if element.type == 'door':
                    etap[0] = etap[0] + 1
                    pribav = False
                if element.type == 'obrat_door':
                    etap[0] = etap[0] - 1
                    pribav = False
                if element.type == 'exit':
                    self.end = True
                if element.kill:
                    x, y = diing(self, True)

            if element.rect.colliderect(self.rect.x + 1, self.rect.y + y, lang_x, lang_y):
                if self.poden < 0:
                    y = element.rect.bottom - self.rect.top
                    self.poden = 0
                elif self.poden >= 0:
                    y = element.rect.top - self.rect.bottom
                    self.poden = 0
                if element.type == 'door' and pribav:
                    etap[0] = etap[0] + 1
                if element.type == 'obrat_door' and pribav:
                    etap[0] = etap[0] - 1
                if element.type == 'exit':
                    self.end = True
                # Если персонаж умирает все спрайты обновляются до первого состояния
                if element.kill:
                    x, y = diing(self, True)

            # делает максимум 2 прыжка от земли
            if element.rect.colliderect(self.rect.x, self.rect.bottom - 5, lang_x, 6):
                self.stoit = True

        if self.stoit:
            self.counter += 1

        self.rect.x += x
        self.rect.y += y
        if self.stoit:
            self.jumping = 0
        if self.counter == 30:
            self.counter = 0
