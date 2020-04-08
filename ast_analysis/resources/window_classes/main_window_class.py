from ast_analysis.resources.forms.py import main_window
from ast_analysis.common.classes import Project

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.setup_menu_actions()

        self.project = Project()

    def create_new_project(self):
        # TODO
        return

    def open_project(self):
        # TODO
        return

    def save_project(self):
        # TODO
        return

    def save_project_as(self):
        # TODO
        return

    def close_project(self):
        # TODO
        return

    def open_settings(self):
        # TODO
        return

    def import_settings(self):
        # TODO
        return

    def export_settings(self):
        # TODO
        return

    def exit_app(self):
        # TODO
        return

    def set_colorspace(self, colorspace):
        # TODO
        return

    def edit_colorsapce(self):
        # TODO
        return

    def save_colorspace(self):
        # TODO
        return

    def load_colorspace(self):
        # TODO
        return

    def set_mag_scale(self, scale):
        # TODO
        return

    def open_target_fram(self):
        #TODO
        return

    def clear_target_frame(self):
        #TODO
        return

    def add_bias_frames(self):
        #TODO
        return

    def delete_bias_frames(self):
        #TODO
        return

    def clear_bias_frames(self):
        #TODO
        return

    def add_flat_frames(self):
        #TODO
        return

    def clear_flat_frames(self):
        #TODO
        return

    def delete_flat_frames(self):
        #TODO
        return

    def open_lamp_frame(self):
        #TODO
        return
    
    def clear_lamp_frame(self):
        #TODO
        return

    def display_fits_file(self, file):

        #TODO
        # array_converted = np.float16(file['array'])
        # q_image=QImage(file['array'], file['array'].shape[0], file['array'].shape[1], QImage.Format_Grayscale16)
        # self.img_lbl.setPixmap(QPixmap.fromImage(q_image))

        return

    def export_fits(self, filetype):
        # TODO
        return

    def med_comb(self):
        # TODO
        return

    def norm_med_comb(self):
        # TODO
        return

    def manual_background_removal(self):
        # TODO
        return

    def bad_pixel_manual(self):
        # TODO
        return

    def bad_pixel_threshold(self):
        # TODO
        return

    def bad_pixel_outlier(self):
        # TODO
        return

    def add_ignore_region(self):
        # TODO
        return

    def delete_ignore_region(self):
        # TODO
        return

    def add_roi(self):
        # TODO
        return

    def delete_roi(self):
        # TODO
        return

    def scale_tile_stripe(self):
        # TODO
        return

    def scale_spline_terp(self):
        # TODO
        return

    def match_spectrum_auto(self):
        # TODO
        return

    def match_spectrum_manual(self):
        # TODO
        return

    def mean_horizontal(self):
        # TODO
        return

    def mean_vertical(self):
        # TODO
        return

    def mean_custom(self):
        # TODO
        return

    def median_horizontal(self):
        # TODO
        return

    def median_vertical(self):
        # TODO
        return

    def median_custom(self):
        # TODO
        return

    def view_measurements(self):
        # TODO
        return

    def get_help(self):
        # TODO
        return

    def submit_bug_report(self):
        # TODO
        return

    def about(self):
        # TODO
        return

    def setup_menu_actions(self):
        self.actionNew_Project.triggered.connect(self.create_new_project)
        self.actionOpen_Project.triggered.connect(self.open_project)
        self.actionSave_Project.triggered.connect(self.save_project)
        self.actionSave_Project_As.triggered.connect(self.save_project_as)
        self.actionClose_Project.triggered.connect(self.close_project)
        self.actionOpen_Settings.triggered.connect(self.open_settings)
        self.actionImport_Settings.triggered.connect(self.import_settings)
        self.actionExport_Settings.triggered.connect(self.export_settings)
        self.actionExit_Program.triggered.connect(self.exit_app)

        self.actionSetColorGreyscale.triggered.connect(lambda: self.set_colorspace('greyscale'))
        self.actionSetColorBlack_Body.triggered.connect(lambda: self.set_colorspace('blackbody'))
        self.actionSetColorHeatmap.triggered.connect(lambda: self.set_colorspace('heatmap'))
        self.actionSetColorCool.triggered.connect(lambda: self.set_colorspace('cool'))
        self.actionSetColorRainbow.triggered.connect(lambda: self.set_colorspace('rainbow'))

        self.actionColorspaceEdit.triggered.connect(self.edit_colorsapce)
        self.actionColorspaceSave.triggered.connect(self.save_colorspace)
        self.actionColorspaceLoad.triggered.connect(self.load_colorspace)

        self.actionViewScaleLinear.triggered.connect(lambda: self.set_mag_scale('lin'))
        self.actionViewScaleLogarithmic.triggered.connect(lambda: self.set_mag_scale('log'))
        self.actionViewScalePower.triggered.connect(lambda: self.set_mag_scale('pow'))
        self.actionViewScaleSquare_Root.triggered.connect(lambda: self.set_mag_scale('sqrt'))
        self.actionViewScaleSquared.triggered.connect(lambda: self.set_mag_scale('sqr'))
        self.actionViewScaleasinh.triggered.connect(lambda: self.set_mag_scale('asinh'))
        self.actionViewScalesinh.triggered.connect(lambda: self.set_mag_scale('sinh'))
        self.actionViewScaleHistogram.triggered.connect(lambda: self.set_mag_scale('hist'))
        self.actionViewScaleMin_Max.triggered.connect(lambda: self.set_mag_scale('min_max'))
        self.actionViewScaleZ_Scale.triggered.connect(lambda: self.set_mag_scale('z'))

        self.actionOpenTargetFrame.triggered.connect(self.open_target_frame)
        self.actionClearTargetFrame.triggered.connect(self.clear_target_frame)
        self.actionAddBiasFrame.triggered.connect(self.add_bias_frames)
        self.actionDeleteBiasFrame.triggered.connect(self.delete_bias_frames)
        self.actionClearBiasFrames.triggered.connect(self.clear_bias_frames)
        self.actionAddFlatFrame.triggered.connect(self.add_flat_frames)
        self.actionClearFlatFrame.triggered.connect(self.clear_flat_frames)
        self.actionDeleteFlatFrame.triggered.connect(self.delete_flat_frames)
        self.actionOpenLampFrame.triggered.connect(self.open_lamp_frame)
        self.actionClearLampFrame.triggered.connect(self.clear_lamp_frame)

        self.actionNR_MedComb.triggered.connect(self.med_comb)
        self.actionNR_NormMedComb.triggered.connect(self.norm_med_comb)
        self.actionNR_ManBackground.triggered.connect(self.manual_background_removal)

        self.actionBP_Manual_Removal.triggered.connect(self.bad_pixel_manual)
        self.actionBP_Threshold_Removal.triggered.connect(self.bad_pixel_threshold)
        self.actionBP_Outlier_Removal.triggered.connect(self.bad_pixel_outlier)

        self.actionAddIgnoreRegion.triggered.connect(self.add_ignore_region)
        self.actionDeleteIgnoreRegion.triggered.connect(self.delete_ignore_region)

        self.actionAddInterestRegion.triggered.connect(self.add_roi)
        self.actionDeleteInterestRegion.triggered.connect(self.delete_roi)

        self.actionScale_TileStripe.triggered.connect(self.scale_tile_stripe)
        self.actionScale_SplineTerp.triggered.connect(self.scale_spline_terp)

        self.actionSpectrum_Automatic.triggered.connect(self.match_spectrum_auto)
        self.actionSpectrum_Manual.triggered.connect(self.match_spectrum_manual)

        self.actionMean_Horizontal.triggered.connect(self.mean_horizontal)
        self.actionMean_Vertical.triggered.connect(self.mean_vertical)
        self.actionMean_Custom.triggered.connect(self.mean_custom)
        self.actionMedian_Horizontal.triggered.connect(self.median_horizontal)
        self.actionMedian_Vertical.triggered.connect(self.median_vertical)
        self.actionMedian_Custom.triggered.connect(self.median_custom)

        self.actionViewMeasurements.triggered.connect(self.view_measurements)

        self.actionHelp.triggered.connect(self.get_help)
        self.actionSubmit_Bug_Report_Feedback.triggered.connect(self.submit_bug_report)
        self.actionAbout.triggered.connect(self.about)
