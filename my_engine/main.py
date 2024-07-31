import pygame
import pygame.gfxdraw
from render import obj3D, Camera
from math import pi

pygame.init()

WIDTH, HEIGHT = 1600, 800
# WIDTH, HEIGHT = 1920, 1000
# COLORS = [(255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 0, 0),
#           (0, 255, 0), (0, 255, 0), (0, 0, 255), (0, 0, 255),
#           (0, 255, 255), (0, 255, 255), (255, 0, 255), (255, 0, 255)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
millisec = 0
flag = True


def animation(surf, obj, camera=None, lighting=None):
    global millisec
    millisec += clock.get_time()

    if millisec > 10:
        angle = 1

        # obj.Zrotate(angle * (pi / 180))
        obj.Yrotate(angle * (pi / 180))
        obj.Xrotate(angle / 4 * (pi / 180))
        draw(surf, obj, camera, lighting)
        millisec = 0


def draw(surf, object, camera, lighting): # can be write as decorator for pygame draw func
    # mash_need=True, dots_need=True, normalies_need=False, faces_need=False
    surf.fill((79, 79, 98))

    hide_faces = False
    if camera:
        hide_faces = True
    v_data = object.vertexes
    faces = object.faces
    # нужно поделить на компоненту w,
    # чтобы перевести корды точек из однородных координат в обычные
    reform_v = [list(map(lambda x: x / i[-1], i))[:2] for i in v_data]
    vertexes = list(map(lambda x: [x[0] + WIDTH / 2, x[1] + HEIGHT / 2], reform_v))
    normalies = object.normalies

    # print(faces, v)
    # print(normalies)
    # need to optimize

    c = 0
    for f in faces:
                
        pl = list()
        for i in range(len(f)):
            pl.append(vertexes[f[i] - 1])
        # print(pl)

        # k = 2
        # a, a1 = [pl[0][0], pl[0][1]], [(pl[1][0] + pl[2][0]) / 2, (pl[1][1] + pl[2][1]) / 2]
        # f_center = [(a[0] + k * a1[0]) / (k + 1), (a[1] + k * a1[1]) / (k + 1)]
        # # print(pl, [a, a1], f_center)
        # # pygame.draw.circle(surf, (255, 0, 0), f_center, 2)

        # n = [[f_center[0], f_center[1]], 
        #      [normalies[c][0] + f_center[0], normalies[c][1] + f_center[1]]]
        # pygame.draw.line(surf, (255, 0, 0), n[0], n[1], 2)

        if hide_faces:
            # print(camera.check(normalies[c]))
            shade = abs(lighting.check(normalies[c]))
            if camera.check(normalies[c]) < 0: # broken normalies

                # pygame.draw.polygon(surf, (0, 0, 0), pl, 2)
                pygame.gfxdraw.filled_polygon(surf, pl, (255 * shade, 255 * shade, 255 * shade))
                pass
                # painter algorythm...
            else:
                # pygame.draw.polygon(surf, (255, 0, 0), pl, 2)
                pass
        c += 1

        # pygame.draw.polygon(surf, (0, 0, 0), pl, 2)
        
        # for v in pl:
        #     pygame.draw.circle(surf, (255, 99, 20), v, 2)
        #     pass


cm1 = Camera()
light = Camera([-5, -10, -10])
md1 = obj3D("C:/Users/nsusc/Desktop/theGame/suzanne.obj")
md1.scale(200)
md1.Yrotate(-43.005 * (pi / 180))
md1.Zrotate(180 * (pi / 180))
md1.move((0, 150, 0))
# cube rote
# md1.Yrotate(30 * (pi / 180))
# md1.Xrotate(45 * (pi / 180))

# md1.move((200, 200, 200))

# draw(screen, md1, cm1, light)

while flag:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    
    animation(screen, md1, cm1, light)

    pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.flip()

    clock.tick(62)

pygame.quit()