# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ApiWithQtDialog
                                 A QGIS plugin
 test API connexion with Qt in QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-12
        git sha              : $Format:%H$
        copyright            : (C) 2019 by ugluponglu
        email                : test@test.test
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

from PyQt5 import uic
from PyQt5 import QtWidgets

# additional PyQt imports
from qgis.PyQt.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QVBoxLayout
from qgis.PyQt.QtCore import Qt

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'api_with_qt_dialog_base.ui'))


class ApiWithQtDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ApiWithQtDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect

        # additional widgets setting
        self.btn = QPushButton("Launch")
        self.lbl_expected = QLabel()
        self.lbl_expected.setAlignment(Qt.AlignCenter)
        self.lbl_found = QLabel()
        self.lbl_found.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.lbl_expected)
        self.layout.addWidget(self.lbl_found)

        self.setLayout(self.layout)
        
        # original ui setup line
        self.setupUi(self)
        