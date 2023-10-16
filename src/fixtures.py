import configparser


class Fixture:
    def __init__(self, name: str, num_channels: int):
        self.name = name
        self.num_channels = num_channels


class FixtureManager:
    def __init__(self):
        self.fixtures = []

    def add_fixture(self, name, num_channels):
        fixture = Fixture(name, num_channels)
        self.fixtures.append(fixture)
