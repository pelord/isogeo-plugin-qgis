# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\credits\ui_credits.ui'
#
# Created: Thu Nov 24 22:50:59 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dlg_credits(object):
    def setupUi(self, dlg_credits):
        dlg_credits.setObjectName(_fromUtf8("dlg_credits"))
        dlg_credits.resize(482, 424)
        dlg_credits.setMinimumSize(QtCore.QSize(482, 300))
        dlg_credits.setMaximumSize(QtCore.QSize(482, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/gavel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlg_credits.setWindowIcon(icon)
        dlg_credits.setWindowOpacity(0.9)
        dlg_credits.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        dlg_credits.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtGui.QWidget(dlg_credits)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 424))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.grp_realization = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.grp_realization.setFlat(True)
        self.grp_realization.setObjectName(_fromUtf8("grp_realization"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.grp_realization)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lbl_development = QtGui.QLabel(self.grp_realization)
        self.lbl_development.setWordWrap(True)
        self.lbl_development.setObjectName(_fromUtf8("lbl_development"))
        self.verticalLayout_7.addWidget(self.lbl_development)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbl_isogeo_logo = QtGui.QLabel(self.grp_realization)
        self.lbl_isogeo_logo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_isogeo_logo.setText(_fromUtf8(""))
        self.lbl_isogeo_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/isogeo.png")))
        self.lbl_isogeo_logo.setScaledContents(False)
        self.lbl_isogeo_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_isogeo_logo.setOpenExternalLinks(True)
        self.lbl_isogeo_logo.setObjectName(_fromUtf8("lbl_isogeo_logo"))
        self.horizontalLayout_4.addWidget(self.lbl_isogeo_logo)
        self.lbl_isogeo_punchline = QtGui.QLabel(self.grp_realization)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_isogeo_punchline.setFont(font)
        self.lbl_isogeo_punchline.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_isogeo_punchline.setOpenExternalLinks(True)
        self.lbl_isogeo_punchline.setObjectName(_fromUtf8("lbl_isogeo_punchline"))
        self.horizontalLayout_4.addWidget(self.lbl_isogeo_punchline)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.grp_realization)
        self.grp_sponsors = QtGui.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.grp_sponsors.setFont(font)
        self.grp_sponsors.setFlat(True)
        self.grp_sponsors.setObjectName(_fromUtf8("grp_sponsors"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.grp_sponsors)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lbl_smavd_url = QtGui.QLabel(self.grp_sponsors)
        self.lbl_smavd_url.setText(_fromUtf8("<html><head/><body><p align=\"center\"><a href=\"http://www.smavd.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Syndicat Mixte d\'Aménagement<br/>de la Durance (SMAVD)</span></a></p></body></html>"))
        self.lbl_smavd_url.setWordWrap(True)
        self.lbl_smavd_url.setOpenExternalLinks(False)
        self.lbl_smavd_url.setObjectName(_fromUtf8("lbl_smavd_url"))
        self.gridLayout_5.addWidget(self.lbl_smavd_url, 0, 0, 1, 1)
        self.lbl_smavd_logo = QtGui.QLabel(self.grp_sponsors)
        self.lbl_smavd_logo.setText(_fromUtf8(""))
        self.lbl_smavd_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/sponsor_logo_SMAVD.jpg")))
        self.lbl_smavd_logo.setScaledContents(False)
        self.lbl_smavd_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_smavd_logo.setOpenExternalLinks(True)
        self.lbl_smavd_logo.setObjectName(_fromUtf8("lbl_smavd_logo"))
        self.gridLayout_5.addWidget(self.lbl_smavd_logo, 0, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.grp_sponsors)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_5.addWidget(self.line_2, 0, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_5)
        self.line = QtGui.QFrame(self.grp_sponsors)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_9.addWidget(self.line)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lbl_lorient_logo = QtGui.QLabel(self.grp_sponsors)
        self.lbl_lorient_logo.setMaximumSize(QtCore.QSize(800, 3000))
        self.lbl_lorient_logo.setText(_fromUtf8(""))
        self.lbl_lorient_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/sponsor_logo_ca_lorient.png")))
        self.lbl_lorient_logo.setScaledContents(False)
        self.lbl_lorient_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lorient_logo.setWordWrap(False)
        self.lbl_lorient_logo.setOpenExternalLinks(True)
        self.lbl_lorient_logo.setObjectName(_fromUtf8("lbl_lorient_logo"))
        self.gridLayout_6.addWidget(self.lbl_lorient_logo, 1, 2, 1, 1)
        self.lbl_lorient_url = QtGui.QLabel(self.grp_sponsors)
        self.lbl_lorient_url.setText(_fromUtf8("<html><head/><body><p align=\"center\"><a href=\"https://www.lorient-agglo.fr/\"><span style=\" text-decoration: underline; color:#0000ff;\">Communauté d\'agglomération de<br/>Lorient (Lorient Agglomération)</span></a></p></body></html>"))
        self.lbl_lorient_url.setObjectName(_fromUtf8("lbl_lorient_url"))
        self.gridLayout_6.addWidget(self.lbl_lorient_url, 1, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.grp_sponsors)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_6.addWidget(self.line_3, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_6)
        self.verticalLayout.addWidget(self.grp_sponsors)
        self.grp_sources = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.grp_sources.setEnabled(True)
        self.grp_sources.setFlat(True)
        self.grp_sources.setCheckable(False)
        self.grp_sources.setObjectName(_fromUtf8("grp_sources"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.grp_sources)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lbl_license_logo_gpl3 = QtGui.QLabel(self.grp_sources)
        self.lbl_license_logo_gpl3.setText(_fromUtf8(""))
        self.lbl_license_logo_gpl3.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Isogeo/resources/gplv3.png")))
        self.lbl_license_logo_gpl3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_license_logo_gpl3.setOpenExternalLinks(True)
        self.lbl_license_logo_gpl3.setObjectName(_fromUtf8("lbl_license_logo_gpl3"))
        self.gridLayout_4.addWidget(self.lbl_license_logo_gpl3, 0, 2, 1, 1)
        self.lbl_source_repository = QtGui.QLabel(self.grp_sources)
        self.lbl_source_repository.setObjectName(_fromUtf8("lbl_source_repository"))
        self.gridLayout_4.addWidget(self.lbl_source_repository, 0, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.grp_sources)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_4.addWidget(self.line_4, 0, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.grp_sources)
        self.btn_ok_close = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.btn_ok_close.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_ok_close.setAutoFillBackground(False)
        self.btn_ok_close.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.btn_ok_close.setOrientation(QtCore.Qt.Horizontal)
        self.btn_ok_close.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.btn_ok_close.setCenterButtons(True)
        self.btn_ok_close.setObjectName(_fromUtf8("btn_ok_close"))
        self.verticalLayout.addWidget(self.btn_ok_close)

        self.retranslateUi(dlg_credits)
        QtCore.QObject.connect(self.btn_ok_close, QtCore.SIGNAL(_fromUtf8("accepted()")), dlg_credits.accept)
        QtCore.QObject.connect(self.btn_ok_close, QtCore.SIGNAL(_fromUtf8("rejected()")), dlg_credits.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_credits)

    def retranslateUi(self, dlg_credits):
        dlg_credits.setWindowTitle(_translate("dlg_credits", "Credits", None))
        self.grp_realization.setTitle(_translate("dlg_credits", "Realization", None))
        self.lbl_development.setText(_translate("dlg_credits", "Developed by Théo Sinatti, internship supervised by Julien Moura for Isogeo.", None))
        self.lbl_isogeo_punchline.setText(_translate("dlg_credits", "<a href=\"http://www.isogeo.com\" style=\"color:#6480A7;text-decoration:none;\">Easy access to geodata!</a>", None))
        self.grp_sponsors.setTitle(_translate("dlg_credits", "Sponsors", None))
        self.grp_sources.setTitle(_translate("dlg_credits", "Sources and license", None))
        self.lbl_source_repository.setText(_translate("dlg_credits", "<html><head/><body><p><a href=\"https://github.com/isogeo/isogeo-plugin-qgis\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/isogeo/isogeo-plugin-qgis</span></a></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg_credits = QtGui.QDialog()
    ui = Ui_dlg_credits()
    ui.setupUi(dlg_credits)
    dlg_credits.show()
    sys.exit(app.exec_())

