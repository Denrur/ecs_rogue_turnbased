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
            blt.color(rend.color)
            blt.layer(rend.layer.value)
            blt.put(rend.x, rend.y, rend.char)
            blt.color('white')
            blt.layer(0)

        blt.refresh()
