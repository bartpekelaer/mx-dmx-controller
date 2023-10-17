import asyncio
from pyartnet import ArtNetNode


class ArtnetNodeManager:
    def __init__(self):
        self.node = None
        self.universe = None

    async def start_node(self):
        self.node = ArtNetNode('10.0.0.23', 6454)
        self.universe = self.node.add_universe(0)

        await self.node.start()
