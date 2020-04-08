from ast_analysis.resources.forms.py import main_window
from ast_analysis.common.classes import Project

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from pyqtgraph import ImageItem


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.setup_menu_actions()

        self.project = Project()
        self.target_frame_lw.itemDoubleClicked.connect(self.display_target_frame)

    def display_target_frame(self, item):
        #TODO Error when handling file with more than one frame
        frame_title = item.text()
        self.frame_display.setImage(self.project.target_frame.frames)

    def update_frame_list_views(self):

        self.target_frame_lw.clear()
        self.bias_frame_lw.clear()
        self.flat_frame_lw.clear()
        self.specref_lw.clear()

        if self.project.target_frame:
            self.target_frame_lw.addItem(self.project.target_frame.file_name)
        if self.project.bias_frames:
            self.bias_frame_lw.addItems([bias_frame.file_name for bias_frame in self.project.bias_frames])
        if self.project.flat_frames:
            self.flat_frame_lw.addItems([flat_frame.file_name for flat_frame in self.project.flat_frames])
        if self.project.lamp_frames:
            self.specref_lw.addItems([lamp_frame.file_name for lamp_frame in self.project.lamp_frames])

        return

    def create_new_project(self):

        if not self.project.is_empty():
            warn_msg = QMessageBox.warning(self, "Save Current Project","Would you like to save your current project?",QMessageBox.Yes|QMessageBox.No)
            if warn_msg == QMessageBox.Ok:
                if self.project.file_path:
                    self.save_project()
                if not self.project.file_path:
                    self.save_project_as()

        self.project.clear_project()
        self.update_frame_list_views()

        return

    def open_project(self):

        if not self.project.is_empty():
            warn_msg = QMessageBox.warning(self, "Save Current Project","Would you like to save your current project?",QMessageBox.Yes|QMessageBox.No)
            if warn_msg == QMessageBox.Ok:
                if self.project.file_path:
                    self.save_project()
                if not self.project.file_path:
                    self.save_project_as()

        file_path, _ = QFileDialog.getOpenFileName(self, "Open Project", filter="*ast-proj")

        if not file_path:
            return

        self.project.open_project(file_path)
        self.update_frame_list_views()

        return

    def save_project(self):

        if not self.project.file_path:
            self.save_project_as()
        else:
            self.project.save()

        return

    def save_project_as(self):

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Project As")

        if not file_path:
            return

        file_path += ".ast-proj"

        self.project.file_path = file_path

        self.project.save()

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

    def open_target_frame(self):
        if self.project.target_frame:
            overide_msg = QMessageBox.question(self, "Replace existing frame?", "Loading a new target frame will replace the current frame.", QMessageBox.Ok|QMessageBox.Cancel)
            if overide_msg == QMessageBox.Cancel:
                return
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Target Frame", filter="*.fits")
        if file_name:
            self.project.load_target_frame(file_name)
        self.update_frame_list_views()
        self.proj_files_tb.setCurrentIndex(0)
        return

    def clear_target_frame(self):

        if not self.project.target_frame:
            QMessageBox.information(self, "No Target Frame", "No target frame is currently loaded.", QMessageBox.Ok)
            return

        warn_msg = QMessageBox.question(self, "Clear Targeet Frame", "Are you sure you want to clear the target frame?", QMessageBox.Ok|QMessageBox.Cancel)

        if warn_msg == QMessageBox.Ok:
            self.project.clear_target_frame()
            self.update_frame_list_views()
            self.proj_files_tb.setCurrentIndex(0)
        return

    def add_bias_frames(self):
        file_names, _ = QFileDialog.getOpenFileNames(self, "Add Bias Frames", filter="*.fits")

        if not file_names:
            return

        self.project.load_bias_frames(file_names)
        self.update_frame_list_views()
        self.proj_files_tb.setCurrentIndex(2)
        return

    def delete_bias_frames(self):
        #TODO
        return

    def clear_bias_frames(self):
        if not self.project.bias_frames:
            QMessageBox.information(self, "No Bias Frames Loaded","No bias frames are currently loaded.", QMessageBox.Ok)
            return

        warn_msg = QMessageBox.warning(self, "Clear Bias Frames","Are you sure you want to clear all bias frames?", QMessageBox.Yes|QMessageBox.No)
        if warn_msg == QMessageBox.Yes:
            self.project.clear_bias_frames()
            self.update_frame_list_views()
            self.proj_files_tb.setCurrentIndex(2)

        return

    def add_flat_frames(self):
        file_names, _ = QFileDialog.getOpenFileNames(self, "Add Flat Frames", filter="*.fits")

        if not file_names:
            return

        self.project.load_flat_frames(file_names)
        self.update_frame_list_views()
        self.proj_files_tb.setCurrentIndex(1)
        return

    def clear_flat_frames(self):
        if not self.project.flat_frames:
            QMessageBox.information(self, "No Flat Frames Loaded","No flat frames are currently loaded.", QMessageBox.Ok)
            return

        warn_msg = QMessageBox.warning(self, "Clear Flat Frames","Are you sure you want to clear all flat frames?", QMessageBox.Yes|QMessageBox.No)
        if warn_msg == QMessageBox.Yes:
            self.project.clear_flat_frames()
            self.update_frame_list_views()
            self.proj_files_tb.setCurrentIndex(1)

        return

    def delete_flat_frames(self):
        #TODO
        return

    def open_lamp_frame(self):
        file_names, _ = QFileDialog.getOpenFileNames(self, "Add Lamp Frames", filter="*.fits")

        if not file_names:
            return

        self.project.load_lamp_frames(file_names)
        self.update_frame_list_views()
        self.proj_files_tb.setCurrentIndex(3)
        return
    
    def clear_lamp_frame(self):
        if not self.project.lamp_frames:
            QMessageBox.information(self, "No Lamp Frames Loaded","No lamp frames are currently loaded.", QMessageBox.Ok)
            return

        warn_msg = QMessageBox.warning(self, "Clear Lamp Frames","Are you sure you want to clear all lamp frames?", QMessageBox.Yes|QMessageBox.No)
        if warn_msg == QMessageBox.Yes:
            self.project.clear_lamp_frame()
            self.update_frame_list_views()
            self.proj_files_tb.setCurrentIndex(3)

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
