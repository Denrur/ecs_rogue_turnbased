from math import sqrt


def distance_to(start, goal):
    return sqrt((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2)


if __name__ == '__main__':

    start = (0, 0)
    goal = (1, 1)

    dist = distance_to(start, goal)
    print(dist)
