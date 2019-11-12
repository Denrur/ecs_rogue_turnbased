from components.action import Action
from components.damager import Damager
from components.inventory import Inventory
from components.item import Item
from components.physics import Physics
from components.renderable import Renderable

from utils.esper import Processor


class ActionProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        print(f'Action Processor {self.world.timer=}'.center(100, '#'))
        ent = self.current_entity
        print(f'current action entity {ent.name=}')
        action = self.world.component_for_entity(ent, Action)
        phys = self.world.component_for_entity(ent, Physics)
        dmg = self.world.component_for_entity(ent, Damager)
        if action.type == 'move':

            phys.dest_x, phys.dest_y = action.param
            phys.move = action.flag
            action.type = None

        elif action.type == 'attack':
            dmg.dest_x, dmg.dest_y = action.param
            dmg.attack = action.flag
            action.type = None

        elif action.type == 'pickup':
            pass
            items = [k for k, (p, i) in self.world.get_components(Physics, Item)
                     if (p.pos_x, p.pos_y) == (phys.pos_x, phys.pos_y)]
            print(f'{items=}')
            if len(items) > 0:
                self.pickup_item(ent, items[0])
            else:
                print('Nothing to pick up')
        elif action.type == 'drop':
            inventory = self.world.component_for_entity(ent, Inventory)
            if len(inventory.items) > 0:
                item = inventory.items[0]
                self.drop_item(ent, item)
                item_phys = self.world.component_for_entity(item, Physics)
                print(f'Dropped {item.name=} in {item_phys.pos_x=} {item_phys.pos_y=}')
                print(f'Dropped {ent.name=} in {phys.pos_x=} {phys.pos_y=}')
            else:
                print('Nothing to drop')

    def pickup_item(self, entity, item):
        if self.world.has_component(item, Item):
            self.add_item(entity, item)
            self.world.remove_component(item, Physics)
            rend = self.world.component_for_entity(item, Renderable)
            rend.renderable = False

    def add_item(self, entity, item):
        inventory = self.world.component_for_entity(entity, Inventory)
        if len(inventory.items) >= inventory.capacity:
            print('Inventory is full')
        else:
            inventory.items.append(item)
        for ind, item in enumerate(inventory.items):
            print(f'{ind} {item.name}')

    def drop_item(self, entity, item):
        self.world.add_component(item, Physics())
        rend = self.world.component_for_entity(item, Renderable)
        rend.renderable = True
        item_phys = self.world.component_for_entity(item, Physics)
        entity_phys = self.world.component_for_entity(entity, Physics)

        item_phys.pos_x = entity_phys.pos_x
        item_phys.pos_y = entity_phys.pos_y

        self.remove_item(entity, item)

    def remove_item(self, entity, item):
        inventory = self.world.component_for_entity(entity, Inventory)
        inventory.items.remove(item)
        for ind, item in enumerate(inventory.items):
            print(f'{ind} {item.name}')
