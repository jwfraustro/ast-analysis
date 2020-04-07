# Module to build/convert QtDesigner forms into PyQt forms
import os
from pathlib import Path
from glob import glob

QT_FORMS_PATH = "../resources/forms/qt_forms/"
BUILD_PATH = "../resources/forms/"


def get_qt_forms():
    return glob(QT_FORMS_PATH + "*.ui")


def build_forms():
    qt_forms = get_qt_forms()

    for form in qt_forms:
        form_name = Path(form).stem
        os.system("pyuic5 %s -o %s" % (form, BUILD_PATH + form_name + ".py"))
    return

if __name__ == '__main__':
    build_forms()
