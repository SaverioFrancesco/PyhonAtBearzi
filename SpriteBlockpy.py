class Ofset:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SpriteBlcok:

    def __init__(self, pygame):
        self.x_size = 16
        self.y_size = 16
        self.x_base = 16
        self.y_base = 16
        self.x_coord = 16
        self.y_coord = 16

        self.image = pygame.image.load("Sprites/Old hero.png").convert()

        color = self.image.get_at((0, 0))

        self.image.set_colorkey(color)

    def draw(self, screen, ofset):
        clip_rect = (self.x_base + ofset.x, self.y_base + ofset.y, self.x_size, self.y_size)

        screen.blit(self.image, [self.x_coord, self.y_coord], clip_rect)


class Puppet(SpriteBlcok):
    PUPPET_STAND = 0
    PUPPET_RUN = 1
    PUPPET_SWIM = 2
    PUPPET_DIE = 3

    def __init__(self, pygame):

        super().__init__(self, pygame)

        self.ofset =  Ofset(16,17)
        self.time = 0

    def draw(self, screen):

        super().draw(self, screen, self.ofset)

    def tick(self):
        self.time += 1

        if self.state == Puppet.PUPPET_STAND:
            pass

        elif self.state == Puppet.PUPPET_RUN:
            pass

    def setState(self, state):
        self.state = state
