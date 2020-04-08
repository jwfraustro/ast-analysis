from astropy.io import fits
import json

class Project:
    def __init__(self):

        self.project_name = None
        self.file_path = None
        self.target_frame = None
        self.bias_frames = []
        self.flat_frames = []
        self.lamp_frames = []

    def is_empty(self):
        if self.file_path:
            return False
        if self.target_frame:
            return False
        if self.bias_frames:
            return False
        if self.flat_frames:
            return False
        if self.lamp_frames:
            return False
        return True

    def clear_project(self):

        self.project_name = None
        self.file_path = None
        self.clear_target_frame()
        self.clear_lamp_frame()
        self.clear_flat_frames()
        self.clear_bias_frames()

        return

    def open_project(self, file_path):

        with open(file_path, 'r') as r:
            project_json = json.load(r)

        self.project_name = project_json['ProjectName']
        self.file_path = project_json['ProjectFilePath']
        target_frame = project_json['ProjectFiles']['TargetFrame']
        flat_frames = project_json['ProjectFiles']['FlatFrames']
        bias_frames = project_json['ProjectFiles']['BiasFrames']
        lamp_frames = project_json['ProjectFiles']['LampFrames']

        if target_frame:
            self.load_target_frame(target_frame)
        if flat_frames:
            self.load_flat_frames(flat_frames)
        if bias_frames:
            self.load_bias_frames(bias_frames)
        if lamp_frames:
            self.load_lamp_frames(lamp_frames)

        return

    def save(self):

        project_file = {
            'ProjectName': self.project_name,
            'ProjectFilePath':self.file_path,
            'ProjectFiles':{
                'TargetFrame':(self.target_frame.file_path if self.target_frame else None),
                'FlatFrames':[frame.file_path for frame in self.flat_frames if self.flat_frames],
                'BiasFrames':[frame.file_path for frame in self.bias_frames if self.bias_frames],
                'LampFrames':[frame.file_path for frame in self.lamp_frames if self.lamp_frames]
            }
        }

        project_json = json.dumps(project_file)
        with open(self.file_path, 'w') as w:
            w.write(project_json)

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
