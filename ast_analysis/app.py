# Main application file
# TODO: Main app file
import sys
from PyQt5.QtWidgets import QApplication
from ast_analysis.resources.window_classes.main_window_class import MainWindow

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

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
    sys.excepthook = my_exception_hook
    run()