from quadtree import QuadTree, RectData


class Ofset:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = x
        self.dy = y

    def setDefault(self):
        self.x = self.dx
        self.y = self.dy


class SpriteBlock:

    def __init__(self, pygame, imgpath):
        self.x_size = 0
        self.y_size = 0
        self.x_base = 0
        self.y_base = 0
        self.x_coord = 0
        self.y_coord = 0
        self.ofset = None
        self.base_ofset = None
        self.save_rect = None

        # super().__init__(self.x_coord, self.y_coord, self.x_size, self.y_size)

        self.image = pygame.image.load(imgpath).convert()

        color = self.image.get_at((0, 0))

        self.image.set_colorkey(color)
        self.rec = RectData(self.x_coord, self.y_coord, self.x_size, self.y_size, (0, 0, 0, 0))

    def draw(self, screen):
        # print(self.ofset.x)
        clip_rect = (self.x_base + self.ofset.x, self.y_base + self.ofset.y, self.x_size, self.y_size)

        screen.blit(self.image, [self.x_coord, self.y_coord], clip_rect)

    def setPosition(self, x, y):

        if x <= 0: return
        if y <= 0: return

        self.x_coord, self.y_coord = x, y

    def getSize(self):
        return self.x_size, self.y_size


class Puppet(SpriteBlock):
    PUPPET_STAND = 0
    PUPPET_RUN = 1
    PUPPET_SWIM = 2
    PUPPET_DIE = 3

    def __init__(self, pygame, posx, posy):

        super().__init__(pygame, "Sprites/Old hero.png")

        self.x_size = 16
        self.y_size = 15
        self.x_base = 16
        self.y_base = 16
        self.x_coord = posx
        self.y_coord = posy

        self.base_ofset = Ofset(16, 17)  # into the sprite system coordinate
        self.ofset = Ofset(16, 17)  # into the sprite system coordinate
        self.time = 0
        self.animation_step = 0
        self.state = Puppet.PUPPET_STAND

    def tick(self):
        self.time += 1

        if self.state == Puppet.PUPPET_RUN:

            self.ofset.y = self.base_ofset.y * 1
            if self.time % 15 == 0:
                self.animation_step += 1
                self.animation_step = self.animation_step % 6
                self.ofset.x = self.base_ofset.x * self.animation_step

        elif self.state == Puppet.PUPPET_STAND:

            self.ofset.y = self.base_ofset.y * 0
            if self.time % 15 == 0:
                self.animation_step += 1
                self.animation_step = self.animation_step % 3
                self.ofset.x = self.base_ofset.x * self.animation_step

    def setState(self, state):
        self.state = state
        self.ofset.setDefault()


class Tile(SpriteBlock):
    SX = SY = 15

    def __init__(self, pygame, x=0, y=0):
        super().__init__(pygame, "Sprites/psygen.png")

        self.base_ofset = Ofset(0, 0)  # into the sprite system coordinate
        self.ofset = Ofset(0, 0)  # into the sprite system coordinate
        self.y_size, self.x_size = Tile.SX, Tile.SY
        self.x_coord = x
        self.y_coord = y


class Pipe(SpriteBlock):
    SX = SY = 15
    TOP=0
    MID=1
    BOT=2

    def __init__(self, pygame, x=0, y=0, mode=MID):
        super().__init__(pygame, "Sprites/psygen.png")

        self.base_ofset = Ofset(0, 0)  # into the sprite system coordinate
        self.ofset = Ofset(0, 15+mode*15)  # into the sprite system coordinate
        self.y_size, self.x_size = Tile.SX, Tile.SY
        self.x_coord = x
        self.y_coord = y


class CompaundTile:

    def draw(self, screen):
        for t in self.tiles:
            t.draw(screen)

    def setPosition(self, x, y):

        # print(self.tiles)
        for i in range(0, len(self.tiles)):
            (a, b) = (self.tiles[i].getSize())
            self.tiles[i].setPosition(x + i * b, y)

    def register(self):
        for i in self.tiles:
            CollisionDetention.register(i)


class Wall(CompaundTile):

    def __init__(self, pygame, base_x, base_y):
        self.tiles = []

        for i in range(0, 10):
            self.tiles.append(Tile(pygame))
            self.tiles[i].setPosition(base_x, base_y + i * Tile.SY)


class Floar(CompaundTile):

    def __init__(self, pygame, base_x, base_y):
        self.tiles = []

        for i in range(0, 10):
            self.tiles.append(Tile(pygame))

            self.tiles[i].setPosition(base_x + i * Tile.SX, base_y)


class CollisionDetention:
    qt = None

    obj = []

    @classmethod
    def buildStructure(cls, screen_x, screen_y, resolution=8):
        cls.qt = QuadTree(resolution, screen_x, screen_y)

    @classmethod
    def checkCollisions(cls, aabb):
        return False

    @classmethod
    def tick(cls):
        cls.insertRegistred()

    @classmethod
    def moveObject(cls, o, delta_x, delta_y):
        # find the object

        find = False
        for object in cls.obj:
            if object == o:
                find = True
        if find:

            # print(type(o))
            cls.unregister(o)

            selected = [rect for rect in cls.qt.querry(o.x_coord + delta_x, o.y_coord + delta_y, o.x_size, o.y_size)]

            if len(selected) > 0:
                r = RectData(o.x_coord, o.y_coord, o.x_size, o.y_size, (0, 0, 0, 0))
                o.save_rect = r
                cls.qt.add(r)

                return False
            else:
                r = RectData(o.x_coord + delta_x, o.y_coord + delta_y, o.x_size, o.y_size, (0, 0, 0, 0))
                o.setPosition(o.x_coord + delta_x, o.y_coord + delta_y)
                o.save_rect = r
                cls.qt.add(r)
                return True

        else:
            return False

    @classmethod
    def draw(cls, p, s):
        cls.qt.recursiveDraw(p, s)

    @classmethod
    def register(cls, u):
        r = RectData(u.x_coord, u.y_coord, u.x_size, u.y_size, (0, 0, 0, 0))
        u.save_rect = r
        cls.obj.append(u)

    @classmethod
    def registerCompaund(cls, o):
        o.register()

    @classmethod
    def insertRegistred(cls):

        for u in cls.obj:
            r = RectData(u.x_coord, u.y_coord, u.x_size, u.y_size, (0, 0, 0, 0))
            u.save_rect = r
            cls.qt.add(r)

    @classmethod
    def unregister(cls, o):
        cls.qt.remove(o.save_rect)

    @classmethod
    def clearAll(cls):
        cls.qt.clear()
        for u in cls.obj:
            del u.save_rect

    @classmethod
    def query(cls, x, y, w, h):
        return len([rect for rect in cls.qt.querry(x, y, w, h)]) == 0

    @classmethod
    def draw(cls, pygame, display):

        def draw_quadtree(surface, node):
            for n in node.nodes:
                draw_quadtree(surface, n)
                pygame.draw.rect(surface, (192, 192, 192), pygame.Rect(n.x, n.y, n.w + 1, n.h + 1), 1)
                for d in n.data:
                    pygame.draw.rect(surface, d.data, pygame.Rect(d.x, d.y, d.w, d.h))
            for d in node.data:
                pygame.draw.rect(surface, d.data, pygame.Rect(d.x, d.y, d.w, d.h))

        n = cls.qt.root
        draw_quadtree(display, n)
