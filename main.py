import ursina as ue
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import texture
from ursina.ursinastuff import destroy
from ursina.vec2 import Vec2
from ursina.vec3 import Vec3

app = ue.Ursina()

grass_texture = ue.load_texture('assets/grass_block.png')
brick_texture = ue.load_texture('assets/brick_block.png')
stone_texture = ue.load_texture('assets/stone_block.png')
dirt_texture = ue.load_texture('assets/dirt_block.png')
sky_texture = ue.load_texture('assets/skybox.png')
arm_texture = ue.load_texture('assets/arm_texture.png')

block_chosen = 1
block_dict = {1: grass_texture, 2:brick_texture, 3:stone_texture, 4:dirt_texture}


class Voxel(ue.Button):
    def __init__(self, texture, position=(0,0,0)):
        super().__init__(parent=ue.scene, position=position, model='assets/block.obj', origin_y=0.5, texture=texture, color=ue.color.white, scale=0.5)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position+ue.mouse.normal, texture=block_dict[block_chosen])
            
            elif key == 'right mouse down':
                destroy(self)


class Sky(ue.Entity):
    def __init__(self):
        super().__init__(parent=ue.scene, model='sphere', texture=sky_texture, scale=150, double_sided=True)


class Hand(ue.Entity):
    def __init__(self):
        super().__init__(parent=ue.camera.ui, model='assets/arm', texture=arm_texture, scale=0.2, rotation=Vec3(150, -20, 0), position=Vec2(0.4, -0.6))
    
    def active(self):
        self.position=Vec2(0.3, -0.5)

    def passive(self):
        self.position=Vec2(0.4, -0.6)


def update():
    global block_chosen

    if ue.held_keys['1']: block_chosen = 1
    if ue.held_keys['2']: block_chosen = 2
    if ue.held_keys['3']: block_chosen = 3
    if ue.held_keys['4']: block_chosen = 4

    if ue.held_keys['left mouse'] or ue.held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z), texture=block_dict[block_chosen])


player = FirstPersonController()
hand = Hand()
sky = Sky()

app.run()