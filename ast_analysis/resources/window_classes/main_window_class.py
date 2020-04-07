from ast_analysis.resources.forms.py import main_window


from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.setup_menu_actions()

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
        self.actionViewZoom1600.triggered.connect(self.set_zoom(1600))
        self.actionViewZoom800.triggered.connect(self.set_zoom(800))
        self.actionViewZoom400.triggered.connect(self.set_zoom(400))
        self.actionViewZoom200.triggered.connect(self.set_zoom(200))
        self.actionViewZoom100.triggered.connect(self.set_zoom(100))
        self.actionViewZoom50.triggered.connect(self.set_zoom(50))
        self.actionViewZoom25.triggered.connect(self.set_zoom(25))
        self.actionViewZoom12.triggered.connect(self.set_zoom(12))
        self.actionViewZoom6.triggered.connect(self.set_zoom(6))
        self.actionViewCustomZoom.triggered.connect(self.set_custom_zoom)

        # TODO: Finish remaining menu actions