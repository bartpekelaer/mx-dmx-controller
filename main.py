import sys
import asyncio

from PySide6 import QtWidgets

from src.gui import MainWindow
from src.artnet import ArtnetNodeManager


async def artnet():
    artnet_manager = ArtnetNodeManager()
    asyncio.create_task(artnet_manager.start_node())


def main() -> None:
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    artnet()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
