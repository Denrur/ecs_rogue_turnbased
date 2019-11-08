from prefabs.creatures import spawn_npc, add_camera


def add_entities(world):
    add_camera(world)
    player = spawn_npc(world, 'Player', 5, 5)
    goblin = spawn_npc(world, 'Goblin', 10, 10)
    worm = spawn_npc(world, 'Worm', 3, 3)

    return player
