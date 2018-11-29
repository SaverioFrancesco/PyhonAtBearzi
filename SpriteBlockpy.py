class Ofset:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = x
        self.dy = y

    def setDefault(self):
        self.x = self.dx
        self.y = self.dy


class AABB:

    def __init__(self, b_x, b_y, s_x, s_y):
        self.b_x, self.b_y, self.s_x, self.s_y = b_x, b_y, s_x, s_y

    def inside(self, aabb):
        nb1 = self.b_x + self.s_x < aabb.b_x or self.b_x > aabb.b_x + aabb.s_x
        nb2 = self.b_y + self.s_y < aabb.b_y or self.b_y > aabb.b_y + aabb.s_y
        return not (nb1 or nb2)

    def draw(self, pygame, screen, fill=False):
        """debug only"""
        if not fill:
            pygame.draw.polygon(screen, (0, 0, 0), [[self.b_x, self.b_y], [self.b_x, self.b_y + self.s_y],
                                                    [self.b_x + self.s_x, self.b_y + self.s_y],
                                                    [self.b_x + self.s_x, self.b_y]], 1)

    def setPos(self, x, y):
        self.b_x, self.b_y = x, y


class SpriteBlock(AABB):

    def __init__(self, pygame, imgpath):
        self.x_size = 0
        self.y_size = 0
        self.x_base = 0
        self.y_base = 0
        self.x_coord = 0  # note, this is  redundant since we inherit from AABB b_x ...
        self.y_coord = 0
        self.ofset = None
        self.base_ofset = None

        super().__init__(self.x_coord, self.y_coord, self.x_size, self.y_size)

        self.image = pygame.image.load(imgpath).convert()

        color = self.image.get_at((0, 0))

        self.image.set_colorkey(color)

        QuadTreeCollisionDetntion.obj_registred.append(self)

    def draw(self, screen):
        print(self.ofset.x)
        clip_rect = (self.x_base + self.ofset.x, self.y_base + self.ofset.y, self.x_size, self.y_size)

        screen.blit(self.image, [self.x_coord, self.y_coord], clip_rect)

    def setPosition(self, x, y):
        self.x_coord, self.y_coord = x, y
        super().setPos(x, y)

    def getSize(self):
        return self.x_size, self.y_size


class Puppet(SpriteBlock):
    PUPPET_STAND = 0
    PUPPET_RUN = 1
    PUPPET_SWIM = 2
    PUPPET_DIE = 3

    def __init__(self, pygame):

        super().__init__(pygame, "Sprites/Old hero.png")

        self.x_size = 16
        self.y_size = 16
        self.x_base = 16
        self.y_base = 15
        self.x_coord = 16
        self.y_coord = 16

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

    def __init__(self, pygame):
        super().__init__(pygame, "Sprites/psygen.png")

        self.base_ofset = Ofset(0, 0)  # into the sprite system coordinate
        self.ofset = Ofset(0, 0)  # into the sprite system coordinate
        self.y_size, self.x_size = Tile.SX, Tile.SY


class Wall():

    def __init__(self, pygame, base_x, base_y):

        self.tiles = []

        for i in range(0, 10):
            self.tiles.append(Tile(pygame))

            self.tiles[i].setPosition(base_x, base_y + i * Tile.SY)

    def draw(self, screen):
        for t in self.tiles:
            t.draw(screen)

    def setPosition(self, x, y):

        # print(self.tiles)
        for i in range(0, len(self.tiles)):
            (a, b) = (self.tiles[i].getSize())
            self.tiles[i].setPosition(x, y + i * b)


class Floar():

    def __init__(self, pygame, base_x, base_y):

        self.tiles = []

        for i in range(0, 10):
            self.tiles.append(Tile(pygame))

            self.tiles[i].setPosition(base_x + i * Tile.SX, base_y)

    def draw(self, screen):
        for t in self.tiles:
            t.draw(screen)

    def setPosition(self, x, y):

        # print(self.tiles)
        for i in range(0, len(self.tiles)):
            (a, b) = (self.tiles[i].getSize())
            self.tiles[i].setPosition(x + i * b, y)


class Quadrant(AABB):

    def __init__(self, b_x, b_y, s_x, s_y, boxes, level_left=0):

        super().__init__(b_x, b_y, s_x, s_y)

        if level_left > 0:
            q1 = []
            q2 = []
            q3 = []
            q4 = []

            for b in boxes:
                if b.inside(AABB(b_x + s_x / 2, b_y + 0, s_x, s_y / 2)):
                    q1.append(b)
                elif b.inside(AABB(b_x + 0, b_y + 0, s_x / 2, s_y / 2)):
                    q2.append(b)
                elif b.inside(AABB(b_x + 0, b_y + s_y / 2, s_x / 2, s_y)):
                    q3.append(b)
                elif b.inside(AABB(b_x + s_x / 2, b_y + s_y / 2, s_x, s_y)):
                    q4.append(b)

            self.aabb1 = Quadrant(b_x + s_x / 2, b_y, s_x / 2, s_y / 2, q1, level_left - 1)

            self.aabb2 = Quadrant(b_x, b_y, s_x / 2, s_y / 2, q2, level_left - 1)

            self.aabb3 = Quadrant(b_x, b_y + s_y / 2, s_x / 2, s_y / 2, q3, level_left - 1)

            self.aabb4 = Quadrant(b_x + s_x / 2, b_y + s_y / 2, s_x / 2, s_y / 2, q4, level_left - 1)

        else:
            self.boxes = boxes
            self.aabb1 = None
            self.aabb2 = None
            self.aabb3 = None
            self.aabb4 = None

    def recursiveDraw(self, p, y):

        if self.aabb1 != None:
            self.aabb1.draw(p, y)
            self.aabb1.recursiveDraw(p, y)
        if self.aabb2 != None:
            self.aabb2.draw(p, y)
            self.aabb2.recursiveDraw(p, y)
        if self.aabb3 != None:
            self.aabb3.draw(p, y)
            self.aabb3.recursiveDraw(p, y)
        if self.aabb4 != None:
            self.aabb4.draw(p, y)
            self.aabb4.recursiveDraw(p, y)


class QuadTreeCollisionDetntion:
    obj_registred = []
    qadr = None

    @classmethod
    def buildStructure(cls, screen_x, screen_y, resolution=5):
        cls.qadr = Quadrant(0, 0, screen_x, screen_y, cls.obj_registred, resolution)

    @classmethod
    def checkCollisions(cls, aabb):
        return False

    @classmethod
    def tick(cls):
        pass

    @classmethod
    def draw(cls, p, s):
        cls.qadr.recursiveDraw(p, s)
