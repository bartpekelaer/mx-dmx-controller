import configparser

fixture = configparser.ConfigParser()
fixture.read('fixtures.cfg')


class Fixture:
    def __init__(self, name: str, num_channels: int):
        self.name = name
        self.num_channels = num_channels


class Luxibel(Fixture):
    def __init__(self):
        super().__init__(str(fixture.get('luxibel', 'name')), int(fixture.get('luxibel', 'channels')))

    @staticmethod
    def dim():
        return 1, 255

    @staticmethod
    def red():
        return 2, 255

    @staticmethod
    def green():
        return 3, 255

    @staticmethod
    def blue():
        return 4, 255

    @staticmethod
    def white():
        return 5, 255

    @staticmethod
    def strobe():
        return 6, 0

    def __str__(self):
        return 'Channel 1: Dim, Channel 2: Red, Channel 3: Green, Channel 4: Blue, Channel 5: White, Channel 6: Strobe'


class Xoop(Fixture):
    def __init__(self):
        super().__init__(str(fixture.get('xoop', 'name')), int(fixture.get('xoop', 'channels')))

    def __str__(self):
        return 'Channel 1: Dim, Channel 2: Cold White, Channel 3: Warm White'


class Scena(Fixture):
    def __init__(self):
        super().__init__(str(fixture.get('scena', 'name')), int(fixture.get('scena', 'channels')))

    def __str__(self):
        return 'Channel 1: Warm White, Channel 2: Cold White, Channel 3: Shutter, Channel 4: Dim, Channel 5: Dimmer Fine, Channel 6: CCT, Channel 7: FUNCS'
