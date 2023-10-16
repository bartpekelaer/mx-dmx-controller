import configparser

ui_section = 'ui'


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('settings.cfg')

        # UI
        self.app_name = str(self.config.get(ui_section, 'title'))
        self.__version__ = str(self.config.get(ui_section, 'version'))
        self.loc_x = int(self.config.get(ui_section, 'loc_x'))
        self.loc_y = int(self.config.get(ui_section, 'loc_y'))
        self.height = int(self.config.get(ui_section, 'height'))
        self.width = int(self.config.get(ui_section, 'width'))
        self.tab_1 = str(self.config.get(ui_section, 'tab_1'))
        self.tab_2 = str(self.config.get(ui_section, 'tab_2'))


config = Config()
