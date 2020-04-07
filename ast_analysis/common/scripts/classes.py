from astropy.io import fits


class FITS_File:
    def __init__(self, file_path):
        self.file_path = file_path

        self.header = None
        self.frames = []

    def open(self):
        self.frames = fits.getdata(self.file_path, lazy_load_hdus=False)
        self.header = fits.getheader(self.file_path)

    def save(self):
        #TODO
        return

    def export(self, file_name, format):
        #TODO
        return

    def header_as_dict(self):
        #TODO
        return
