from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('kirby.png')
hand_arrow = load_image('hand_arrow.png')


def handle_events():
    global direction
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def move_towards_target():
    global x, y, target_x, target_y, direction
    speed = 2
    distance = math.sqrt((target_x - x) ** 2 + (target_y - y) ** 2)
    if distance > speed:
        angle = math.atan2(target_y - y, target_x - x)
        x += speed * math.cos(angle)
        y += speed * math.sin(angle)
        direction = 1 if target_x > x else 0
    else:
        x, y = target_x, target_y
        target_x, target_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
target_x, target_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
frame = 0
hide_cursor()
direction = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    move_towards_target()

    if direction == 1:
        character.clip_draw(frame * 65, 0, 65, 45, x, y, 100, 100)
    elif direction == 0:
        character.clip_composite_draw(frame * 65, 0, 65, 45, 0, 'h', x, y, 100, 100)

    hand_arrow.draw(target_x, target_y)

    update_canvas()
    frame = (frame +1) % 8

    handle_events()

close_canvas()




