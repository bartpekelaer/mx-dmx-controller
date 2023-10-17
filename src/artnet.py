from pyartnet import ArtNetNode


class ArtnetNodeManager:
    def __init__(self):
        self.node = ArtNetNode('10.0.0.23', 6454)

    def start_node(self):
        self.node.start()
