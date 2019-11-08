from initialization import init_world
from utils.decorators import open_in_blt


@open_in_blt
def play_game():
    world = init_world()
    while True:
        world.process()


if __name__ == '__main__':
    play_game()
