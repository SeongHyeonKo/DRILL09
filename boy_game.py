from pico2d import *


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
FRAME_DELAY = 0.05


def main():
    open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
    background = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    running = True

    while running:
        clear_canvas()
        background.draw(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        character.clip_draw(0, 300, 100, 100, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        update_canvas()

        for event in get_events():
            if event.type == SDL_QUIT:
                running = False

        delay(FRAME_DELAY)

    close_canvas()


if __name__ == '__main__':
    main()
