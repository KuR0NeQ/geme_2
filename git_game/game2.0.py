import pygame
class Character(object):
    speed = 16
    current_animation_left = 0
    current_animation_right = 0
    current_animation_down = 0
    current_animation_up = 0
    current_animation_default = 0
    current_animation_type = 'left'

    def __init__(self, animations_left: list, animations_right: list, animations_down: list, animations_up: list,
                 animations_default: list,
                 pos_x: int, pos_y: int):
        self.animations_default = animations_default
        self.animations_left = animations_left
        self.animations_up = animations_up
        self.animations_right = animations_right
        self.animations_down = animations_down

        self.animations_default_count = len(animations_default)
        self.animations_left_count = len(animations_left)
        self.animations_up_count = len(animations_up)
        self.animations_right_count = len(animations_right)
        self.animations_down_count = len(animations_down)

        self.pos_x = pos_x
        self.pos_y = pos_y

    def animation_set_type(self, animation_type: str):
        self.current_animation_type = animation_type

    def animation_change_animation_number(self):
        match self.current_animation_type:
            case 'left':
                self.current_animation_left = (self.current_animation_left + 1) % self.animations_left_count
            case 'right':
                self.current_animation_right = (self.current_animation_right + 1) % self.animations_right_count
            case 'down':
                self.current_animation_down = (self.current_animation_down + 1) % self.animations_down_count
            case 'up':
                self.current_animation_up = (self.current_animation_up + 1) % self.animations_up_count
            case 'deafult':
                self.current_animation_default = (self.current_animation_default + 1) % self.animations_default_count



clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1920, 1080))  # создание экрана
pygame.display.set_caption("лютый марио")  # название игры в окошке
# icon = pygame.image.load("icongame.png") #подгрузка иконки
# pygame.display.set_icon(icon) #установка иконки
game_map = pygame.image.load("linkleft/mup.png")
link_left = [
    pygame.image.load("linkleft/game_now_1.png"),  # подгрузка всех картинок
    pygame.image.load("linkleft/game_now_2.png"),
    pygame.image.load("linkleft/game_now_3.png"),
    pygame.image.load("linkleft/game_now_4.png"),
]
default = [
    pygame.image.load("linkleft/game_now_1.png")
]
link_right = [
    pygame.image.load("linkright/Sprite-0001.png"),  # подгрузка всех картинок
    pygame.image.load("linkright/Sprite-0002.png"),
    pygame.image.load("linkright/Sprite-0003.png"),
    pygame.image.load("linkright/Sprite-0004.png"),
]

main_character = Character(link_left, link_right, [], [], default, 300, 300)
main_character.speed = 32

gameplay = True

running = True
while running:
    if gameplay:

        screen.blit(game_map, (0, 50))
        keys = pygame.key.get_pressed()  # добавление клавиши ходьбы

        if keys[pygame.K_a] and main_character.pos_x > 200:
            main_character.pos_x -= main_character.speed
            main_character.animation_set_type('left')
        elif keys[pygame.K_d] and main_character.pos_x < 1230:
            main_character.pos_x += main_character.speed
            main_character.animation_set_type('right')
        elif keys[pygame.K_w] and main_character.pos_y > 50:
            main_character.pos_y -= main_character.speed
            main_character.animation_set_type('left')
        elif keys[pygame.K_s] and main_character.pos_y < 870:
            main_character.pos_y += main_character.speed
            main_character.animation_set_type('left')
        else:
            main_character.animation_set_type('default')

        match main_character.current_animation_type:
            case 'left':
                screen.blit(main_character.animations_left[main_character.current_animation_left],
                            (main_character.pos_x, main_character.pos_y))
                main_character.animation_change_animation_number()
            case 'right':
                screen.blit(main_character.animations_right[main_character.current_animation_right],
                            (main_character.pos_x, main_character.pos_y))
                main_character.animation_change_animation_number()
            case 'up':
                screen.blit(main_character.animations_up[main_character.current_animation_up],
                            (main_character.pos_x, main_character.pos_y))
                main_character.animation_change_animation_number()
            case 'down':
                screen.blit(main_character.animations_down[main_character.current_animation_down],
                            (main_character.pos_x, main_character.pos_y))
                main_character.animation_change_animation_number()
            case 'default':
                screen.blit(main_character.animations_default[main_character.current_animation_default],
                            (main_character.pos_x, main_character.pos_y))
                main_character.animation_change_animation_number()

    else:
        screen.fill("red")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(16)  # фреймтайм