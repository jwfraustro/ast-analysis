# Main application file
# TODO: Main app file

from PyQt5.QtWidgets import QApplication
from ast_analysis.resources.window_classes.main_window_class import MainWindow

def run():
    # TODO: Main run function

    app = QApplication([])
    win = MainWindow()
    win.show()
    app.setActiveWindow(win)
    app.exec_()

    return

def load_settings():
    # TODO: Load default/user settings
    return

def save_settings():
    # TODO: Save user settings
    return

if __name__ == '__main__':
    run()