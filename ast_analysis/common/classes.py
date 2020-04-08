from astropy.io import fits

class Project:
    def __init__(self):

        self.file_path = None
        self.target_frame = None
        self.bias_frames = []
        self.flat_frames = []
        self.lamp_frames = []

    def open_project(self, file_path):
        # TODO
        return

    def save_project(self, file_path):
        # TODO
        return

    def load_target_frame(self, file_path):

        target_frame = FITS_File(file_path)
        self.target_frame = target_frame
        return

    def clear_target_frame(self):
        self.target_frame = None
        return

    def load_bias_frames(self, file_paths):

        for file in file_paths:
            bias_frame = FITS_File(file)
            self.bias_frames.append(bias_frame)
        return

    def delete_bias_frame(self, file_name):
        for file in self.bias_frames:
            if file.file_name == file_name:
                self.bias_frames.remove(file)
        return

    def clear_bias_frames(self):
        self.bias_frames.clear()
        return

    def load_flat_frames(self, file_paths):
        for file in file_paths:
            flat_frame = FITS_File(file)
            self.flat_frames.append(flat_frame)
        return

    def delete_flat_frame(self, file_name):
        for file in self.flat_frames:
            if file.file_name == file_name:
                self.flat_frames.remove(file)
        return

    def clear_flat_frames(self):
        self.flat_frames.clear()
        return

    def load_lamp_frames(self, file_paths):
        for file in file_paths:
            lamp_frame = FITS_File(file)
            self.lamp_frames.append(lamp_frame)
        return

    def clear_lamp_frame(self):
        self.lamp_frames.clear()
        return

class FITS_File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.frames = fits.getdata(self.file_path, lazy_load_hdus=False)
        self.header = fits.getheader(self.file_path)
        self.file_name = self.file_path.split("/")[-1]

        return
    def save(self):
        #TODO
        return

    def export(self, file_name, format):
        #TODO
        return

    def header_as_dict(self):
        #TODO
        return
