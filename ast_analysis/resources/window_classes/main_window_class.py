from ast_analysis.resources.forms.py import main_window
from ast_analysis.common.scripts.io import open_fits_file
import numpy as np

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.setup_menu_actions()

        self.fits_files = []

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

    def undo_edit(self):
        # TODO
        return

    def redo_edit(self):
        # TODO
        return

    def revert_changes(self):
        # TODO
        return

    def cut_project_file(self):
        # TODO
        return

    def copy_project_file(self):
        # TODO
        return

    def paste_project_file(self):
        # TODO
        return

    def rename_project_file(self):
        # TODO
        return

    def view_project_panel(self):
        # TODO
        return

    def view_info_panel(self):
        # TODO
        return

    def view_thumbnail(self):
        # TODO
        return

    def view_magnifier(self):
        # TODO
        return

    def view_colorbar(self):
        # TODO
        return

    def view_single_frame(self):
        # TODO
        return

    def view_tiled_frames(self):
        # TODO
        return

    def reset_zoom(self):
        # TODO
        return

    def zoom_in(self):
        # TODO
        return

    def zoom_out(self):
        # TODO
        return

    def zoom_selection(self):
        # TODO
        return

    def set_zoom(self, zoom_level):
        # TODO
        return

    def set_custom_zoom(self):
        # TODO
        return

    def reset_view_rotate(self):
        # TODO
        return

    def view_flip_horizontal(self):
        # TODO
        return

    def view_flip_vertical(self):
        # TODO
        return

    def view_rotate(self, angle):
        # TODO
        return

    def custom_view_rotate(self):
        # TODO
        return

    def center_image_view(self):
        # TODO
        return

    def center_selection_view(self):
        # TODO
        return

    def fullscreen_view(self):
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

    def new_fits_file(self):
        # TODO
        return

    def open_fits_file(self):
        # TODO

        file_path, _ = QFileDialog.getOpenFileName(self, "Open FITS File", filter="*.fits")

        array, headers, msg = open_fits_file(file_path)

        if msg:
            QMessageBox.information(self, "Error Opening FITS file", msg, QMessageBox.Ok)

        image = {'file_path':file_path,'array':array, 'headers':headers}

        self.fits_files.append(image)

        self.display_fits_file(image)

        return

    def display_fits_file(self, file):

        #TODO
        array_converted = np.float16(file['array'])
        q_image=QImage(file['array'], file['array'].shape[0], file['array'].shape[1], QImage.Format_Grayscale16)
        self.img_lbl.setPixmap(QPixmap.fromImage(q_image))

        return

    def save_fits_file(self):
        # TODO
        return

    def save_as_fits_file(self):
        # TODO
        return

    def export_fits(self, filetype):
        # TODO
        return

    def fits_flip_horiz(self):
        # TODO
        return

    def fits_flip_vert(self):
        # TODO
        return

    def fits_rotate(self, angle):
        # TODO
        return

    def fits_crop_to_selection(self):
        # TODO
        return

    def view_fits_headers(self):
        # TODO
        return

    def edit_fits_headers(self):
        # TODO
        return

    def close_fits_file(self):
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

    def getting_started(self):
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

        self.actionUndo_Edit.triggered.connect(self.undo_edit)
        self.actionRedo_Edit.triggered.connect(self.redo_edit)
        self.actionRevert_Changes.triggered.connect(self.revert_changes)
        self.actionEditCut_File.triggered.connect(self.cut_project_file)
        self.actionEditCopy_File.triggered.connect(self.copy_project_file)
        self.actionEditPaste_File.triggered.connect(self.paste_project_file)
        self.actionRename_File.triggered.connect(self.rename_project_file)

        self.actionViewProject_Panel.triggered.connect(self.view_project_panel)
        self.actionViewInfo_Panel.triggered.connect(self.view_info_panel)
        self.actionViewThumbnail.triggered.connect(self.view_thumbnail)
        self.actionViewMagnifier_View.triggered.connect(self.view_magnifier)
        self.actionViewColor_Map.triggered.connect(self.view_colorbar)
        self.actionViewSingleFrames.triggered.connect(self.view_single_frame)
        self.actionViewTiledFrames.triggered.connect(self.view_tiled_frames)

        self.actionResetView_Zoom.triggered.connect(self.reset_zoom)
        self.actionViewZoomIn.triggered.connect(self.zoom_in)
        self.actionViewZoomOut.triggered.connect(self.zoom_out)
        self.actionViewZoomToSelection.triggered.connect(self.zoom_selection)
        self.actionViewZoom1600.triggered.connect(lambda: self.set_zoom(1600))
        self.actionViewZoom800.triggered.connect(lambda: self.set_zoom(800))
        self.actionViewZoom400.triggered.connect(lambda: self.set_zoom(400))
        self.actionViewZoom200.triggered.connect(lambda: self.set_zoom(200))
        self.actionViewZoom100.triggered.connect(lambda: self.set_zoom(100))
        self.actionViewZoom50.triggered.connect(lambda: self.set_zoom(50))
        self.actionViewZoom25.triggered.connect(lambda: self.set_zoom(25))
        self.actionViewZoom12.triggered.connect(lambda: self.set_zoom(12))
        self.actionViewZoom6.triggered.connect(lambda: self.set_zoom(6))
        self.actionViewCustomZoom.triggered.connect(self.set_custom_zoom)

        self.actionResetViewFlipRotate.triggered.connect(self.reset_view_rotate)
        self.actionViewFlip_Horizontal.triggered.connect(self.view_flip_horizontal)
        self.actionViewFlip_Vertical.triggered.connect(self.view_flip_vertical)
        self.actionViewRotate_15_CCW.triggered.connect(lambda: self.view_rotate(-15))
        self.actionViewRotate_15_CW.triggered.connect(lambda: self.view_rotate(15))
        self.actionViewRotate_90_CW.triggered.connect(lambda: self.view_rotate(90))
        self.actionViewRotate_90_CCW.triggered.connect(lambda: self.view_rotate(-90))
        self.actionViewRotate_180.triggered.connect(lambda: self.view_rotate(180))
        self.actionViewOtherRotateAngle.triggered.connect(self.custom_view_rotate)

        self.actionViewCenterImage.triggered.connect(self.center_image_view)
        self.actionViewCenterSelection.triggered.connect(self.center_selection_view)
        self.actionViewFullscreen.triggered.connect(self.fullscreen_view)

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

        self.actionNew_FITS.triggered.connect(self.new_fits_file)
        self.actionFITS_Open.triggered.connect(self.open_fits_file)
        self.actionFITS_Save.triggered.connect(self.save_fits_file)
        self.actionFITS_SaveAs.triggered.connect(self.save_as_fits_file)

        self.actionExportPNG.triggered.connect(lambda: self.export_fits('PNG'))
        self.actionExportJPG.triggered.connect(lambda: self.export_fits('JPG'))
        self.actionExportGIF.triggered.connect(lambda: self.export_fits('GIF'))

        self.actionFITS_FlipHorizontal.triggered.connect(self.fits_flip_horiz)
        self.actionFITS_FlipVertical.triggered.connect(self.fits_flip_vert)
        self.actionFITS_Rotate_90_CW.triggered.connect(lambda: self.fits_rotate(90))
        self.actionFITS_Rotate_90_CCW.triggered.connect(lambda: self.fits_rotate(-90))
        self.actionFITS_Rotate_180.triggered.connect(lambda: self.fits_rotate(180))
        self.actionFITS_Crop_to_Selection.triggered.connect(self.fits_crop_to_selection)
        self.actionHeaders_View.triggered.connect(self.view_fits_headers)
        self.actionHeaders_Edit.triggered.connect(self.edit_fits_headers)
        self.actionFITS_Close.triggered.connect(self.close_fits_file)

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
        self.actionGetting_Started.triggered.connect(self.getting_started)
        self.actionSubmit_Bug_Report_Feedback.triggered.connect(self.submit_bug_report)
        self.actionAbout.triggered.connect(self.about)
