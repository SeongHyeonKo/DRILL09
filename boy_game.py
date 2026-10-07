from pico2d import *


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
FRAME_DELAY = 0.05
MOVE_STEP = 5
SPRITE_SIZE = 100
FRAME_COUNT = 8
IDLE_ROW_RIGHT = 300
IDLE_ROW_LEFT = 200
RUN_ROW_RIGHT = 100
RUN_ROW_LEFT = 0
START_X = SCREEN_WIDTH // 2
START_Y = SCREEN_HEIGHT // 2
MOVEMENT_KEYS = (SDLK_UP, SDLK_DOWN, SDLK_LEFT, SDLK_RIGHT)


def main():
    open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
    background = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    running = True
    pressed_keys = []
    x = START_X
    y = START_Y
    facing_right = True
    frame = 0

    while running:
        clear_canvas()
        background.draw(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        if pressed_keys:
            animation_row = RUN_ROW_RIGHT if facing_right else RUN_ROW_LEFT
        else:
            animation_row = IDLE_ROW_RIGHT if facing_right else IDLE_ROW_LEFT
        character.clip_draw(frame * SPRITE_SIZE, animation_row, SPRITE_SIZE, SPRITE_SIZE, x, y)
        update_canvas()
        frame = (frame + 1) % FRAME_COUNT

        for event in get_events():
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
            elif event.type == SDL_KEYDOWN and event.key in MOVEMENT_KEYS:
                if event.key not in pressed_keys:
                    pressed_keys.append(event.key)
            elif event.type == SDL_KEYUP and event.key in MOVEMENT_KEYS:
                if event.key in pressed_keys:
                    pressed_keys.remove(event.key)

        if pressed_keys:
            active_key = pressed_keys[0]
            if active_key == SDLK_UP:
                y += MOVE_STEP
            elif active_key == SDLK_DOWN:
                y -= MOVE_STEP
            elif active_key == SDLK_LEFT:
                x -= MOVE_STEP
                facing_right = False
            elif active_key == SDLK_RIGHT:
                x += MOVE_STEP
                facing_right = True

        x = max(SPRITE_SIZE // 2, min(SCREEN_WIDTH - SPRITE_SIZE // 2, x))
        y = max(SPRITE_SIZE // 2, min(SCREEN_HEIGHT - SPRITE_SIZE // 2, y))

        delay(FRAME_DELAY)

    close_canvas()


if __name__ == '__main__':
    main()
