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

        self.image = pygame.image.load(imgpath).convert()

        color = self.image.get_at((0, 0))

        self.image.set_colorkey(color)

    def draw(self, screen):
        print(self.ofset.x)
        clip_rect = (self.x_base + self.ofset.x, self.y_base + self.ofset.y, self.x_size, self.y_size)

        screen.blit(self.image, [self.x_coord, self.y_coord], clip_rect)

    def setPosition(self, x, y):
        self.x_coord, self.y_coord = x, y

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
    SX= SY =15

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

        #print(self.tiles)
        for i in range(0, len(self.tiles)):
            (a, b) = (self.tiles[i].getSize())
            self.tiles[i].setPosition(x, y + i * b)

class Floar():

    def __init__(self, pygame, base_x, base_y):

        self.tiles = []

        for i in range(0, 10):
            self.tiles.append(Tile(pygame))

            self.tiles[i].setPosition(base_x + i * Tile.SX, base_y )

    def draw(self, screen):
        for t in self.tiles:
            t.draw(screen)

    def setPosition(self, x, y):

        #print(self.tiles)
        for i in range(0, len(self.tiles)):
            (a, b) = (self.tiles[i].getSize())
            self.tiles[i].setPosition(x + i * b, y )
