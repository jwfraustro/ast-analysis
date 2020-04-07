# Module for the importing, exporting, etc of files
# TODO: Input/Output scripts
from astropy.io import fits



def new_project():
    # TODO
    return


def open_project(file_path):
    # TODO
    return


def save_project(project, save_as=False):
    # TODO
    return


def load_settings(settings_path):
    # TODO
    return


def save_settings(settings):
    # TODO
    return


def export_settings(settings):
    # TODO
    return


def open_fits_file(file_path):
    msg = None
    fits_data = fits.getdata(file_path, lazy_load_hdus=False)[0]
    headers = fits.getheader(file_path)

    return fits_data, headers, msg


def save_fits_file(array, file_path, params):
    # TODO
    return


def export_fits_file(array, file_path, file_type):
    # TODO
    return


def copy_project_file(file):
    # TODO
    return


def paste_project_file(file):
    # TODO
    return


def rename_project_file(file, new_name):
    # TODO
    return


def save_colorspace(colorspace):
    # TODO
    return


def load_colorspace(colorspace):
    # TODO
    return
