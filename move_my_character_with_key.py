from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('kirby.png')


def handle_events():
    global running, dirX, dirY, direction

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
                direction = 2

            elif event.key == SDLK_LEFT:
                dirX -= 1
                direction = 1

            elif event.key == SDLK_UP:
                dirY += 1
                direction = 3

            elif event.key == SDLK_DOWN:
                dirY -= 1
                direction = 4

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                direction = 0
            elif event.key == SDLK_LEFT:
                dirX += 1
                direction = 0
            elif event.key == SDLK_UP:
                dirY -= 1
                direction = 0
            elif event.key == SDLK_DOWN:
                dirY += 1
                direction = 0


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
stopFrame = 0
updownFrame = 0
dirX = 0
dirY = 0
direction = 0   #0 멈춤, 1 좌, 2 우, 3 상, 4 하

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if direction == 2:
        character.clip_draw(frame * 65, 0, 65, 45, x, y, 100, 100)
    elif direction == 1:
        character.clip_composite_draw(frame * 65, 0, 65, 45, 0, 'h', x, y, 100, 100)
    elif direction == 3 or direction == 4:
        character.clip_draw(updownFrame * 85 + 220, 270, 85, 75, x, y, 100, 100)
    else:
        character.clip_draw(stopFrame * 45, 450, 45, 35, x, y, 100, 100)

    update_canvas()
    handle_events()

    if direction !=0:
        frame = (frame +1) % 8
        updownFrame = (updownFrame + 1) % 2
    else:
        stopFrame = (stopFrame + 1) % 2

    #frame = (frame + 1) % 8
    x += dirX * 10
    y += dirY * 10
    if(x >TUK_WIDTH or x < 0):
        x -= dirX * 10
    if(y > TUK_HEIGHT - 100 or y < 150):
        y -= dirY * 10
    delay(0.1)


close_canvas()

