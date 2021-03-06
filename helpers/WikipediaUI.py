# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WikipediaUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup
import requests
import html5lib
import mysql.connector as msql
import yaml
db = yaml.load(open('db.yaml'))
user=db['user']
password=db['password']



class Ui_Wikipedia(object):
    def setupUi(self, Wikipedia):
        Wikipedia.setObjectName("Wikipedia")
        Wikipedia.resize(985, 509)
        Wikipedia.setStyleSheet("background-color: #2C3336;\n"
"font: 63 12pt \"Nunito\";")
        self.centralwidget = QtWidgets.QWidget(Wikipedia)
        self.centralwidget.setObjectName("centralwidget")
        self.wiki = QtWidgets.QLabel(self.centralwidget)
        self.wiki.setGeometry(QtCore.QRect(360, 40, 271, 41))
        self.wiki.setStyleSheet("color: cyan;\n"
"font: 81 24pt \"Nunito ExtraBold\";\n"
"")
        self.wiki.setObjectName("wiki")
        self.Wikiquery = QtWidgets.QLineEdit(self.centralwidget)
        self.Wikiquery.setGeometry(QtCore.QRect(310, 120, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Wikiquery.setFont(font)
        self.Wikiquery.setStyleSheet("border-radius:10px;\n"
"background-color: white;")
        self.Wikiquery.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Wikiquery.setClearButtonEnabled(False)
        self.Wikiquery.setObjectName("Wikiquery")
        self.Wikigo = QtWidgets.QPushButton(self.centralwidget)
        self.Wikigo.setGeometry(QtCore.QRect(590, 120, 81, 31))
        self.Wikigo.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.Wikigo.setObjectName("Wikigo")
        self.wikiresult = QtWidgets.QTextBrowser(self.centralwidget)
        self.wikiresult.setGeometry(QtCore.QRect(80, 210, 721, 271))
        self.wikiresult.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Nunito Black\";\n"
"border-radius: 10px;")
        self.wikiresult.setObjectName("wikiresult")
        self.WIkisavedata = QtWidgets.QPushButton(self.centralwidget)
        self.WIkisavedata.setGeometry(QtCore.QRect(820, 230, 141, 31))
        self.WIkisavedata.setStyleSheet("border-radius:10px;\n"
"font: 75 11pt \"Nunito\";\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.WIkisavedata.setObjectName("WIkisavedata")
        self.Wikisavetext = QtWidgets.QPushButton(self.centralwidget)
        self.Wikisavetext.setGeometry(QtCore.QRect(820, 270, 141, 31))
        self.Wikisavetext.setStyleSheet("border-radius:10px;\n"
"font: 75 11pt \"Nunito\";\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.Wikisavetext.setObjectName("Wikisavetext")
        Wikipedia.setCentralWidget(self.centralwidget)

        self.retranslateUi(Wikipedia)
        QtCore.QMetaObject.connectSlotsByName(Wikipedia)

        self.Wikigo.clicked.connect(self.wikiProject)
        self.Wikisavetext.clicked.connect(self.wikitextsave)
        self.WIkisavedata.clicked.connect(self.wikidata)
    def wikiProject(self):
        try:
            input = self.Wikiquery.text()
            ads=input
            if len(input) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Zero Input Error")
                msg.setInformativeText("Type something to search")
                msg.setWindowTitle('Error')
                msg.exec_()
            else:
                r=requests.get('https://en.wikipedia.org/wiki/{}'.format(input))
                so=BeautifulSoup(r.content,'html5lib')
                title=so.find("h1",class_="firstHeading").getText()
                p=so.find_all("p")[2].getText()
                s=so.find('table',class_="infobox")
                f=s.find('tbody')
                one=s.find_all('tr')[1]
                oneo=one.find('th').getText()
                onet=one.find('td').getText()
                two=s.find_all('tr')[5]
                twoo=two.find('th').getText()
                twot=two.find('td').getText()
                three=s.find_all('tr')[6]
                threeo=three.find('th').getText()
                threet=three.find('td').getText()
                four=s.find_all('tr')[7]
                fouro=four.find('th').getText()
                fourt=four.find('td').getText()
                five=s.find_all('tr')[8]
                fiveo=five.find('th').getText()
                fivet=five.find('td').getText()
                six=s.find_all('tr')[9]
                sixo=six.find('th').getText()
                sixt=six.find('td').getText()
                wiki=title+"\n"+"___________"+"\n"+p+"___________"+"\n"+oneo+"--"+onet+"\n"+twoo+"--"+twot+"\n"+threeo+"--"+threet+"\n"+fouro+"--"+fourt+"\n"+fiveo+"--"+fivet+"\n"+sixo+"--"+sixt+"\n"+"_____________"
                self.wikiresult.append(str(wiki))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("An erro roccured")
            msg.setInformativeText("Check your spelling and try again")
            msg.setWindowTitle('Error')
            msg.exec_()
            
            
    def wikitextsave(self):
        s="../txtfiles/"+self.Wikiquery.text()+".txt"
        fd=open(s,'w',encoding='utf-8')
        fd.write(self.wikiresult.toPlainText())
        fd.close()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("File Succesfully saved")
        msg.setInformativeText("FIle saved as "+s)
        msg.setWindowTitle('Saved')
        msg.exec_()
    def wikidata(self):
        if con.is_connected():
           cur=con.cursor()
           n=self.wikiresult.toPlainText()
           l=(n,)
           k=("insert into checking (info) values(%s)")
           cur.execute(k,l)
           con.commit()
           msg = QMessageBox()
           msg.setIcon(QMessageBox.Information)
           msg.setText("Data saved succesfully in database")
           msg.setInformativeText("Data")
           msg.setWindowTitle('Saved')
           msg.exec_()
           

        else:
            print('connection error')

        
        
    def retranslateUi(self, Wikipedia):
        _translate = QtCore.QCoreApplication.translate
        Wikipedia.setWindowTitle(_translate("Wikipedia", "Wikipedia"))
        self.wiki.setText(_translate("Wikipedia", "Wikipedia Search"))
        self.Wikiquery.setText(_translate("Wikipedia", ""))
        self.Wikiquery.setPlaceholderText(_translate("Wikipedia", "                        Search here"))
        self.Wikigo.setText(_translate("Wikipedia", "GO"))
        self.WIkisavedata.setText(_translate("Wikipedia", "Save to database"))
        self.Wikisavetext.setText(_translate("Wikipedia", "Save as text file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wikipedia = QtWidgets.QMainWindow()
    ui = Ui_Wikipedia()
    ui.setupUi(Wikipedia)
    Wikipedia.show()
    sys.exit(app.exec_())
