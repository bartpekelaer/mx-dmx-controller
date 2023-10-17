from PySide6 import QtWidgets, QtCore

from src.config import config
from src.fixtures import Luxibel
from src.artnet import ArtnetNodeManager

node = ArtnetNodeManager()
universe = node.universe


luxibel = Luxibel()
# universe.add_channel(width=luxibel.num_channels, start=1, name=luxibel.name)


def luxibel_red():
    lux = universe.get_channel(luxibel.name)
    lux.set_values([0, 255, 0, 0, 0, 0])


class BaseTab(QtWidgets.QTabWidget):
    def __init__(self, layout=None):
        super().__init__()
        if layout:
            self.layout = layout(self)
        else:
            self.layout = QtWidgets.QVBoxLayout(self)


class Tab1(BaseTab):
    def __init__(self):
        super().__init__(layout=QtWidgets.QGridLayout)

        self.luxibel_label = QtWidgets.QLabel('Luxibel BPar 180 RGBW')
        self.luxibel_button_red = QtWidgets.QPushButton('Red')
        self.luxibel_button_red.clicked.connect(luxibel_red)
        self.luxibel_button_green = QtWidgets.QPushButton('Green')
        self.luxibel_button_blue = QtWidgets.QPushButton('Blue')
        self.luxibel_button_white = QtWidgets.QPushButton('White')

        self.layout.addWidget(self.luxibel_label, 0, 0)
        self.layout.addWidget(self.luxibel_button_red, 0, 1)
        self.layout.addWidget(self.luxibel_button_green, 0, 2)
        self.layout.addWidget(self.luxibel_button_blue, 0, 3)
        self.layout.addWidget(self.luxibel_button_white, 0, 4)

        self.luxibel_label_dim = QtWidgets.QLabel('Dimmer')
        self.luxibel_dimmer = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)

        self.luxibel_dimmer.setMinimum(0)
        self.luxibel_dimmer.setMaximum(255)
        self.luxibel_dimmer.setValue(0)

        self.layout.addWidget(self.luxibel_label_dim, 1, 0)
        self.layout.addWidget(self.luxibel_dimmer, 1, 1, 1, 2)

        self.layout.rowStretch(2)

        self.xoop_label = QtWidgets.QLabel('Xoop EL100 CW/WW')
        self.xoop_button_ww = QtWidgets.QPushButton('Warm White')
        self.xoop_button_cww = QtWidgets.QPushButton('Mixed White')
        self.xoop_button_cw = QtWidgets.QPushButton('Cool White')

        self.layout.addWidget(self.xoop_label, 2, 0)
        self.layout.addWidget(self.xoop_button_ww, 2, 1)
        self.layout.addWidget(self.xoop_button_cww, 2, 2)
        self.layout.addWidget(self.xoop_button_cw, 2, 3)

        self.xoop_label_dim = QtWidgets.QLabel('Dimmer')
        self.xoop_dimmer = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.xoop_dimmer.setMinimum(0)
        self.xoop_dimmer.setMaximum(255)
        self.xoop_dimmer.setValue(0)

        self.layout.addWidget(self.xoop_label_dim, 3, 0)
        self.layout.addWidget(self.xoop_dimmer, 3, 1, 1, 2)

        self.layout.rowStretch(2)

        self.scena_label = QtWidgets.QLabel('DTS Scena LED 80CT')
        self.scena_button_ww = QtWidgets.QPushButton('Warm White')
        self.scena_button_cww = QtWidgets.QPushButton('Mixed White')
        self.scena_button_cw = QtWidgets.QPushButton('Cold White')

        self.layout.addWidget(self.scena_label, 4, 0)
        self.layout.addWidget(self.scena_button_ww, 4, 1)
        self.layout.addWidget(self.scena_button_cww, 4, 2)
        self.layout.addWidget(self.scena_button_cw, 4, 3)

        self.scena_label_dim = QtWidgets.QLabel('Dimmer')
        self.scena_dimmer = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.scena_dimmer.setMinimum(0)
        self.scena_dimmer.setMaximum(255)
        self.scena_dimmer.setValue(0)

        self.layout.addWidget(self.scena_label_dim, 5, 0)
        self.layout.addWidget(self.scena_dimmer, 5, 1, 1, 2)
        self.layout.rowStretch(2)


class Tab2(BaseTab):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel('This is the settings tab')
        self.layout.addWidget(self.label)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'{config.app_name} V: {config.__version__}')
        self.setGeometry(config.loc_x, config.loc_y, config.width, config.height)
        QtWidgets.QApplication.instance().setStyle('Fusion')

        self.tab_widget = QtWidgets.QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.tab_widget.addTab(Tab1(), config.tab_1)
        self.tab_widget.addTab(Tab2(), config.tab_2)
