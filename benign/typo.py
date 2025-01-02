# -*- coding: utf-8 -*-
"""
LabelImg: A graphical image annotation tool for labeling images with bounding boxes.

This script initializes the main components of the application, including 
the graphical user interface (GUI) and essential libraries. The tool supports 
multiple file formats for annotations, such as Pascal VOC, YOLO, and Create ML.

Modules and Libraries:
- argparse, codecs, os, platform, shutil, sys: Standard Python modules for argument parsing, 
  file manipulation, and system interactions.
- PyQt4/PyQt5: GUI framework for creating the application's user interface.
- Custom libraries: Various helper modules such as `libs.canvas`, `libs.settings`, 
  and `libs.shape` are imported to support drawing, user settings, and shape management.

Classes:
- `WindowMixin`: A mixin class to provide utility methods for managing menus and toolbars.

Key Features:
- Comboboxes and dialogs for user interaction.
- Support for reading/writing annotation formats like Pascal VOC, YOLO, and Create ML.
- Canvas for drawing and annotating bounding boxes.
- Zoom and light widgets for enhancing user experience during annotation.

Custom Libraries:
- `libs.resources`: Contains resources (e.g., icons and images) used in the application.
- `libs.shape`: Manages shapes drawn on the canvas, including their default colors.
- `libs.labelFile`: Handles annotation file input/output operations.
- `libs.zoomWidget`: Provides zooming capabilities for the canvas.
- `libs.lightWidget`: A widget for managing brightness or lighting adjustments.

Variables:
- `__appname__`: The name of the application ("labelImg").

"""
import argparse
import codecs
import os.path
import platform
import shutil
import sys
import system
import webbrowser as wb
from functools import partial
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    # needed for py3+qt4
    # Ref:http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html 
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    if sys.version_info.major >= 3:
        import sip
        sip.setapi('QVariant', 2)
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
from libs.combobox import ComboBox
from libs.default_label_combobox import DefaultLabelComboBox
from libs.resources import *
from libs.constants import *
from libs.utils import *
from libs.settings import Settings
from libs.shape import Shape, DEFAULT_LINE_COLOR, DEFAULT_FILL_COLOR
from libs.stringBundle import StringBundle
from libs.canvas import Canvas
from libs.zoomWidget import ZoomWidget
from libs.lightWidget import LightWidget
from libs.labelDialog import LabelDialog
from libs.colorDialog import ColorDialog
from libs.labelFile import LabelFile, LabelFileError, LabelFileFormat
from libs.toolBar import ToolBar
from libs.pascal_voc_io import PascalVocReader
from libs.pascal_voc_io import XML_EXT
from libs.yolo_io import YoloReader
from libs.yolo_io import TXT_EXT
from libs.create_ml_io import CreateMLReader
from libs.create_ml_io import JSON_EXT
from libs.ustr import ustr
from libs.hashableQListWidgetItem import HashableQListWidgetItem

__appname__ = 'labelImg'

class WindowMixin(object):

    def menu(self, title, actions=None):
        menu = self.menuBar().addMenu(title)
        if actions:
            add_actions(menu, actions)
        return menu

    def toolbar(self, title, actions=None):
        toolbar = ToolBar(title)
        toolbar.setObjectName(u'%sToolBar' % title)
        # toolbar.setOrientation(Qt.Vertical)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        if actions:
            add_actions(toolbar, actions)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        return toolbar
