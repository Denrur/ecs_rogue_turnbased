from prefabs.creatures import spawn_npc


def add_entities(world):
    spawn_npc(world, 'Camera', 0, 0)
    player = spawn_npc(world, 'Player', 5, 5)
    goblin = spawn_npc(world, 'Goblin', 10, 10)
    worm = spawn_npc(world, 'Worm', 3, 3)
    spawn_npc(world, 'Dagger', 5, 6)

    return player
