# player settings
from settings import *
from map import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


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
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.run_right = [Player.image_run_r1, Player.image_run_r2, Player.image_run_r3, Player.image_run_r4,
                          Player.image_run_r5, Player.image_run_r6]
        self.jump = False
        self.count = 21
        self.naprav = None
        self.speed = 1
        self.poden = 0
        self.dwiz = -1

    def movement(self):
        keys = pygame.key.get_pressed()
        sdwig = False
        x = 0
        y = 0

        # За что отвечают клавиши
        if keys[pygame.K_SPACE] and not self.jump:
            self.jump = True
            sdwig = True
            self.poden = -15
        if not keys[pygame.K_SPACE]:
            sdwig = True
            self.jump = False
        if keys[pygame.K_d] and self.rect.x + 50 <= width:
            x += 5
            self.dwiz += 1
            self.naprav = 'right'
            sdwig = True
        if keys[pygame.K_s] and self.rect.y + 5 >= height - lang_y:
            y += 5
        if keys[pygame.K_a] and self.rect.x >= 0:
            x -= 5
            self.dwiz += 1
            self.naprav = 'left'
            sdwig = True
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.dwiz = -1

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
        if self.poden < 10:
            if self.naprav == 'left':
                self.image = pygame.transform.flip(Player.image_jump, True, False)
            else:
                self.image = Player.image_jump

        for element in tiles_group:
            if element.rect.colliderect(self.rect.x, self.rect.y, lang_x, lang_y):
                if self.poden < 0:
                    y = element.rect.bottom - self.rect.top
                elif self.poden >= 0:
                    y = element.rect.top - self.rect.bottom

        self.rect.x += x
        self.rect.y += y