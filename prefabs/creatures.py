from components.action import Action
from components.control import Control
from components.camera import Camera
from components.char_attr import CharAttr
from components.damager import Damager
from components.inventory import Inventory
from components.item import Item
from components.physics import Physics
from components.renderable import Renderable

from utils.layers import Layers


def spawn_npc(world, kind, pos_x, pos_y):
    temp = creatures.get(kind)
    name = temp.get('Name')
    components = temp.get('components')
    ent = world.create_entity(name=name)
    for component in components:
        c = component()
        for attr in [i for i in c.__dict__.keys() if i[:1] != '_']:
            param = temp.get(attr)
            if param:
                c.__setattr__(attr, param)
        if type(c) is Physics:
            c.pos_x, c.pos_y = pos_x, pos_y
            world.entities_position[(c.pos_x, c.pos_y)][0].append(ent)
            if c.collidable:
                world.entities_position[(c.pos_x, c.pos_y)][1] = False
        world.add_component(ent, c)

    return ent


creatures = {'Player': {'Name': 'Player',
                        'components': [Action, Control, Renderable, Physics, Damager, CharAttr, Inventory],
                        'layer': Layers.ENTITIES,
                        'health': 100,
                        'power': 25,
                        'capacity': 26,
                        'color': 'white', 'glyph': '@',
                        'str': 5,
                        'int': 10,
                        'dex': 5,
                        'collidable': True
                        },
             'Goblin': {'Name': 'Goblin',
                        'components': [Action, Renderable, Physics, CharAttr],
                        'layer': Layers.ENTITIES,
                        'health': 30,
                        'color': 'green', 'glyph': 'G',
                        'collidable': True},
             'Worm': {'Name': 'Worm',
                      'components': [Action, Renderable, Physics, CharAttr],
                      'layer': Layers.ENTITIES,
                      'health': 30,
                      'color': 'pink', 'glyph': 's',
                      'collidable': True},
             'Dagger': {'Name': 'Dagger',
                        'components': [Renderable, Physics, Item, Damager],
                        'layer': Layers.ITEMS,
                        'color': 'blue', 'glyph': '-',
                        'coast': 3, 'weight': 5,
                        'collidable': False},
             'Camera': {'Name': 'Camera',
                        'components': [Camera]}
             }


# named_npcs = dict()
#
# named_npcs["Goblin"] = {'Name': "Goblin"}
#
#     Str = 8, Dex = 14, Con = 10, Int = 10, Wis = 8, Cha = 8,
#     HP = 7, Level = 1,
#     Mesh = "SkeletalMesh'/Game/Models/NPC/Goblin/Goblin.Goblin'",
#     StartingSkills = { "Long Blades/2", "Dodging/3" },
#     Equipment = { "Longsword", "Wooden Kite Shield", "Leather Doublet", "Leather Pants", "Leather Boots" },
#     Gold = 2,
#     Description = "A vile goblin, with its heart set on wickedness. Goblins are surprisingly intelligent, but not the slightest bit interested in good behavior.",
#     AI = "Hostile",
#     Glyph = Glyph("g"), FG = C["RED"],
#     LootTable = "Starter Undead",
#     Variants = {
#         chopper = {
#             StartingSkills = { "Axes/2", "Dodging/3" },
#             Equipment = { "Axe", "Wooden Buckler", "Leather Doublet", "Leather Pants", "Leather Boots" },
#             Suffix = "Chopper"
#         },
#         basher = {
#             StartingSkills = { "Blunt Weapons/2", "Dodging/3" },
#             Equipment = { "Mace", "Wooden Buckler", "Leather Doublet", "Leather Pants", "Leather Boots" },
#             Suffix = "Basher"
#         },
#         thumper = {
#             StartingSkills = { "Staves/2", "Dodging/3" },
#             Equipment = { "Wizard's Staff", "Wooden Buckler", "Leather Doublet", "Leather Pants", "Leather Boots" },
#             Suffix = "Witch"
#         },
#         archer = {
#             StartingSkills = { "Bows/2", "Dodging/3" },
#             Equipment = { "Shortbow", "Leather Doublet", "Leather Pants", "Leather Boots" },
#             Suffix = "Archer",
#             Behavior = "Archer",
#         }
#     },
#     AllowStatVariation = true,
#     Faction = "Goblin",
#     Behavior = "Attack"
# }
