import pygame
from random import randint, choice

pygame.init()

screen_surface = pygame.display.set_mode( (600,800) )
game_status = True
FPS = 144
clock = pygame.time.Clock()

def load_image(path: str, pos):

    img = pygame.image.load(path)
    surface = img.convert()
    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)
    rect = surface.get_rect(center=pos)

    return [img, surface, rect]

def print_image(img_list):
    img, surface, rect = img_list
    screen_surface.blit(surface, rect)

player_pos = [300, 400]
player = load_image('player.png', player_pos)

def player_movement(keys, delta_speed):
    x = 0
    y = 0
    speed = 600 * delta_speed

    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed

    return [x,y]

def update_pos(img_list, pos):
    img, surface, rect = img_list
    rect = surface.get_rect(center=pos)
    return [img, surface, rect] 

def limit(pos):
    x, y = pos
    x = max(0, min(x, 600))
    y = max(0, min(y, 800))
    return [x,y]

bonus_list = ['bonus_1.png', 'bonus_2.png', 'bonus_3.png']
bonus_objects = []

def generate_bonus():
    bonus_img = choice(bonus_list)

    x = randint(0,600)
    y = randint(0,800)
    pos = [x,y]

    obj = load_image(bonus_img, pos)
    bonus_objects.append(obj)

def print_bonuses():
    for obj in bonus_objects:
        print_image(obj)

total_ticks = 0
points = 0

def check_collisions():
    global points
    rect_player = player[2]
    for index in range(len(bonus_objects) - 1, -1, -1):
        obj = bonus_objects[index]
        rect = obj[2]
        if rect.colliderect(rect_player):
            bonus_objects.pop(index)
            points += 1

FONT = pygame.font.SysFont('ebrima', 20)

def print_points(points):
    txt = f'Points: {points}'
    color = [255,255,255]
    pos = [0,0]
    label = FONT.render(txt, False, color)
    screen_surface.blit(label, pos)

while game_status:
    
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
    # MIĘDZY EVENTS

    keys = pygame.key.get_pressed()

    delta_time = clock.get_time() / 1000.0
    x, y = player_movement(keys, delta_time)

    player_pos[0] += x
    player_pos[1] += y
    player_pos = limit(player_pos)
    player = update_pos(player, player_pos)

    # MIĘDZY PRINT
    background_color = [9,42,121]
    screen_surface.fill(background_color)

    if total_ticks % (FPS * 1) == 0:
        generate_bonus()
    check_collisions()
    print_points(points)
    print_bonuses()

    print_image(player)
    pygame.display.update()
    clock.tick(FPS)
    total_ticks += 1

pygame.quit()
quit()