# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IsogeoDockWidget
                                 A QGIS plugin
 Recherchez des données via un ou plusieurs catalogues Isogeo
                             -------------------
        begin                : 2015-12-22
        git sha              : $Format:%H$
        copyright            : (C) 2015 by GeoJulien/Isogeo
        email                : projets@isogeo.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import QtGui, uic
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import pyqtSignal

# # changed because of an issue generated by Qt Designer
# # see: http://gis.stackexchange.com/a/155599/19817
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "ui_credits.ui"))

# from ui_credits import Ui_dlg_credits


# # changed besause of an issue generated by Qt Designer
# # see: http://gis.stackexchange.com/a/155599/19817
# class IsogeoCredits(QDialog, FORM_CLASS):


class IsogeoCredits(QDialog, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(IsogeoCredits, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
