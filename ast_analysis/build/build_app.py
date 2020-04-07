# Script to compile app with Pyinstaller
import os

APP_PATH = "\"../__main__.py\""
BUILD_DIR = "../build/"

def run():
    version = "0.0.1"
    one_file = False
    app_name = "FITS Graphical Analyzer"
    overwrite_build = True
    clean_temp_files = True
    console = True

    build_name = "\"" + app_name + " " + version + "\""

    command = "pyinstaller "

    if clean_temp_files:
        command += "--clean "

    if one_file:
        command += "-F "
    else:
        command += "-D "

    if not console:
        command += "--noconsole "

    command += "--name " + build_name

    command += " " + APP_PATH

    print(command)

    os.system(command)

    return


if __name__ == '__main__':
    run()
