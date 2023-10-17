import sys

from PySide6 import QtWidgets

from src.gui import MainWindow
from src.artnet import ArtnetNodeManager


async def start_dmx_broadcast():
    node = ArtnetNodeManager()
    await node.start_node()


def main() -> None:
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    start_dmx_broadcast()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
