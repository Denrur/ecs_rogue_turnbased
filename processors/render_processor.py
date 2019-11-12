from bearlibterminal import terminal as blt

from components.renderable import Renderable

from utils.esper import Processor


class RenderProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.fps = 4

    def process(self, *args, **kwargs):
        print(f'Render Processor'.center(100, '#'))

        blt.clear()

        for ent, rend in self.world.get_component(Renderable):
            if rend.renderable:
                render_entity(rend)

                print(f'{ent.name=} {rend.rend_x=} {rend.rend_y=}')

        blt.refresh()


def render_entity(rend):
    blt.color(rend.color)
    blt.layer(rend.layer.value)
    blt.put(rend.rend_x, rend.rend_y, rend.glyph)
    blt.color('white')
    blt.layer(0)
