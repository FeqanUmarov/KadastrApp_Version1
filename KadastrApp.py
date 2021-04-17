from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import xlrd
import sqlite3

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(568, 570)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(115, 10, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(410, 10, 121, 23))
        self.pushButton.setToolTip("Excel fayılı daxil et")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 60, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self)
        self.comboBox_4.setGeometry(QtCore.QRect(460, 60, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 101, 61))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 40, 101, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 40, 101, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 20, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.comboBox_5 = QtWidgets.QComboBox(self)
        self.comboBox_5.setGeometry(QtCore.QRect(410, 140, 156, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")

        self.comboBox_6 = QtWidgets.QComboBox(self)
        self.comboBox_6.setGeometry(QtCore.QRect(410, 200, 156, 22))
        self.comboBox_6.setObjectName("comboBox_6")

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 240, 156, 25))
        self.pushButton_4.setToolTip("Torpaq tipinə daxil olan yarımtipləri yeniləyir")
        self.pushButton_4.setObjectName("pushButton")

        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 270, 156, 25))
        self.pushButton_5.setToolTip("Yarımtiplləri sıfırlayır")
        self.pushButton_5.setObjectName("pushButton")
        

        
        self.groupBox_4 = QtWidgets.QGroupBox(self)
        self.groupBox_4.setGeometry(QtCore.QRect(450, 40, 110, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 26, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(180, 110, 26, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(340, 110, 36, 16))
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(440, 110, 80, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(435, 180, 120, 16))
        self.label_7.setObjectName("label_7")



        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 150, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 150, 71, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 130, 391, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 210, 391, 80))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(320, 230, 71, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 230, 71, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.groupBox_7 = QtWidgets.QGroupBox(self)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 290, 391, 80))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self)
        self.lineEdit_9.setGeometry(QtCore.QRect(320, 310, 71, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 310, 71, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.groupBox_8 = QtWidgets.QGroupBox(self)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 370, 391, 80))
        self.groupBox_8.setObjectName("groupBox_8")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self)
        self.lineEdit_12.setGeometry(QtCore.QRect(320, 390, 71, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self)
        self.lineEdit_13.setGeometry(QtCore.QRect(160, 390, 71, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.groupBox_9 = QtWidgets.QGroupBox(self)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 450, 391, 80))
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_14.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self)
        self.lineEdit_15.setGeometry(QtCore.QRect(320, 470, 71, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self)
        self.lineEdit_16.setGeometry(QtCore.QRect(160, 470, 71, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(234, 540, 170, 23))
        self.pushButton_2.setToolTip("Excel məlumatlarına əsasən torpaq qatlarını standarta gətir")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 540, 141, 23))
        self.pushButton_3.setToolTip("Hesablanmış torpaq məlumatlaırını sql bazasına göndər")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(423, 360, 131, 200))
        self.textBrowser.setObjectName("textBrowser")
        
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(450, 340, 71, 16))
        self.label_5.setObjectName("label_5")


        self.groupBox_5.raise_()
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.groupBox_6.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.groupBox_7.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.groupBox_8.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_13.raise_()
        self.groupBox_9.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_16.raise_()
        #self.lineEdit_20.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        #self.comboBox_5.setCurrentIndex(0)




    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Excel faylinin yolu"))
        self.pushButton.setText(_translate("Dialog", "Excel fayli daxil et"))
        self.pushButton.clicked.connect(self.ExcelFile)
        
        self.comboBox.setItemText(0, _translate("Dialog", "Var"))
        self.comboBox.setItemText(1, _translate("Dialog", "Yox"))
        
        
        self.comboBox_2.setItemText(0, _translate("Dialog", "Var"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Yox"))

        
        self.comboBox_4.setItemText(0, _translate("Dialog", "Var"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Yox"))
        self.groupBox.setTitle(_translate("Dialog", "Azot"))
        self.groupBox_2.setTitle(_translate("Dialog", "Fosfor"))
        self.groupBox_3.setTitle(_translate("Dialog", "Kalium"))
        
        self.comboBox_3.setItemText(0, _translate("Dialog", "Var"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Yox"))

        self.comboBox_5.setItemText(0, _translate("Dialog", "Dağ-çəmən"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Qonur dağ-meşə"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Qəhvəyi dağ-meşə"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "Bozqırlaşmış dağ-qəhvəyi"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "Dağ boz-qəhvəyi"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "Dağ qaratorpaq"))
        self.comboBox_5.setItemText(6, _translate("Dialog", "Dağ şabalıdı"))
        self.comboBox_5.setItemText(7, _translate("Dialog", "Sarı"))
        self.comboBox_5.setItemText(8, _translate("Dialog", "Çəmən-qəhvəyi"))
        self.comboBox_5.setItemText(9, _translate("Dialog", "Şabalıdı"))
        self.comboBox_5.setItemText(10, _translate("Dialog", "Çəmən-şabalıdı"))
        self.comboBox_5.setItemText(11, _translate("Dialog", "Boz-qonur"))
        self.comboBox_5.setItemText(12, _translate("Dialog", "Boz"))
        self.comboBox_5.setItemText(13, _translate("Dialog", "Çəmənləşmiş-boz"))
        self.comboBox_5.setItemText(14, _translate("Dialog", "Çəmən-boz"))
        self.comboBox_5.setItemText(15, _translate("Dialog", "Çəmən-meşə"))
        self.comboBox_5.setItemText(16, _translate("Dialog", "Allüvial-çəmən"))
        self.comboBox_5.setItemText(17, _translate("Dialog", "Çəmən-bataqlı"))
        self.comboBox_5.setItemText(18, _translate("Dialog", "Şoranlar"))
        
        self.groupBox_4.setTitle(_translate("Dialog", "Udulmuş əsaslar"))
        self.label_2.setText(_translate("Dialog", "0-20"))
        self.label_3.setText(_translate("Dialog", "0-50"))
        self.label_4.setText(_translate("Dialog", "0-100"))
        self.groupBox_5.setTitle(_translate("Dialog", "Humus"))
        self.groupBox_6.setTitle(_translate("Dialog", "Azot"))
        self.groupBox_7.setTitle(_translate("Dialog", "Fosfor"))
        self.groupBox_8.setTitle(_translate("Dialog", "Kalium"))
        self.groupBox_9.setTitle(_translate("Dialog", "Udulmuş əsaslar"))
        self.pushButton_2.setText(_translate("Dialog", "Qat məlumatlarını hesabla"))
        self.pushButton_2.clicked.connect(self.Isle)

        self.pushButton_3.setText(_translate("Dialog", "Melumatlari SQl gonder"))
        self.pushButton_3.clicked.connect(self.Send)
        
        self.label_5.setText(_translate("Dialog", "Bildiriş paneli"))
        self.label_6.setText(_translate("Dialog","Torpaq Tipləri"))
        self.label_7.setText(_translate("Dialog", "Torpaq Yarımtipləri"))

        self.pushButton_4.setText(_translate ("Dialog", "Yarımtipləri Yenilə"))
        self.pushButton_4.clicked.connect(self.Refresh)

        self.pushButton_5.setText(_translate("Dialog", "Yarımtipləri Sifirla"))
        self.pushButton_5.clicked.connect(self.Clear)

    def ExcelFile(self):
        filename = QFileDialog.getOpenFileName()
        filename = filename[0]
        filename = str(filename)
        self.lineEdit.setText(filename)


    def Refresh(self, Dialog):
        _translatee = QtCore.QCoreApplication.translate

        if self.comboBox_5.currentText() == "Dağ-çəmən":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Çimli-torflu dağ-çəmən")
            self.comboBox_6.addItem("Çimli dağ-çəmən")
            self.comboBox_6.addItem("Qaramtıl dağ-çəmən")
            self.comboBox_6.addItem("Bozqır dağ-çəmən")

        if self.comboBox_5.currentText() == "Qonur dağ-meşə":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Tipik qonur dağ-meşə")
            self.comboBox_6.addItem("Zəif doymuş (lösləşmiş) qonur dağ-meşə")
            self.comboBox_6.addItem("Karbonat qalıqlı qonur dağ-meşə")
            self.comboBox_6.addItem("Bozqırlaşmış qonur dağ-meşə")
            self.comboBox_6.addItem("Podzollaşmış qonur dağ-meşə")

        if self.comboBox_5.currentText() == "Qəhvəyi dağ-meşə":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yuyulmuş qəhvəyi dağ meşə")
            self.comboBox_6.addItem("Tipik qəhvəyi dağ meşə")
            self.comboBox_6.addItem("Karbonatlı qəhvəyi dağ meşə")

        if self.comboBox_5.currentText() == "Bozqırlaşmış dağ-qəhvəyi":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Dağ boz-qəhvəyi":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Dağ qaratorpaq":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yuyulmuş dağ qara")
            self.comboBox_6.addItem("Adi dağ qara")
            self.comboBox_6.addItem("Karbonatlı dağ qara")
            self.comboBox_6.addItem("Bərkimiş dağ qara")

        if self.comboBox_5.currentText() == "Dağ şabalıdı":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Sarı":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Sarı dağ-meşə")
            self.comboBox_6.addItem("Podzollu-sarı")
            self.comboBox_6.addItem("Podzollu-qleyli-sarı")
            self.comboBox_6.addItem("Sarı-qleyli ")

        if self.comboBox_5.currentText() == "Çəmən-qəhvəyi":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Səthdən çəmənləşmiş şabalıdı")
            self.comboBox_6.addItem("Çəmən-qəhvəyi")

        if self.comboBox_5.currentText() == "Şabalıdı":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Tünd şabalıdı")
            self.comboBox_6.addItem("Adi şabalıdı")
            self.comboBox_6.addItem("Açıq şabalıdı")
            self.comboBox_6.addItem("'gəcli' şabalıdı")

        if self.comboBox_5.currentText() == "Çəmən-şabalıdı":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Səthdən çəmənləşmiş şabalıdı")
            self.comboBox_6.addItem("Çəmənləşmiş şabalıdı")
            self.comboBox_6.addItem("Çəmən şabalıdı")

        if self.comboBox_5.currentText() == "Boz-qonur":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Boz":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Açıq-boz")
            self.comboBox_6.addItem("Adi-boz")
            self.comboBox_6.addItem("Qədimdən suvarılan boz")
            self.comboBox_6.addItem("İbtidai boz")

        if self.comboBox_5.currentText() == "Çəmənləşmiş-boz":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Çəmən-boz":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Çəmən-meşə":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Allüvial-çəmən":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

        if self.comboBox_5.currentText() == "Çəmən-bataqlı":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Çürüntülü çəmən-bataqlıq")
            self.comboBox_6.addItem("Lilli çəmənbataqlıq")

        if self.comboBox_5.currentText() == "Şoranlar":
            self.comboBox_6.clear()
            self.comboBox_6.addItem("Yarımtipi yoxdur")

    def Clear(self):
        self.comboBox_6.clear()




    def Isle(self):
        connect = self.lineEdit.text()
        try:
            loc = (str(connect))
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0,0)

    ################### Butun şert bloklarinda movcud olan melumatlar ##################################
            w1 = []
            w2 = []
            w3_humus = []
            w3_Azot = []
            w3_Fosfor = []
            w3_Kalium = []
    ################### Butun şert bloklarinda movcud olan melumatlar ##################################
            w3_humus_index = []
            w3_azot_index = []
            w3_fosfor_index = []
            w3_kalium_index = []
            #################################################
            w3_humus_index_end = []
            ##########################################
            w20_2 = []
            w20_humus = []
            w20_azot = []
            w20_fosfor = []
            w20_kalium = []
            w20_humus_process_end = []
            w20_azot_process_end = []
            w20_fosfor_process_end = []
            w20_kalium_process_end = []
            w20_2_max = []
            w20_2_index = []
            w20_2_index_azot = []
            w20_2_index_fosfor = []
            w20_2_index_kalium = []
            w20_1 = []
            Total_20_sum = []
            Total_20_sum_azot = []
            Total_20_sum_fosfor = []
            Total_20_sum_kalium = []
            ##########################################
            index_w20 = []
            ##########################################
            W50_remain = []
            w50_2 = []
            w50_humus = []
            w50_azot = []
            w50_fosfor = []
            w50_kalium = []
            w50_humus_process_end = []
            w50_azot_process_end = []
            w50_fosfor_process_end = []
            w50_kalium_process_end = []
            w50_2_max = []
            w50_2_index = []
            w50_1 = []
            Total_50_sum = []
            Total_50_sum_azot = []
            Total_50_sum_fosfor = []
            Total_50_sum_kalium = []
            ##########################################
            index_w50 = []
            ##########################################
            W100_remain = []
            w100_humus_end = []
            w100_2 = []
            w100_humus = []
            w100_azot = []
            w100_fosfor = []
            w100_kalium = []
            w100_humus_process_end = []
            w100_2_max = []
            w100_2_index = []
            w100_1 = []
            Total_100_sum = []
            ##########################################
            index_w100 = []
            ##########################################


            ##########################################
            for i in range(sheet.nrows):
                p = sheet.cell_value(i, 0)
                w1.append(p)
            w1.remove("Qat_araligi1")

        
            for i in range(sheet.nrows):
                p = sheet.cell_value(i, 1)
                w2.append(p)
            w2.remove("Qat_araligi2")
            try:
                for i in range(sheet.nrows):
                    p = sheet.cell_value(i, 2)
                    w3_humus.append(p)
                w3_humus.remove("Humus")
            except:
                self.textBrowser.setText("Humus melumatı düzgün sütunda yazılmayıb!")
                print("Humus melumatlari daxil edilmeyib!!!")

            try:
                for i in range(sheet.nrows):
                    p = sheet.cell_value(i, 3)
                    w3_Azot.append(p)
                w3_Azot.remove("Azot")
            except:
                self.textBrowser.setText("Azot melumatı düzgün sütunda yazılmayıb!")
                print("Azot melumatlari daxil edilmeyib!!!")

            try:
                for i in range(sheet.nrows):
                    p = sheet.cell_value(i, 4)
                    w3_Fosfor.append(p)
                w3_Fosfor.remove("Fosfor")
            except:
                self.textBrowser.setText("Fosfor melumatı düzgün sütunda yazılmayıb!")
                print("Fosfor melumatlari daxil edilmeyib!!!")

            try:
                for i in range(sheet.nrows):
                    p = sheet.cell_value(i, 5)
                    w3_Kalium.append(p)
                w3_Kalium.remove("Kalium")
            except:
                self.QTextBrowser.setText("Kalium melumatı düzgün sütunda yazılmayıb!")
                print("Kalium melumatlari daxil edilmeyib!!!")



            if min(w2)<=20 and max(w2)>100:
                for s in w2:
                    try:
                        s = int(s)
                        if s <= 20:
                            q=w2.index(s)
                            index_w20.append(q)
                            w20_2.append(s)
                        if 20 < s <= 50:
                            q=w2.index(s)
                            index_w50.append(q)
                            w50_2.append(s)
                        if 50 < s <= 100:
                            q = w2.index(s)
                            index_w100.append(q)
                            w100_2.append(s)
                    except ValueError:
                        print("Excel melumatlarinda her hansi sutunda reqem melumatindan kenar verilen var!!!")



    ####################################################
            
                for s in index_w20:
                    q = w1[s]
                    q = int(q)
                    w20_1.append(q)

                for s in index_w20:
                    q = w3_humus[s]
                    w20_humus.append(q)

                for s in index_w20:
                    q = w3_Azot[s]
                    w20_azot.append(q)

                for s in index_w20:
                    q = w3_Fosfor[s]
                    w20_fosfor.append(q)

                for s in index_w20:
                    q = w3_Kalium[s]
                    w20_kalium.append(q)

        
    ####################################################
    ####################################################
        
                for s in index_w50:
                    q = w1[s]
                    q = int(q)
                    w50_1.append(q)

                for s in index_w50:
                    q = w3_humus[s]
                    w50_humus.append(q)

                for s in index_w50:
                    q = w3_Azot[s]
                    w50_azot.append(q)

                for s in index_w50:
                    q = w3_Fosfor[s]
                    w50_fosfor.append(q)

                for s in index_w50:
                    q = w3_Kalium[s]
                    w50_kalium.append(q)



    ####################################################
    ####################################################
        
                for s in index_w100:
                    q = w1[s]
                    q = int(q)
                    w100_1.append(q)

                for s in index_w100:
                    q = w3_humus[s]
                    w100_humus.append(q)

                for s in index_w100:
                    q = w3_Azot[s]
                    w100_azot.append(q)

                for s in index_w100:
                    q = w3_Fosfor[s]
                    w100_fosfor.append(q)

                for s in index_w100:
                    q = w3_Kalium[s]
                    w100_kalium.append(q)


    ####################################################
    ####################################################

    ####################################################

                for s in w20_2:
                    k = w20_2.index(s)
                    w20_2_index.append(k)

                for s in w50_2:
                    k = w50_2.index(s)
                    w50_2_index.append(k)


                for s in w100_2:
                    k = w100_2.index(s)
                    w100_2_index.append(k)


    ####################################################
                for s in w3_humus:
                    k = w3_humus.index(s)
                    w3_humus_index.append(k)
                    w3_humus_index_max = max(w3_humus_index)
                    w3_humus_index.clear()
                    w3_humus_index.append(w3_humus_index_max)
                q = w3_humus[w3_humus_index[0]]
                w100_humus_end.append(q)

    ####################################################
    ####################################################
        
                for s in w20_2_index:
                    q =  (w20_2[s] - w20_1[s])*w20_humus[s]
                    q = round(q,2)
                    w20_humus_process_end.append(q)
                q = 20-max(w20_2)
                W50_remain.append(q)
                k = q*w50_humus[0]
                k = round(k,2)
                w20_humus_process_end.append(k)
                total_20 = sum(w20_humus_process_end)
                Total_20_sum.append(total_20)    
                process_end_humus_20 = total_20/20
                process_end_humus_20 = round(process_end_humus_20,2)
                w20_humus_process_end.clear()
                w20_humus_process_end.append(process_end_humus_20)
                self.lineEdit_2.setText(str(w20_humus_process_end[0]))
                print("0-20 qati:",w20_humus_process_end)

        ####################### HUMUS ######################################################

                    

                    
                
    ####################################################
    ####################################################
                try:
                    r = w50_1[0]+W50_remain[0]
                    w50_1.remove(w50_1[0])
                    w50_1.insert(0,r)
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_humus[s]
                        q = round(q,2)
                        w50_humus_process_end.append(q)
                    q = 50-max(w50_2)
                    W100_remain.append(q)
                    k = q*w100_humus[0]
                    k = round(k,2)
                    w50_humus_process_end.append(k)
                    total_50 = sum(w50_humus_process_end)
                    Total_50_sum.append(total_50)
                    Total_50_sum.extend(Total_20_sum)
                    process_end_humus_50_tam = sum(Total_50_sum)
                    process_end_humus_50_tam = round(process_end_humus_50_tam,2)
                    process_end_humus_50_tam_proccesEnd = process_end_humus_50_tam/50
                    process_end_humus_50_tam_proccesEnd = round(process_end_humus_50_tam_proccesEnd,2)
                    w50_humus_process_end.clear()
                    w50_humus_process_end.append(process_end_humus_50_tam_proccesEnd)
                    self.lineEdit_3.setText(str(w50_humus_process_end[0]))
                    print("0-50 qati:",w50_humus_process_end)

                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")

                if self.comboBox.currentText() == "Var":
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_azot[s]
                        q = round(q,2)
                        w20_azot_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_azot[0]
                    k = round(k,2)
                    w20_azot_process_end.append(k)
                    total_20 = sum(w20_azot_process_end)
                    Total_20_sum_azot.append(total_20)    
                    process_end_azot_20 = total_20/20
                    process_end_azot_20 = round(process_end_azot_20,2)
                    w20_azot_process_end.clear()
                    w20_azot_process_end.append(process_end_azot_20)
                    self.lineEdit_5.setText(str(w20_azot_process_end[0]))
                    print("0-20 qati:",w20_azot_process_end)


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_azot[s]
                        q = round(q,2)
                        w50_azot_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_azot[0]
                    k = round(k,2)
                    w50_azot_process_end.append(k)
                    total_50 = sum(w50_azot_process_end)
                    Total_50_sum_azot.append(total_50)
                    Total_50_sum_azot.extend(Total_20_sum_azot)
                    process_end_azot_50_tam = sum(Total_50_sum_azot)
                    process_end_azot_50_tam = round(process_end_azot_50_tam,2)
                    process_end_azot_50_tam_proccesEnd = process_end_azot_50_tam/50
                    process_end_azot_50_tam_proccesEnd = round(process_end_azot_50_tam_proccesEnd,2)
                    w50_azot_process_end.clear()
                    w50_azot_process_end.append(process_end_azot_50_tam_proccesEnd)
                    self.lineEdit_7.setText(str(w50_azot_process_end[0]))
                    self.lineEdit_6.setText("0")
                    print("0-50 qati:",w50_azot_process_end)

                if self.comboBox.currentText() == "Yox":
                    self.lineEdit_5.setText("0")
                    self.lineEdit_7.setText("0")
                    self.lineEdit_6.setText("0")

                if self.comboBox_2.currentText() == "Var":
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_fosfor[s]
                        q = round(q,2)
                        w20_fosfor_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_fosfor[0]
                    k = round(k,2)
                    w20_fosfor_process_end.append(k)
                    total_20 = sum(w20_fosfor_process_end)
                    Total_20_sum_fosfor.append(total_20)    
                    process_end_fosfor_20 = total_20/20
                    process_end_fosfor_20 = round(process_end_fosfor_20,2)
                    w20_fosfor_process_end.clear()
                    w20_fosfor_process_end.append(process_end_fosfor_20)
                    self.lineEdit_8.setText(str(w20_fosfor_process_end[0]))
                    print("0-20 qati:",w20_fosfor_process_end)


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_fosfor[s]
                        q = round(q,2)
                        w50_fosfor_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_fosfor[0]
                    k = round(k,2)
                    w50_fosfor_process_end.append(k)
                    total_50 = sum(w50_fosfor_process_end)
                    Total_50_sum_fosfor.append(total_50)
                    Total_50_sum_fosfor.extend(Total_20_sum_fosfor)
                    process_end_fosfor_50_tam = sum(Total_50_sum_fosfor)
                    process_end_fosfor_50_tam = round(process_end_fosfor_50_tam,2)
                    process_end_fosfor_50_tam_proccesEnd = process_end_fosfor_50_tam/50
                    process_end_fosfor_50_tam_proccesEnd = round(process_end_fosfor_50_tam_proccesEnd,2)
                    w50_fosfor_process_end.clear()
                    w50_fosfor_process_end.append(process_end_fosfor_50_tam_proccesEnd)
                    self.lineEdit_10.setText(str(w50_fosfor_process_end[0]))
                    self.lineEdit_9.setText("0")
                    print("0-50 qati:",w50_fosfor_process_end)

                if self.comboBox_2.currentText() == "Yox":
                    self.lineEdit_8.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")

                if self.comboBox_3.currentText() == "Var":
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_kalium[s]
                        q = round(q,2)
                        w20_kalium_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_kalium[0]
                    k = round(k,2)
                    w20_kalium_process_end.append(k)
                    total_20 = sum(w20_kalium_process_end)
                    Total_20_sum_kalium.append(total_20)    
                    process_end_kalium_20 = total_20/20
                    process_end_kalium_20 = round(process_end_kalium_20,2)
                    w20_kalium_process_end.clear()
                    w20_kalium_process_end.append(process_end_kalium_20)
                    self.lineEdit_11.setText(str(w20_kalium_process_end[0]))
                    print("0-20 qati:",w20_kalium_process_end)


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_kalium[s]
                        q = round(q,2)
                        w50_kalium_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_kalium[0]
                    k = round(k,2)
                    w50_kalium_process_end.append(k)
                    total_50 = sum(w50_kalium_process_end)
                    Total_50_sum_kalium.append(total_50)
                    Total_50_sum_kalium.extend(Total_20_sum_kalium)
                    process_end_kalium_50_tam = sum(Total_50_sum_kalium)
                    process_end_kalium_50_tam = round(process_end_kalium_50_tam,2)
                    process_end_kalium_50_tam_proccesEnd = process_end_kalium_50_tam/50
                    process_end_kalium_50_tam_proccesEnd = round(process_end_kalium_50_tam_proccesEnd,2)
                    w50_kalium_process_end.clear()
                    w50_kalium_process_end.append(process_end_kalium_50_tam_proccesEnd)
                    self.lineEdit_13.setText(str(w50_kalium_process_end[0]))
                    self.lineEdit_12.setText("0")
                    print("0-50 qati:",w50_kalium_process_end)

                if self.comboBox_3.currentText() == "Yox":
                    self.lineEdit_11.setText("0")
                    self.lineEdit_13.setText("0")
                    self.lineEdit_12.setText("0")

                    








                



                    

    ####################################################
    ####################################################
                try:
                    if len(w100_2_index)!=0:
                        r = w100_1[0]+W100_remain[0]
                        w100_1.remove(w100_1[0])
                        w100_1.insert(0,r)
                        for s in w100_2_index:
                            q = (w100_2[s]-w100_1[s])*w100_humus[s]
                            q = round(q,2)
                            w100_humus_process_end.append(q)
                        q = 100-max(w100_2)
                        k = q*w100_humus_end[0]
                        k = round(k,2)
                        w100_humus_process_end.append(k)
                        total = sum(w100_humus_process_end)
                        Total_100_sum.append(total)    
                        Total_100_sum.extend(Total_50_sum)
                        Total_100_sum = sum(Total_100_sum)
                        process_end_humus_100 = Total_100_sum/100
                        process_end_humus_100 = round(process_end_humus_100,2)
                        w100_humus_process_end.clear()
                        w100_humus_process_end.append(process_end_humus_100)
                        self.lineEdit_4.setText(str(w100_humus_process_end[0]))
                        print("0-100 qati:",w100_humus_process_end)
                    
                    else:
                        print("0 - 100 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
            if min(w2)>20 and max(w2)>100:
    ################# 0-20 ############################
                try:
                    for s in w3_humus:
                        k = w3_humus.index(s)
                        w3_humus_index.append(k)
                    r = w3_humus_index[0]
                    w20_2_index.append(r)
                    for s in w20_2_index:
                        w = w3_humus[s]
                        w_str = str(w)
                        w20_humus_process_end.append(w)
                    self.lineEdit_2.setText(w_str)
                    print("0-20 qati:",w20_humus_process_end)
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ################# 0-20 ############################
    ################# 0-50 qatinin indexlemesi ve melumatlari ############################
                for s in w2:
                    try:
                        s = int(s)
                        if 20 < s <= 50:
                            q=w2.index(s)
                            index_w50.append(q)
                    
                            w50_2.append(s)
                        if 50 < s <= 100:
                            q = w2.index(s)
                            index_w100.append(q)
                            w100_2.append(s)
                    except ValueError:
                        print("Excel melumatlarinda her hansi sutunda reqem melumatindan kenar verilen var!!!") 
    ################# 0-50 qatinin indexlemesi ve melumatlari ############################
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in index_w50:
                    q = w1[s]
                    q = int(q)
                    w50_1.append(q)

                for s in index_w50:
                    q = w3_humus[s]
                    w50_humus.append(q)

                for s in index_w50:
                    q = w3_Azot[s]
                    w50_azot.append(q)

                for s in index_w50:
                    q = w3_Fosfor[s]
                    w50_fosfor.append(q)

                for s in index_w50:
                    q = w3_Kalium[s]
                    w50_kalium.append(q)
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in index_w100:
                    q = w1[s]
                    q = int(q)
                    w100_1.append(q)

                for s in index_w100:
                    q = w3_humus[s]
                    w100_humus.append(q)

                for s in index_w100:
                    q = w3_Azot[s]
                    w100_azot.append(q)

                for s in index_w100:
                    q = w3_Fosfor[s]
                    w100_fosfor.append(q)

                for s in index_w100:
                    q = w3_Kalium[s]
                    w100_kalium.append(q)
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in w50_2:
                    k = w50_2.index(s)
                    w50_2_index.append(k)


                for s in w100_2:
                    k = w100_2.index(s)
                    w100_2_index.append(k)
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
    ################################ >100 hallari ucun humusun sonuncu qiymetinin cixarilmasi ############################################################
                for s in w3_humus:
                    k = w3_humus.index(s)
                    w3_humus_index.append(k)
                    w3_humus_index_max = max(w3_humus_index)
                    w3_humus_index.clear()
                    w3_humus_index.append(w3_humus_index_max)
                q = w3_humus[w3_humus_index[0]]
                w100_humus_end.append(q)
    ################################ >100 hallari ucun humusun sonuncu qiymetinin cixarilmasi ############################################################
    ################# 0-50 ############################
                try:
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_humus[s]
                        q = round(q,2)
                        w50_humus_process_end.append(q)
                    q = 50-max(w50_2)
                    W100_remain.append(q)
                    k = q*w100_humus[0]
                    k = round(k,2)
                    w50_humus_process_end.append(k)
                    total_50 = sum(w50_humus_process_end)
                    Total_50_sum.append(total_50)
                    process_end_humus_50_tam = sum(Total_50_sum)
                    process_end_humus_50_tam = round(process_end_humus_50_tam,2)
                    process_end_humus_50_tam_proccesEnd = process_end_humus_50_tam/50
                    process_end_humus_50_tam_proccesEnd = round(process_end_humus_50_tam_proccesEnd,2)
                    w50_humus_process_end.clear()
                    w50_humus_process_end.append(process_end_humus_50_tam_proccesEnd)
                    self.lineEdit_3.setText(str(w50_humus_process_end[0]))
                    print("0-50 qati:",w50_humus_process_end)
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")


                ################## AZOT 0-20 #########################
                if self.comboBox.currentText() == "Var":
                    for s in w3_Azot:
                        k = w3_Azot.index(s)
                        w3_azot_index.append(k)
                    r = w3_azot_index[0]
                    w20_2_index_azot.append(r)
                    for s in w20_2_index_azot:
                        w = w3_Azot[s]
                        w20_azot_process_end.append(w)
                    self.lineEdit_5.setText(str(w20_azot_process_end[0]))
                    print("0-20 qati:",w20_azot_process_end)
                ################## AZOT 0-20 #########################

                    
                ################## AZOT 0-50 #########################
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_azot[s]
                        q = round(q,2)
                        w50_azot_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_azot[0]
                    k = round(k,2)
                    w50_azot_process_end.append(k)
                    total_50 = sum(w50_azot_process_end)
                    Total_50_sum_azot.append(total_50)
                    process_end_azot_50_tam = sum(Total_50_sum_azot)
                    process_end_azot_50_tam = round(process_end_azot_50_tam,2)
                    process_end_azot_50_tam_proccesEnd = process_end_azot_50_tam/50
                    process_end_azot_50_tam_proccesEnd = round(process_end_azot_50_tam_proccesEnd,2)
                    w50_azot_process_end.clear()
                    w50_azot_process_end.append(process_end_azot_50_tam_proccesEnd)
                    self.lineEdit_7.setText(str(w50_azot_process_end[0]))
                    self.lineEdit_6.setText("0")
                    print("0-50 qati:",w50_azot_process_end)
                ################## AZOT 0-50 ######################### 

                if self.comboBox.currentText() == "Yox":
                    self.lineEdit_5.setText("0")
                    self.lineEdit_7.setText("0")
                    self.lineEdit_6.setText("0")

            ################## FOSFOR 0-20 #########################
                if self.comboBox_2.currentText() == "Var":
                    for s in w3_Fosfor:
                        k = w3_Fosfor.index(s)
                        w3_fosfor_index.append(k)
                    r = w3_fosfor_index[0]
                    w20_2_index_fosfor.append(r)
                    for s in w20_2_index_fosfor:
                        w = w3_Fosfor[s]
                        w20_fosfor_process_end.append(w)
                    self.lineEdit_8.setText(str(w20_fosfor_process_end[0]))
                    print("0-20 qati:",w20_fosfor_process_end)
                ################## FOSFOR 0-20 #########################

                    
                ################## FOSFOR 0-50 #########################
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_fosfor[s]
                        q = round(q,2)
                        w50_fosfor_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_fosfor[0]
                    k = round(k,2)
                    w50_fosfor_process_end.append(k)
                    total_50 = sum(w50_fosfor_process_end)
                    Total_50_sum_fosfor.append(total_50)
                    process_end_fosfor_50_tam = sum(Total_50_sum_fosfor)
                    process_end_fosfor_50_tam = round(process_end_fosfor_50_tam,2)
                    process_end_fosfor_50_tam_proccesEnd = process_end_fosfor_50_tam/50
                    process_end_fosfor_50_tam_proccesEnd = round(process_end_fosfor_50_tam_proccesEnd,2)
                    w50_fosfor_process_end.clear()
                    w50_fosfor_process_end.append(process_end_fosfor_50_tam_proccesEnd)
                    self.lineEdit_10.setText(str(w50_fosfor_process_end[0]))
                    self.lineEdit_9.setText("0")
                    print("0-50 qati:",w50_fosfor_process_end)
                ################## FOSFOR 0-50 ######################### 

                if self.comboBox_2.currentText() == "Yox":
                    self.lineEdit_8.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")

                ################## FOSFOR 0-20 #########################
                if self.comboBox_3.currentText() == "Var":
                    for s in w3_Kalium:
                        k = w3_Kalium.index(s)
                        w3_kalium_index.append(k)
                    r = w3_kalium_index[0]
                    w20_2_index_kalium.append(r)
                    for s in w20_2_index_kalium:
                        w = w3_Kalium[s]
                        w20_kalium_process_end.append(w)
                    self.lineEdit_11.setText(str(w20_kalium_process_end[0]))
                    print("0-20 qati:",w20_kalium_process_end)
                ################## KALIUM 0-20 #########################

                    
                ################## FOSFOR 0-50 #########################
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_kalium[s]
                        q = round(q,2)
                        w50_kalium_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_kalium[0]
                    k = round(k,2)
                    w50_kalium_process_end.append(k)
                    total_50 = sum(w50_kalium_process_end)
                    Total_50_sum_kalium.append(total_50)
                    process_end_kalium_50_tam = sum(Total_50_sum_kalium)
                    process_end_kalium_50_tam = round(process_end_kalium_50_tam,2)
                    process_end_kalium_50_tam_proccesEnd = process_end_kalium_50_tam/50
                    process_end_kalium_50_tam_proccesEnd = round(process_end_kalium_50_tam_proccesEnd,2)
                    w50_kalium_process_end.clear()
                    w50_kalium_process_end.append(process_end_kalium_50_tam_proccesEnd)
                    self.lineEdit_13.setText(str(w50_kalium_process_end[0]))
                    self.lineEdit_12.setText("0")
                    print("0-50 qati:",w50_kalium_process_end)
                ################## FOSFOR 0-50 ######################### 

                if self.comboBox_3.currentText() == "Yox":
                    self.lineEdit_11.setText("0")
                    self.lineEdit_13.setText("0")
                    self.lineEdit_12.setText("0")





               

    ################# 0-100 ############################
                try:
                    if len(w100_2_index)!=0:
                        r = w100_1[0]+W100_remain[0]
                        w100_1.remove(w100_1[0])
                        w100_1.insert(0,r)
                        for s in w100_2_index:
                            q = (w100_2[s]-w100_1[s])*w100_humus[s]
                            q = round(q,2)
                            w100_humus_process_end.append(q)
                        q = 100-max(w100_2)
                        k = q*w100_humus_end[0]
                        k = round(k,2)
                        w100_humus_process_end.append(k)
                        total = sum(w100_humus_process_end)
                        Total_100_sum.append(total)    
                        Total_100_sum.extend(Total_50_sum)
                        Total_100_sum = sum(Total_100_sum)
                        process_end_humus_100 = Total_100_sum/100
                        process_end_humus_100 = round(process_end_humus_100,2)
                        w100_humus_process_end.clear()
                        w100_humus_process_end.append(process_end_humus_100)
                        self.lineEdit_4.setText(str(w100_humus_process_end[0]))
                        print("0-100 qati:",w100_humus_process_end)
                    else:
                        print("0 - 100 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ################# 0-100 ############################
            if min(w2)>20 and 90< max(w2)<=100:
    ################# 0-20 ############################
                try:
                    for s in w3_humus:
                        k = w3_humus.index(s)
                        w3_humus_index.append(k)
                    r = w3_humus_index[0]
                    w20_2_index.append(r)
                    for s in w20_2_index:
                        w = w3_humus[s]
                        w20_humus_process_end.append(w)
                    print("0-20 qati:",w20_humus_process_end)
                    self.lineEdit_2.setText(str(w20_humus_process_end[0]))
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ################# 0-20 ############################
    ################# 0-50 qatinin indexlemesi ve melumatlari ############################
                for s in w2:
                    try:
                        s = int(s)
                        if 20 < s <= 50:
                            q=w2.index(s)
                            index_w50.append(q)
                            
                            w50_2.append(s)
                        if 50 < s <= 100:
                            q = w2.index(s)
                            index_w100.append(q)
                            w100_2.append(s)
                    except ValueError:
                        print("Excel melumatlarinda her hansi sutunda reqem melumatindan kenar verilen var!!!") 
    ################# 0-50 qatinin indexlemesi ve melumatlari ############################    
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in index_w50:
                    q = w1[s]
                    q = int(q)
                    w50_1.append(q)

                for s in index_w50:
                    q = w3_humus[s]
                    w50_humus.append(q)

                for s in index_w50:
                    q = w3_Azot[s]
                    w50_azot.append(q)

                for s in index_w50:
                    q = w3_Fosfor[s]
                    w50_fosfor.append(q)

                for s in index_w50:
                    q = w3_Kalium[s]
                    w50_kalium.append(q)
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in index_w100:
                    q = w1[s]
                    q = int(q)
                    w100_1.append(q)

                for s in index_w100:
                    q = w3_humus[s]
                    w100_humus.append(q)

                for s in index_w100:
                    q = w3_Azot[s]
                    w100_azot.append(q)

                for s in index_w100:
                    q = w3_Fosfor[s]
                    w100_fosfor.append(q)

                for s in index_w100:
                    q = w3_Kalium[s]
                    w100_kalium.append(q)
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in w50_2:
                    k = w50_2.index(s)
                    w50_2_index.append(k)   


                for s in w100_2:
                    k = w100_2.index(s)
                    w100_2_index.append(k)
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
    ################################ >100 hallari ucun humusun sonuncu qiymetinin cixarilmasi ############################################################
                for s in w3_humus:
                    k = w3_humus.index(s)
                    w3_humus_index.append(k)
                    w3_humus_index_max = max(w3_humus_index)
                    w3_humus_index.clear()
                    w3_humus_index.append(w3_humus_index_max)
                q = w3_humus[w3_humus_index[0]]
                w100_humus_end.append(q)
    ################################ >100 hallari ucun humusun sonuncu qiymetinin cixarilmasi ############################################################
    ################# 0-50 ############################
                try:
                    if len(w50_2_index)!=0:
                        for s in w50_2_index:
                            q = (w50_2[s]-w50_1[s])*w50_humus[s]
                            q = round(q,2)
                            w50_humus_process_end.append(q)
                        q = 50-max(w50_2)
                        W100_remain.append(q)
                        k = q*w100_humus[0]
                        k = round(k,2)
                        w50_humus_process_end.append(k)
                        total_50 = sum(w50_humus_process_end)
                        Total_50_sum.append(total_50)
                        process_end_humus_50_tam = sum(Total_50_sum)
                        process_end_humus_50_tam = round(process_end_humus_50_tam,2)
                        process_end_humus_50_tam_proccesEnd = process_end_humus_50_tam/50
                        process_end_humus_50_tam_proccesEnd = round(process_end_humus_50_tam_proccesEnd,2)
                        w50_humus_process_end.clear()
                        w50_humus_process_end.append(process_end_humus_50_tam_proccesEnd)
                        print("0-50 qati:",w50_humus_process_end)
                        self.lineEdit_3.setText(str(w50_humus_process_end[0]))
                    else:
                        print("0 - 50 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")


                if self.comboBox.currentText() == "Var":
                ########################### AZOT 0-20 #######################
                    for s in w3_Azot:
                        k = w3_Azot.index(s)
                        w3_azot_index.append(k)
                    r = w3_azot_index[0]
                    w20_2_index_azot.append(r)
                    for s in w20_2_index_azot:
                        w = w3_Azot[s]
                        w20_azot_process_end.append(w)
                    print("0-20 qati:",w20_azot_process_end)
                    self.lineEdit_5.setText(str(w20_azot_process_end[0]))
                ########################### AZOT 0-20 #######################
                    
                ########################### AZOT 0-50 #######################   
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_azot[s]
                        q = round(q,2)
                        w50_azot_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_azot[0]
                    k = round(k,2)
                    w50_azot_process_end.append(k)
                    total_50 = sum(w50_azot_process_end)
                    Total_50_sum_azot.append(total_50)
                    process_end_azot_50_tam = sum(Total_50_sum_azot)
                    process_end_azot_50_tam = round(process_end_azot_50_tam,2)
                    process_end_azot_50_tam_proccesEnd = process_end_azot_50_tam/50
                    process_end_azot_50_tam_proccesEnd = round(process_end_azot_50_tam_proccesEnd,2)
                    w50_azot_process_end.clear()
                    w50_azot_process_end.append(process_end_azot_50_tam_proccesEnd)
                    print("0-50 qati:",w50_azot_process_end)
                    self.lineEdit_7.setText(str(w50_azot_process_end[0]))
                    self.lineEdit_6.setText("0")
                ########################### AZOT 0-50 ####################### 
                    
                if self.comboBox.currentText() == "Yox":
                    self.lineEdit_5.setText("0")
                    self.lineEdit_7.setText("0")
                    self.lineEdit_6.setText("0")

                if self.comboBox_2.currentText() == "Var":
                ########################### AZOT 0-20 #######################
                    for s in w3_Fosfor:
                        k = w3_Fosfor.index(s)
                        w3_fosfor_index.append(k)
                    r = w3_fosfor_index[0]
                    w20_2_index_fosfor.append(r)
                    for s in w20_2_index_fosfor:
                        w = w3_Fosfor[s]
                        w20_fosfor_process_end.append(w)
                    print("0-20 qati:",w20_fosfor_process_end)
                    self.lineEdit_8.setText(str(w20_fosfor_process_end[0]))
                ########################### AZOT 0-20 #######################
                    
                ########################### AZOT 0-50 #######################   
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_fosfor[s]
                        q = round(q,2)
                        w50_fosfor_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_fosfor[0]
                    k = round(k,2)
                    w50_fosfor_process_end.append(k)
                    total_50 = sum(w50_fosfor_process_end)
                    Total_50_sum_fosfor.append(total_50)
                    process_end_fosfor_50_tam = sum(Total_50_sum_fosfor)
                    process_end_fosfor_50_tam = round(process_end_fosfor_50_tam,2)
                    process_end_fosfor_50_tam_proccesEnd = process_end_fosfor_50_tam/50
                    process_end_fosfor_50_tam_proccesEnd = round(process_end_fosfor_50_tam_proccesEnd,2)
                    w50_fosfor_process_end.clear()
                    w50_fosfor_process_end.append(process_end_fosfor_50_tam_proccesEnd)
                    print("0-50 qati:",w50_fosfor_process_end)
                    self.lineEdit_10.setText(str(w50_fosfor_process_end[0]))
                    self.lineEdit_9.setText("0")
                ########################### AZOT 0-50 ####################### 
                    
                if self.comboBox_2.currentText() == "Yox":
                    self.lineEdit_8.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")

                if self.comboBox_3.currentText() == "Var":
                ########################### AZOT 0-20 #######################
                    for s in w3_Kalium:
                        k = w3_Kalium.index(s)
                        w3_kalium_index.append(k)
                    r = w3_kalium_index[0]
                    w20_2_index_kalium.append(r)
                    for s in w20_2_index_kalium:
                        w = w3_Kalium[s]
                        w20_kalium_process_end.append(w)
                    print("0-20 qati:",w20_kalium_process_end)
                    self.lineEdit_11.setText(str(w20_kalium_process_end[0]))
                ########################### AZOT 0-20 #######################
                    
                ########################### AZOT 0-50 #######################   
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_kalium[s]
                        q = round(q,2)
                        w50_kalium_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_kalium[0]
                    k = round(k,2)
                    w50_kalium_process_end.append(k)
                    total_50 = sum(w50_kalium_process_end)
                    Total_50_sum_kalium.append(total_50)
                    process_end_kalium_50_tam = sum(Total_50_sum_kalium)
                    process_end_kalium_50_tam = round(process_end_kalium_50_tam,2)
                    process_end_kalium_50_tam_proccesEnd = process_end_kalium_50_tam/50
                    process_end_kalium_50_tam_proccesEnd = round(process_end_kalium_50_tam_proccesEnd,2)
                    w50_kalium_process_end.clear()
                    w50_kalium_process_end.append(process_end_kalium_50_tam_proccesEnd)
                    print("0-50 qati:",w50_kalium_process_end)
                    self.lineEdit_13.setText(str(w50_kalium_process_end[0]))
                    self.lineEdit_12.setText("0")
                ########################### AZOT 0-50 ####################### 
                    
                if self.comboBox_3.currentText() == "Yox":
                    self.lineEdit_11.setText("0")
                    self.lineEdit_13.setText("0")
                    self.lineEdit_12.setText("0")


                ################# 0-100 ############################
                try:
                    if len(w100_2_index)!=0:
                        r = w100_1[0]+W100_remain[0]
                        w100_1.remove(w100_1[0])
                        w100_1.insert(0,r)
                        for s in w100_2_index:
                            q = (w100_2[s]-w100_1[s])*w100_humus[s]
                            q = round(q,2)
                            w100_humus_process_end.append(q)
                        total = sum(w100_humus_process_end)
                        Total_100_sum.append(total)    
                        Total_100_sum.extend(Total_50_sum)
                        Total_100_sum = sum(Total_100_sum)
                        process_end_humus_100 = Total_100_sum/100
                        process_end_humus_100 = round(process_end_humus_100,2)
                        w100_humus_process_end.clear()
                        w100_humus_process_end.append(process_end_humus_100)
                        print("0-100 qati:",w100_humus_process_end)
                        self.lineEdit_4.setText(str(w100_humus_process_end[0]))
                    else:
                        print("0 - 100 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ################# 0-100 ############################
            if min(w2)<=20 and 90 < max(w2) <=100:
                for s in w2:
                    try:
                        s = int(s)
                        if s <= 20:
                            q=w2.index(s)
                            index_w20.append(q)
                            w20_2.append(s)
                        if 20 < s <= 50:
                            q=w2.index(s)
                            index_w50.append(q)
                            w50_2.append(s)
                        if 50 < s <= 100:
                            q = w2.index(s)
                            index_w100.append(q)
                            w100_2.append(s)
                    except ValueError:
                        print("Excel melumatlarinda her hansi sutunda reqem melumatindan kenar verilen var!!!")

    ####################################################
            
                for s in index_w20:
                    q = w1[s]
                    q = int(q)
                    w20_1.append(q)

                for s in index_w20:
                    q = w3_humus[s]
                    w20_humus.append(q)

                for s in index_w20:
                    q = w3_Azot[s]
                    w20_azot.append(q)

                for s in index_w20:
                    q = w3_Fosfor[s]
                    w20_fosfor.append(q)

                for s in index_w20:
                    q = w3_Kalium[s]
                    w20_kalium.append(q)
        
    ####################################################
    ####################################################
        
                for s in index_w50:
                    q = w1[s]
                    q = int(q)
                    w50_1.append(q)

                for s in index_w50:
                    q = w3_humus[s]
                    w50_humus.append(q)

                for s in index_w50:
                    q = w3_Azot[s]
                    w50_azot.append(q)

                for s in index_w50:
                    q = w3_Fosfor[s]
                    w50_fosfor.append(q)

                for s in index_w50:
                    q = w3_Kalium[s]
                    w50_kalium.append(q)

    ####################################################
    ####################################################
        
                for s in index_w100:
                    q = w1[s]
                    q = int(q)
                    w100_1.append(q)

                for s in index_w100:
                    q = w3_humus[s]
                    w100_humus.append(q)

                for s in index_w100:
                    q = w3_Azot[s]
                    w100_azot.append(q)

                for s in index_w100:
                    q = w3_Fosfor[s]
                    w100_fosfor.append(q)

                for s in index_w100:
                    q = w3_Kalium[s]
                    w100_kalium.append(q)
        
    ####################################################
    ####################################################

    ####################################################

                for s in w20_2:
                    k = w20_2.index(s)
                    w20_2_index.append(k)

                for s in w50_2:
                    k = w50_2.index(s)
                    w50_2_index.append(k)




                for s in w100_2:
                    k = w100_2.index(s)
                    w100_2_index.append(k)


    ####################################################
                for s in w3_humus:
                    k = w3_humus.index(s)
                    w3_humus_index.append(k)
                    w3_humus_index_max = max(w3_humus_index)
                    w3_humus_index.clear()
                    w3_humus_index.append(w3_humus_index_max)
                q = w3_humus[w3_humus_index[0]]
                w100_humus_end.append(q)

    ####################################################
    ####################################################
                try:
                    if len(w20_2_index)!= 0:
                        for s in w20_2_index:
                            q =  (w20_2[s] - w20_1[s])*w20_humus[s]
                            q = round(q,2)
                            w20_humus_process_end.append(q)
                        q = 20-max(w20_2)
                        W50_remain.append(q)
                        k = q*w50_humus[0]
                        k = round(k,2)
                        w20_humus_process_end.append(k)
                        total_20 = sum(w20_humus_process_end)
                        Total_20_sum.append(total_20)    
                        process_end_humus_20 = total_20/20
                        process_end_humus_20 = round(process_end_humus_20,2)
                        w20_humus_process_end.clear()
                        w20_humus_process_end.append(process_end_humus_20)
                        print("0-20 qati:",w20_humus_process_end)
                        self.lineEdit_2.setText(str(w20_humus_process_end[0]))
                    else:
                        print("0-20 qatinin hesablanmasi ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ####################################################    
    ####################################################
                try:
                    if len(w50_2_index)!=0:
                        r = w50_1[0]+W50_remain[0]
                        w50_1.remove(w50_1[0])
                        w50_1.insert(0,r)
                        for s in w50_2_index:
                            q = (w50_2[s]-w50_1[s])*w50_humus[s]
                            q = round(q,2)
                            w50_humus_process_end.append(q)
                        q = 50-max(w50_2)
                        W100_remain.append(q)
                        k = q*w100_humus[0]
                        k = round(k,2)
                        w50_humus_process_end.append(k)
                        total_50 = sum(w50_humus_process_end)
                        Total_50_sum.append(total_50)
                        Total_50_sum.extend(Total_20_sum)
                        process_end_humus_50_tam = sum(Total_50_sum)
                        process_end_humus_50_tam = round(process_end_humus_50_tam,2)
                        process_end_humus_50_tam_proccesEnd = process_end_humus_50_tam/50
                        process_end_humus_50_tam_proccesEnd = round(process_end_humus_50_tam_proccesEnd,2)
                        w50_humus_process_end.clear()
                        w50_humus_process_end.append(process_end_humus_50_tam_proccesEnd)
                        print("0-50 qati:",w50_humus_process_end)
                        self.lineEdit_3.setText(str(w50_humus_process_end[0]))
                    else:
                        print("0 - 50 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")

                if self.comboBox.currentText() == "Var":
                ################ 0-20 AZOT ########################
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_azot[s]
                        q = round(q,2)
                        w20_azot_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_azot[0]
                    k = round(k,2)
                    w20_azot_process_end.append(k)
                    total_20 = sum(w20_azot_process_end)
                    Total_20_sum_azot.append(total_20)    
                    process_end_azot_20 = total_20/20
                    process_end_azot_20 = round(process_end_azot_20,2)
                    w20_azot_process_end.clear()
                    w20_azot_process_end.append(process_end_azot_20)
                    print("0-20 qati:",w20_azot_process_end)
                    self.lineEdit_5.setText(str(w20_azot_process_end[0]))
                ################## 0-20 AZOT ###############################

                ################## 0-50 AZOT ################################ 

                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_azot[s]
                        q = round(q,2)
                        w50_azot_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_azot[0]
                    k = round(k,2)
                    w50_azot_process_end.append(k)
                    total_50 = sum(w50_azot_process_end)
                    Total_50_sum_azot.append(total_50)
                    Total_50_sum_azot.extend(Total_20_sum_azot)
                    process_end_azot_50_tam = sum(Total_50_sum_azot)
                    process_end_azot_50_tam = round(process_end_azot_50_tam,2)
                    process_end_azot_50_tam_proccesEnd = process_end_azot_50_tam/50
                    process_end_azot_50_tam_proccesEnd = round(process_end_azot_50_tam_proccesEnd,2)
                    w50_azot_process_end.clear()
                    w50_azot_process_end.append(process_end_azot_50_tam_proccesEnd)
                    print("0-50 qati:",w50_azot_process_end)
                    self.lineEdit_7.setText(str(w50_azot_process_end[0]))
                    self.lineEdit_6.setText("0")

                ################# 0-50 AZOT ######################################

                if self.comboBox.currentText() == "Yox":
                    self.lineEdit_5.setText("0")
                    self.lineEdit_7.setText("0")
                    self.lineEdit_6.setText("0")

                if self.comboBox_2.currentText() == "Var":
                ################ 0-20 AZOT ########################
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_fosfor[s]
                        q = round(q,2)
                        w20_fosfor_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_fosfor[0]
                    k = round(k,2)
                    w20_fosfor_process_end.append(k)
                    total_20 = sum(w20_fosfor_process_end)
                    Total_20_sum_fosfor.append(total_20)    
                    process_end_fosfor_20 = total_20/20
                    process_end_fosfor_20 = round(process_end_fosfor_20,2)
                    w20_fosfor_process_end.clear()
                    w20_fosfor_process_end.append(process_end_fosfor_20)
                    print("0-20 qati:",w20_fosfor_process_end)
                    self.lineEdit_8.setText(str(w20_fosfor_process_end[0]))
                ################## 0-20 AZOT ###############################

                ################## 0-50 AZOT ################################ 

                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_fosfor[s]
                        q = round(q,2)
                        w50_fosfor_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_fosfor[0]
                    k = round(k,2)
                    w50_fosfor_process_end.append(k)
                    total_50 = sum(w50_fosfor_process_end)
                    Total_50_sum_fosfor.append(total_50)
                    Total_50_sum_fosfor.extend(Total_20_sum_fosfor)
                    process_end_fosfor_50_tam = sum(Total_50_sum_fosfor)
                    process_end_fosfor_50_tam = round(process_end_fosfor_50_tam,2)
                    process_end_fosfor_50_tam_proccesEnd = process_end_fosfor_50_tam/50
                    process_end_fosfor_50_tam_proccesEnd = round(process_end_fosfor_50_tam_proccesEnd,2)
                    w50_fosfor_process_end.clear()
                    w50_fosfor_process_end.append(process_end_fosfor_50_tam_proccesEnd)
                    print("0-50 qati:",w50_fosfor_process_end)
                    self.lineEdit_10.setText(str(w50_fosfor_process_end[0]))
                    self.lineEdit_9.setText("0")

                ################# 0-50 AZOT ######################################

                if self.comboBox_2.currentText() == "Yox":
                    self.lineEdit_8.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")

                if self.comboBox_3.currentText() == "Var":
                ################ 0-20 AZOT ########################
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_kalium[s]
                        q = round(q,2)
                        w20_kalium_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_kalium[0]
                    k = round(k,2)
                    w20_kalium_process_end.append(k)
                    total_20 = sum(w20_kalium_process_end)
                    Total_20_sum_kalium.append(total_20)    
                    process_end_kalium_20 = total_20/20
                    process_end_kalium_20 = round(process_end_kalium_20,2)
                    w20_kalium_process_end.clear()
                    w20_kalium_process_end.append(process_end_kalium_20)
                    print("0-20 qati:",w20_kalium_process_end)
                    self.lineEdit_11.setText(str(w20_kalium_process_end[0]))
                ################## 0-20 AZOT ###############################

                ################## 0-50 AZOT ################################ 

                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_kalium[s]
                        q = round(q,2)
                        w50_kalium_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_kalium[0]
                    k = round(k,2)
                    w50_kalium_process_end.append(k)
                    total_50 = sum(w50_kalium_process_end)
                    Total_50_sum_kalium.append(total_50)
                    Total_50_sum_kalium.extend(Total_20_sum_kalium)
                    process_end_kalium_50_tam = sum(Total_50_sum_kalium)
                    process_end_kalium_50_tam = round(process_end_kalium_50_tam,2)
                    process_end_kalium_50_tam_proccesEnd = process_end_kalium_50_tam/50
                    process_end_kalium_50_tam_proccesEnd = round(process_end_kalium_50_tam_proccesEnd,2)
                    w50_kalium_process_end.clear()
                    w50_kalium_process_end.append(process_end_kalium_50_tam_proccesEnd)
                    print("0-50 qati:",w50_kalium_process_end)
                    self.lineEdit_13.setText(str(w50_kalium_process_end[0]))
                    self.lineEdit_12.setText("0")

                ################# 0-50 AZOT ######################################

                if self.comboBox_3.currentText() == "Yox":
                    self.lineEdit_11.setText("0")
                    self.lineEdit_13.setText("0")
                    self.lineEdit_12.setText("0")

                




    ####################################################
    ####################################################
                try:
                    if len(w100_2_index)!=0:
                        r = w100_1[0]+W100_remain[0]
                        w100_1.remove(w100_1[0])
                        w100_1.insert(0,r)
                        for s in w100_2_index:
                            q = (w100_2[s]-w100_1[s])*w100_humus[s]
                            q = round(q,2)
                            w100_humus_process_end.append(q)
                        total = sum(w100_humus_process_end)
                        Total_100_sum.append(total)    
                        Total_100_sum.extend(Total_50_sum)
                        Total_100_sum = sum(Total_100_sum)
                        process_end_humus_100 = Total_100_sum/100
                        process_end_humus_100 = round(process_end_humus_100,2)
                        w100_humus_process_end.clear()
                        w100_humus_process_end.append(process_end_humus_100)
                        print("0-100 qati:",w100_humus_process_end)
                        self.lineEdit_4.setText(str(w100_humus_process_end[0]))
                    else:
                        print("0 - 100 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")

    ##################################################################################
            if min(w2)<=20 and max(w2)<90:
    ## Qatlar uzre melumatlar toplanilir ########################################################################################
                for s in w2:
                    try:
                        s = int(s)
                        if s <= 20:
                            q=w2.index(s)
                            index_w20.append(q)
                            w20_2.append(s)
                        if 20 < s <= 50:
                            q=w2.index(s)
                            index_w50.append(q)
                            w50_2.append(s)

                        if 50 < s <= 100:
                            q = w2.index(s)
                            index_w100.append(q)
                    except ValueError:
                        print("Excel melumatlarinda her hansi sutunda reqem melumatindan kenar verilen var!!!")
    ## Qatlar uzre melumatlar toplanilir #############################################################################################

    ############## 20 qatinin indexlemesi esasinda 1ci sutunun ve 20 qatinin humus melumatlari toplanir ######################################
            
                for s in index_w20:
                    q = w1[s]
                    q = int(q)
                    w20_1.append(q)

                for s in index_w20:
                    q = w3_humus[s]
                    w20_humus.append(q)

                for s in index_w20:
                    q = w3_Azot[s]
                    w20_azot.append(q)

                for s in index_w20:
                    q = w3_Fosfor[s]
                    w20_fosfor.append(q)

                for s in index_w20:
                    q = w3_Kalium[s]
                    w20_kalium.append(q)
    ############## 20 qatinin indexlemesi esasinda 1ci sutunun ve 20 qatinin humus melumatlari toplanir ######################################

    ############### 50 qatinin indexlemesi esasinda 1ci sutunun ve 50 qatinin humus melumatlari toplanir #####################################
        
                for s in index_w50:
                    q = w1[s]
                    q = int(q)
                    w50_1.append(q)

                for s in index_w50:
                    q = w3_humus[s]
                    w50_humus.append(q)

                for s in index_w50:
                    q = w3_Azot[s]
                    w50_azot.append(q)

                for s in index_w50:
                    q = w3_Fosfor[s]
                    w50_fosfor.append(q)

                for s in index_w50:
                    q = w3_Kalium[s]
                    w50_kalium.append(q)
    ############### 50 qatinin indexlemesi esasinda 1ci sutunun ve 50 qatinin humus melumatlari toplanir #####################################
      
    ############### 20 ve 50 qatlarinin oz listlerindeki indexlemeleri aparilir ##############################################################

                for s in w20_2:
                    k = w20_2.index(s)
                    w20_2_index.append(k)

                for s in w50_2:
                    k = w50_2.index(s)
                    w50_2_index.append(k)
    ############### 20 ve 50 qatlarinin oz listlerindeki indexlemeleri aparilir ##############################################################

    ############ 100 qatinin indexlemesi esasinda 1ci sutunun ve 100 qatinin humus melumatlari toplanir  ################################
                for s in index_w100:
                    q = w1[s]
                    q = int(q)
                    w100_1.append(q)

                for s in index_w100:
                    q = w3_humus[s]
                    w100_humus.append(q)

                for s in index_w100:
                    q = w3_Azot[s]
                    w100_azot.append(q)

                for s in index_w100:
                    q = w3_Fosfor[s]
                    w100_fosfor.append(q)

                for s in index_w100:
                    q = w3_Kalium[s]
                    w100_kalium.append(q)
    ############ 100 qatinin indexlemesi esasinda 1ci sutunun ve 100 qatinin humus melumatlari toplanir  ################################
        

    ############ 100 qati hesablanarken sonuncu humus melumati indexlenir ###############################################################
                for s in w3_humus:
                    k = w3_humus.index(s)
                    w3_humus_index.append(k)
                    w3_humus_index_max = max(w3_humus_index)
                    w3_humus_index.clear()
                    w3_humus_index.append(w3_humus_index_max)
                q = w3_humus[w3_humus_index[0]]
                w100_humus_end.append(q)
    ############ 100 qati hesablanarken sonuncu humus melumati indexlenir ###############################################################
        
    ################ 0-20 qati hesablanir ####################################
                try:
                    if len(w20_2_index)!= 0:
                        for s in w20_2_index:
                            q =  (w20_2[s] - w20_1[s])*w20_humus[s]
                            q = round(q,2)
                            w20_humus_process_end.append(q)
                        q = 20-max(w20_2)
                        W50_remain.append(q)
                        k = q*w50_humus[0]
                        k = round(k,2)
                        w20_humus_process_end.append(k)
                        total_20 = sum(w20_humus_process_end)
                        Total_20_sum.append(total_20)    
                        process_end_humus_20 = total_20/20
                        process_end_humus_20 = round(process_end_humus_20,2)
                        w20_humus_process_end.clear()
                        w20_humus_process_end.append(process_end_humus_20)
                        print("0-20 qati:",w20_humus_process_end)
                        self.lineEdit_2.setText(str(w20_humus_process_end[0]))
                    else:
                        print("0-20 qatinin hesablanmasi ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ################ 0-20 qati hesablanir ####################################    
    ################ 0-50 qati hesablanir ####################################
                try:
                    if len(w50_2_index)!=0:
                        r = w50_1[0]+W50_remain[0]
                        w50_1.remove(w50_1[0])
                        w50_1.insert(0,r)
                        for s in w50_2_index:
                            q = (w50_2[s]-w50_1[s])*w50_humus[s]
                            q = round(q,2)
                            w50_humus_process_end.append(q)
                        q = 50-max(w50_2)
                        k = q*w100_humus[0]
                        k = round(k,2)
                        w50_humus_process_end.append(k)
                        total_50 = sum(w50_humus_process_end)
                        Total_50_sum.append(total_50)
                        Total_50_sum.extend(Total_20_sum)
                        process_end_humus_50_tam = sum(Total_50_sum)
                        process_end_humus_50_tam = round(process_end_humus_50_tam,2)
                        process_end_humus_50_tam_proccesEnd = process_end_humus_50_tam/50
                        process_end_humus_50_tam_proccesEnd = round(process_end_humus_50_tam_proccesEnd,2)
                        w50_humus_process_end.clear()
                        w50_humus_process_end.append(process_end_humus_50_tam_proccesEnd)
                        print("0-50 qati:",w50_humus_process_end)
                        self.lineEdit_3.setText(str(w50_humus_process_end[0]))
                        self.lineEdit_4.setText("0")
                    else:
                        print("0 - 50 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")

                if self.comboBox.currentText() == "Var":
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_azot[s]
                        q = round(q,2)
                        w20_azot_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_azot[0]
                    k = round(k,2)
                    w20_azot_process_end.append(k)
                    total_20 = sum(w20_azot_process_end)
                    Total_20_sum_azot.append(total_20)    
                    process_end_azot_20 = total_20/20
                    process_end_azot_20 = round(process_end_azot_20,2)
                    w20_azot_process_end.clear()
                    w20_azot_process_end.append(process_end_azot_20)
                    print("0-20 qati:",w20_azot_process_end)
                    self.lineEdit_5.setText(str(w20_azot_process_end[0]))


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_azot[s]
                        q = round(q,2)
                        w50_azot_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_azot[0]
                    k = round(k,2)
                    w50_azot_process_end.append(k)
                    total_50 = sum(w50_azot_process_end)
                    Total_50_sum_azot.append(total_50)
                    Total_50_sum_azot.extend(Total_20_sum_azot)
                    process_end_azot_50_tam = sum(Total_50_sum_azot)
                    process_end_azot_50_tam = round(process_end_azot_50_tam,2)
                    process_end_azot_50_tam_proccesEnd = process_end_azot_50_tam/50
                    process_end_azot_50_tam_proccesEnd = round(process_end_azot_50_tam_proccesEnd,2)
                    w50_azot_process_end.clear()
                    w50_azot_process_end.append(process_end_azot_50_tam_proccesEnd)
                    print("0-50 qati:",w50_azot_process_end)
                    self.lineEdit_7.setText(str(w50_azot_process_end[0]))
                    self.lineEdit_6.setText("0")

                if self.comboBox.currentText() == "Yox":
                    self.lineEdit_5.setText("0")
                    self.lineEdit_7.setText("0")
                    self.lineEdit_6.setText("0")

                if self.comboBox_2.currentText() == "Var":
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_fosfor[s]
                        q = round(q,2)
                        w20_fosfor_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_fosfor[0]
                    k = round(k,2)
                    w20_fosfor_process_end.append(k)
                    total_20 = sum(w20_fosfor_process_end)
                    Total_20_sum_fosfor.append(total_20)    
                    process_end_fosfor_20 = total_20/20
                    process_end_fosfor_20 = round(process_end_fosfor_20,2)
                    w20_fosfor_process_end.clear()
                    w20_fosfor_process_end.append(process_end_fosfor_20)
                    print("0-20 qati:",w20_fosfor_process_end)
                    self.lineEdit_8.setText(str(w20_fosfor_process_end[0]))


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_fosfor[s]
                        q = round(q,2)
                        w50_fosfor_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_fosfor[0]
                    k = round(k,2)
                    w50_fosfor_process_end.append(k)
                    total_50 = sum(w50_fosfor_process_end)
                    Total_50_sum_fosfor.append(total_50)
                    Total_50_sum_fosfor.extend(Total_20_sum_fosfor)
                    process_end_fosfor_50_tam = sum(Total_50_sum_fosfor)
                    process_end_fosfor_50_tam = round(process_end_fosfor_50_tam,2)
                    process_end_fosfor_50_tam_proccesEnd = process_end_fosfor_50_tam/50
                    process_end_fosfor_50_tam_proccesEnd = round(process_end_fosfor_50_tam_proccesEnd,2)
                    w50_fosfor_process_end.clear()
                    w50_fosfor_process_end.append(process_end_fosfor_50_tam_proccesEnd)
                    print("0-50 qati:",w50_fosfor_process_end)
                    self.lineEdit_10.setText(str(w50_fosfor_process_end[0]))
                    self.lineEdit_9.setText("0")

                if self.comboBox_2.currentText() == "Yox":
                    self.lineEdit_8.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")

                if self.comboBox_3.currentText() == "Var":
                    for s in w20_2_index:
                        q =  (w20_2[s] - w20_1[s])*w20_kalium[s]
                        q = round(q,2)
                        w20_kalium_process_end.append(q)
                    q = 20-max(w20_2)
                    k = q*w50_kalium[0]
                    k = round(k,2)
                    w20_kalium_process_end.append(k)
                    total_20 = sum(w20_kalium_process_end)
                    Total_20_sum_kalium.append(total_20)    
                    process_end_kalium_20 = total_20/20
                    process_end_kalium_20 = round(process_end_kalium_20,2)
                    w20_kalium_process_end.clear()
                    w20_kalium_process_end.append(process_end_kalium_20)
                    print("0-20 qati:",w20_kalium_process_end)
                    self.lineEdit_11.setText(str(w20_kalium_process_end[0]))


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_kalium[s]
                        q = round(q,2)
                        w50_kalium_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_kalium[0]
                    k = round(k,2)
                    w50_kalium_process_end.append(k)
                    total_50 = sum(w50_kalium_process_end)
                    Total_50_sum_kalium.append(total_50)
                    Total_50_sum_kalium.extend(Total_20_sum_kalium)
                    process_end_kalium_50_tam = sum(Total_50_sum_kalium)
                    process_end_kalium_50_tam = round(process_end_kalium_50_tam,2)
                    process_end_kalium_50_tam_proccesEnd = process_end_kalium_50_tam/50
                    process_end_kalium_50_tam_proccesEnd = round(process_end_kalium_50_tam_proccesEnd,2)
                    w50_kalium_process_end.clear()
                    w50_kalium_process_end.append(process_end_kalium_50_tam_proccesEnd)
                    print("0-50 qati:",w50_kalium_process_end)
                    self.lineEdit_13.setText(str(w50_kalium_process_end[0]))
                    self.lineEdit_12.setText("0")

                if self.comboBox_3.currentText() == "Yox":
                    self.lineEdit_11.setText("0")
                    self.lineEdit_13.setText("0")
                    self.lineEdit_12.setText("0")
                
                

    ################ 0-50 qati hesablanir ####################################
            if min(w2)>20 and max(w2)<90:
    ################# 0-20 qatinin melumatlari hesablanir ############################
                try:
                    for s in w3_humus:
                        k = w3_humus.index(s)
                        w3_humus_index.append(k)
                    r = w3_humus_index[0]
                    w20_2_index.append(r)
                    for s in w20_2_index:
                        w = w3_humus[s]
                        w20_humus_process_end.append(w)
                    print("0-20 qati:",w20_humus_process_end)
                    self.lineEdit_2.setText(str(w20_humus_process_end[0]))
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ################# 0-20 qatinin melumatlari hesablanir ############################
    ################# 0-50 qatinin indexlemesi ve melumatlari ############################
                for s in w2:
                    try:
                        s = int(s)
                        if 20 < s <= 50:
                            q=w2.index(s)
                            index_w50.append(q)                
                            w50_2.append(s)
    ## 0-100 qatinnan humus melumatlarinin goturulmesi ucun indexleme aparilir########################                
                        if 50 < s <= 100:
                            q = w2.index(s)
                            index_w100.append(q)
    ## 0-100 qatinnan humus melumatlarinin goturulmesi ucun indexleme aparilir########################  
                    except ValueError:
                        print("Excel melumatlarinda her hansi sutunda reqem melumatindan kenar verilen var!!!")    
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in index_w50:
                    q = w1[s]
                    q = int(q)
                    w50_1.append(q)

                for s in index_w50:
                    q = w3_humus[s]
                    w50_humus.append(q)

                for s in index_w50:
                    q = w3_Azot[s]
                    w50_azot.append(q)

                for s in index_w50:
                    q = w3_Fosfor[s]
                    w50_fosfor.append(q)

                for s in index_w50:
                    q = w3_Kalium[s]
                    w50_kalium.append(q) 
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
    ################### 0-100 qatinin humus melumatlari toplanir ################################


                for s in index_w100:
                    q = w3_humus[s]
                    w100_humus.append(q)

                for s in index_w100:
                    q = w3_Azot[s]
                    w100_azot.append(q)

                for s in index_w100:
                    q = w3_Fosfor[s]
                    w100_fosfor.append(q)

                for s in index_w100:
                    q = w3_Kalium[s]
                    w100_kalium.append(q)
    ################### 0-100 qatinin humus melumatlari toplanir ################################
    ################### 0-50 qatinin 2ci hissesinin indexlemesi aparilir ################################
                for s in w50_2:
                    k = w50_2.index(s)
                    w50_2_index.append(k)
    ################### 0-50 qatinin 2ci hissesinin indexlemesi aparilir ################################


    ################# 0-50 ############################
                try:
                    if len(w50_2_index)!=0:
                        for s in w50_2_index:
                            q = (w50_2[s]-w50_1[s])*w50_humus[s]
                            q = round(q,2)
                            w50_humus_process_end.append(q)
                        q = 50-max(w50_2)
                        W100_remain.append(q)
                        k = q*w100_humus[0]
                        k = round(k,2)
                        w50_humus_process_end.append(k)
                        total_50 = sum(w50_humus_process_end)
                        Total_50_sum.append(total_50)
                        process_end_humus_50_tam = sum(Total_50_sum)
                        process_end_humus_50_tam = round(process_end_humus_50_tam,2)
                        process_end_humus_50_tam_proccesEnd = process_end_humus_50_tam/50
                        process_end_humus_50_tam_proccesEnd = round(process_end_humus_50_tam_proccesEnd,2)
                        w50_humus_process_end.clear()
                        w50_humus_process_end.append(process_end_humus_50_tam_proccesEnd)
                        print("0-50 qati:",w50_humus_process_end)
                        self.lineEdit_3.setText(str(w50_humus_process_end[0]))
                        self.lineEdit_4.setText("0")
                    else:
                        print("0 - 50 qati ucun lazimi melumatlar yoxdur!!!")
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")

                if self.comboBox.currentText() == "Var":
                    for s in w3_Azot:
                        k = w3_Azot.index(s)
                        w3_azot_index.append(k)
                    r = w3_azot_index[0]
                    w20_2_index_azot.append(r)
                    for s in w20_2_index_azot:
                        w = w3_Azot[s]
                        w20_azot_process_end.append(w)
                    print("0-20 qati:",w20_azot_process_end)
                    self.lineEdit_5.setText(str(w20_azot_process_end[0]))


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_azot[s]
                        q = round(q,2)
                        w50_azot_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_azot[0]
                    k = round(k,2)
                    w50_azot_process_end.append(k)
                    total_50 = sum(w50_azot_process_end)
                    Total_50_sum_azot.append(total_50)
                    process_end_azot_50_tam = sum(Total_50_sum_azot)
                    process_end_azot_50_tam = round(process_end_azot_50_tam,2)
                    process_end_azot_50_tam_proccesEnd = process_end_azot_50_tam/50
                    process_end_azot_50_tam_proccesEnd = round(process_end_azot_50_tam_proccesEnd,2)
                    w50_azot_process_end.clear()
                    w50_azot_process_end.append(process_end_azot_50_tam_proccesEnd)
                    print("0-50 qati:",w50_azot_process_end)
                    self.lineEdit_7.setText(str(w50_azot_process_end[0]))
                    self.lineEdit_6.setText("0")

                if self.comboBox.currentText() == "Yox":
                    self.lineEdit_5.setText("0")
                    self.lineEdit_7.setText("0")
                    self.lineEdit_6.setText("0")

                if self.comboBox_2.currentText() == "Var":
                    for s in w3_Fosfor:
                        k = w3_Fosfor.index(s)
                        w3_fosfor_index.append(k)
                    r = w3_fosfor_index[0]
                    w20_2_index_fosfor.append(r)
                    for s in w20_2_index_fosfor:
                        w = w3_Fosfor[s]
                        w20_fosfor_process_end.append(w)
                    print("0-20 qati:",w20_fosfor_process_end)
                    self.lineEdit_8.setText(str(w20_fosfor_process_end[0]))


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_fosfor[s]
                        q = round(q,2)
                        w50_fosfor_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_fosfor[0]
                    k = round(k,2)
                    w50_fosfor_process_end.append(k)
                    total_50 = sum(w50_fosfor_process_end)
                    Total_50_sum_fosfor.append(total_50)
                    process_end_fosfor_50_tam = sum(Total_50_sum_fosfor)
                    process_end_fosfor_50_tam = round(process_end_fosfor_50_tam,2)
                    process_end_fosfor_50_tam_proccesEnd = process_end_fosfor_50_tam/50
                    process_end_fosfor_50_tam_proccesEnd = round(process_end_fosfor_50_tam_proccesEnd,2)
                    w50_fosfor_process_end.clear()
                    w50_fosfor_process_end.append(process_end_fosfor_50_tam_proccesEnd)
                    print("0-50 qati:",w50_fosfor_process_end)
                    self.lineEdit_10.setText(str(w50_fosfor_process_end[0]))
                    self.lineEdit_9.setText("0")

                if self.comboBox_2.currentText() == "Yox":
                    self.lineEdit_8.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")

                if self.comboBox_3.currentText() == "Var":
                    for s in w3_Kalium:
                        k = w3_Kalium.index(s)
                        w3_kalium_index.append(k)
                    r = w3_kalium_index[0]
                    w20_2_index_kalium.append(r)
                    for s in w20_2_index_kalium:
                        w = w3_Kalium[s]
                        w20_kalium_process_end.append(w)
                    print("0-20 qati:",w20_kalium_process_end)
                    self.lineEdit_11.setText(str(w20_kalium_process_end[0]))


                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_kalium[s]
                        q = round(q,2)
                        w50_kalium_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_kalium[0]
                    k = round(k,2)
                    w50_kalium_process_end.append(k)
                    total_50 = sum(w50_kalium_process_end)
                    Total_50_sum_kalium.append(total_50)
                    process_end_kalium_50_tam = sum(Total_50_sum_kalium)
                    process_end_kalium_50_tam = round(process_end_kalium_50_tam,2)
                    process_end_kalium_50_tam_proccesEnd = process_end_kalium_50_tam/50
                    process_end_kalium_50_tam_proccesEnd = round(process_end_kalium_50_tam_proccesEnd,2)
                    w50_kalium_process_end.clear()
                    w50_kalium_process_end.append(process_end_kalium_50_tam_proccesEnd)
                    print("0-50 qati:",w50_kalium_process_end)
                    self.lineEdit_13.setText(str(w50_kalium_process_end[0]))
                    self.lineEdit_12.setText("0")

                if self.comboBox_3.currentText() == "Yox":
                    self.lineEdit_11.setText("0")
                    self.lineEdit_13.setText("0")
                    self.lineEdit_12.setText("0")

            if min(w2)>20 and max(w2)>90 and len(w2)>len(w3_humus):
            ################# 0-20 ############################
                try:
                    for s in w3_humus:
                        k = w3_humus.index(s)
                        w3_humus_index.append(k)
                    r = w3_humus_index[0]
                    w20_2_index.append(r)
                    for s in w20_2_index:
                        w = w3_humus[s]
                        w_str = str(w)
                        w20_humus_process_end.append(w)
                    self.lineEdit_2.setText(w_str)
                    print("0-20 qati:",w20_humus_process_end)
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")
    ################# 0-20 ############################
    ################# 0-50 qatinin indexlemesi ve melumatlari ############################
                for s in w2:
                    try:
                        s = int(s)
                        if 20 < s <= 50:
                            q=w2.index(s)
                            index_w50.append(q)
                    
                            w50_2.append(s)
                        if 50 < s <= 100:
                            q = w2.index(s)
                            index_w100.append(q)
                            w100_2.append(s)
                    except ValueError:
                        print("Excel melumatlarinda her hansi sutunda reqem melumatindan kenar verilen var!!!") 
    ################# 0-50 qatinin indexlemesi ve melumatlari ############################
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in index_w50:
                    q = w1[s]
                    q = int(q)
                    w50_1.append(q)

                for s in index_w50:
                    q = w3_humus[s]
                    w50_humus.append(q)

                for s in index_w50:
                    q = w3_Azot[s]
                    w50_azot.append(q)

                for s in index_w50:
                    q = w3_Fosfor[s]
                    w50_fosfor.append(q)

                for s in index_w50:
                    q = w3_Kalium[s]
                    w50_kalium.append(q)
    ################### 0-50 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in index_w100:
                    q = w1[s]
                    q = int(q)
                    w100_1.append(q)

                for s in index_w100:
                    q = w3_humus[s]
                    w100_humus.append(q)

                for s in index_w100:
                    q = w3_Azot[s]
                    w100_azot.append(q)

                for s in index_w100:
                    q = w3_Fosfor[s]
                    w100_fosfor.append(q)

                for s in index_w100:
                    q = w3_Kalium[s]
                    w100_kalium.append(q)
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
                for s in w50_2:
                    k = w50_2.index(s)
                    w50_2_index.append(k)


                for s in w100_2:
                    k = w100_2.index(s)
                    w100_2_index.append(k)
    ################### 0-100 qatinin birinci hissesinin ve onlarin humus melumatlari ################################
    ################################ >100 hallari ucun humusun sonuncu qiymetinin cixarilmasi ############################################################
                for s in w3_humus:
                    k = w3_humus.index(s)
                    w3_humus_index.append(k)
                    w3_humus_index_max = max(w3_humus_index)
                    w3_humus_index.clear()
                    w3_humus_index.append(w3_humus_index_max)
                q = w3_humus[w3_humus_index[0]]
                w100_humus_end.append(q)
    ################################ >100 hallari ucun humusun sonuncu qiymetinin cixarilmasi ############################################################
    ################# 0-50 ############################
                try:
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_humus[s]
                        q = round(q,2)
                        w50_humus_process_end.append(q)
                    q = 50-max(w50_2)
                    W100_remain.append(q)
                    k = q*w100_humus[0]
                    k = round(k,2)
                    w50_humus_process_end.append(k)
                    total_50 = sum(w50_humus_process_end)
                    Total_50_sum.append(total_50)
                    process_end_humus_50_tam = sum(Total_50_sum)
                    process_end_humus_50_tam = round(process_end_humus_50_tam,2)
                    process_end_humus_50_tam_proccesEnd = process_end_humus_50_tam/50
                    process_end_humus_50_tam_proccesEnd = round(process_end_humus_50_tam_proccesEnd,2)
                    w50_humus_process_end.clear()
                    w50_humus_process_end.append(process_end_humus_50_tam_proccesEnd)
                    self.lineEdit_3.setText(str(w50_humus_process_end[0]))
                    print("0-50 qati:",w50_humus_process_end)
                except:
                    print("Torpaq qatlarinin melumatlari daxil edilmeyib")


                ################## AZOT 0-20 #########################
                if self.comboBox.currentText() == "Var":
                    for s in w3_Azot:
                        k = w3_Azot.index(s)
                        w3_azot_index.append(k)
                    r = w3_azot_index[0]
                    w20_2_index_azot.append(r)
                    for s in w20_2_index_azot:
                        w = w3_Azot[s]
                        w20_azot_process_end.append(w)
                    self.lineEdit_5.setText(str(w20_azot_process_end[0]))
                    print("0-20 qati:",w20_azot_process_end)
                ################## AZOT 0-20 #########################

                    
                ################## AZOT 0-50 #########################
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_azot[s]
                        q = round(q,2)
                        w50_azot_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_azot[0]
                    k = round(k,2)
                    w50_azot_process_end.append(k)
                    total_50 = sum(w50_azot_process_end)
                    Total_50_sum_azot.append(total_50)
                    process_end_azot_50_tam = sum(Total_50_sum_azot)
                    process_end_azot_50_tam = round(process_end_azot_50_tam,2)
                    process_end_azot_50_tam_proccesEnd = process_end_azot_50_tam/50
                    process_end_azot_50_tam_proccesEnd = round(process_end_azot_50_tam_proccesEnd,2)
                    w50_azot_process_end.clear()
                    w50_azot_process_end.append(process_end_azot_50_tam_proccesEnd)
                    self.lineEdit_7.setText(str(w50_azot_process_end[0]))
                    self.lineEdit_6.setText("0")
                    print("0-50 qati:",w50_azot_process_end)
                ################## AZOT 0-50 ######################### 

                if self.comboBox.currentText() == "Yox":
                    self.lineEdit_5.setText("0")
                    self.lineEdit_7.setText("0")
                    self.lineEdit_6.setText("0")

            ################## FOSFOR 0-20 #########################
                if self.comboBox_2.currentText() == "Var":
                    for s in w3_Fosfor:
                        k = w3_Fosfor.index(s)
                        w3_fosfor_index.append(k)
                    r = w3_fosfor_index[0]
                    w20_2_index_fosfor.append(r)
                    for s in w20_2_index_fosfor:
                        w = w3_Fosfor[s]
                        w20_fosfor_process_end.append(w)
                    self.lineEdit_8.setText(str(w20_fosfor_process_end[0]))
                    print("0-20 qati:",w20_fosfor_process_end)
                ################## FOSFOR 0-20 #########################

                    
                ################## FOSFOR 0-50 #########################
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_fosfor[s]
                        q = round(q,2)
                        w50_fosfor_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_fosfor[0]
                    k = round(k,2)
                    w50_fosfor_process_end.append(k)
                    total_50 = sum(w50_fosfor_process_end)
                    Total_50_sum_fosfor.append(total_50)
                    process_end_fosfor_50_tam = sum(Total_50_sum_fosfor)
                    process_end_fosfor_50_tam = round(process_end_fosfor_50_tam,2)
                    process_end_fosfor_50_tam_proccesEnd = process_end_fosfor_50_tam/50
                    process_end_fosfor_50_tam_proccesEnd = round(process_end_fosfor_50_tam_proccesEnd,2)
                    w50_fosfor_process_end.clear()
                    w50_fosfor_process_end.append(process_end_fosfor_50_tam_proccesEnd)
                    self.lineEdit_10.setText(str(w50_fosfor_process_end[0]))
                    self.lineEdit_9.setText("0")
                    print("0-50 qati:",w50_fosfor_process_end)
                ################## FOSFOR 0-50 ######################### 

                if self.comboBox_2.currentText() == "Yox":
                    self.lineEdit_8.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")

                ################## FOSFOR 0-20 #########################
                if self.comboBox_3.currentText() == "Var":
                    for s in w3_Kalium:
                        k = w3_Kalium.index(s)
                        w3_kalium_index.append(k)
                    r = w3_kalium_index[0]
                    w20_2_index_kalium.append(r)
                    for s in w20_2_index_kalium:
                        w = w3_Kalium[s]
                        w20_kalium_process_end.append(w)
                    self.lineEdit_11.setText(str(w20_kalium_process_end[0]))
                    print("0-20 qati:",w20_kalium_process_end)
                ################## KALIUM 0-20 #########################

                    
                ################## FOSFOR 0-50 #########################
                    for s in w50_2_index:
                        q = (w50_2[s]-w50_1[s])*w50_kalium[s]
                        q = round(q,2)
                        w50_kalium_process_end.append(q)
                    q = 50-max(w50_2)
                    k = q*w100_kalium[0]
                    k = round(k,2)
                    w50_kalium_process_end.append(k)
                    total_50 = sum(w50_kalium_process_end)
                    Total_50_sum_kalium.append(total_50)
                    process_end_kalium_50_tam = sum(Total_50_sum_kalium)
                    process_end_kalium_50_tam = round(process_end_kalium_50_tam,2)
                    process_end_kalium_50_tam_proccesEnd = process_end_kalium_50_tam/50
                    process_end_kalium_50_tam_proccesEnd = round(process_end_kalium_50_tam_proccesEnd,2)
                    w50_kalium_process_end.clear()
                    w50_kalium_process_end.append(process_end_kalium_50_tam_proccesEnd)
                    self.lineEdit_13.setText(str(w50_kalium_process_end[0]))
                    self.lineEdit_12.setText("0")
                    print("0-50 qati:",w50_kalium_process_end)
                ################## FOSFOR 0-50 ######################### 

                if self.comboBox_3.currentText() == "Yox":
                    self.lineEdit_11.setText("0")
                    self.lineEdit_13.setText("0")
                    self.lineEdit_12.setText("0")
                
    ################# 0-50 ############################
        except:
            self.textBrowser.setText("""Xəta baş verdi! Xətanın baş verməsinin 4 səbəi ola bilər:\n1) Excel Fayılının yolu daxil edilməmişdir\n2) Göstərdiyiniz fayıl Excel fayılı deyildir\n3) Excel fayılının Sturukturu standarta uyğun hazırlanmayıb\n4) Proqram parametrlərini excel fayılınıza uyğun təyin etməmisiz (Məsəslən Excelde Fosfor məlumatı yoxdur lakin siz var kimi təyin etmisiz)""")
            print("Fayilin yolunu gosterin!!!")
    def Send(self):
        con = sqlite3.connect(r"C:\Users\umaro\OneDrive\Desktop\DatabaseD.db")
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS DatabaseD(Torpaq_adi TEXT,Torpaq_Yarım_Tipi TEXT, Humus_20 INT, Humus_50 INT, Humus_100 INT, Azot_20 INT,Azot_50 INT,Azot_100 INT,
Fosfor_20 INT, Fosfor_50 INT,Fosfor_100 INT,Kalium_20 INT,Kalium_50 INT,Kalium_100 INT)""")
        Humus_20 = self.lineEdit_2.text()
        Humus_50 = self.lineEdit_3.text()
        Humus_100 = self.lineEdit_4.text()

        Azot_20 = self.lineEdit_5.text()
        Azot_50 = self.lineEdit_7.text()
        Azot_100 = self.lineEdit_6.text()

        Fosfor_20 = self.lineEdit_8.text()
        Fosfor_50 = self.lineEdit_10.text()
        Fosfor_100 = self.lineEdit_9.text()

        Kalium_20 = self.lineEdit_11.text()
        Kalium_50 = self.lineEdit_13.text()
        Kalium_100 = self.lineEdit_12.text()
        cursor.execute("""INSERT INTO DatabaseD(Torpaq_adi,Torpaq_Yarım_Tipi,Humus_20,Humus_50,Humus_100,Azot_20,Azot_50,Azot_100,
Fosfor_20,Fosfor_50,Fosfor_100,Kalium_20,Kalium_50,Kalium_100) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (self.comboBox_5.currentText(),self.comboBox_6.currentText(),Humus_20,Humus_50, Humus_100,
                                                                                                      Azot_20,Azot_50,Azot_100,Fosfor_20,Fosfor_50,Fosfor_100,
                                                                                                      Kalium_20,Kalium_50,Kalium_100))
        con.commit()
            





def window():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    window()

