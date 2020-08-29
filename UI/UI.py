#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:59:47 2018

@author: unixuser
"""

from PyQt5 import QtWidgets, QtGui, QtCore, uic

import sys
sys.path.insert(0,r'.\BL')

from BL import bLogic

logic = bLogic()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi(r'.\UI\mainwindow.ui',self)
        self.setFixedSize(self.size())
        self.lineEdit.setMaxLength(4)
        self.pushButton.clicked.connect(self.showCalendar)
        
    def showCalendar(self):
        self.child_win=CalendarWindow()
        num = self.lineEdit.text()
        if num == '':
            self.showDialog('Some fields are left blank, parang tayo','Error </3')
            return
        try:
            num = int(num)
        except:
            self.showDialog("Pins are only in numerical form!","Error.")
            return
        else:
            if logic.verifyPin(self.lineEdit.text()) == True:
                self.hide()
                self.lineEdit.setText('')
                self.child_win.exec_()
                self.show()
            else:
                self.showDialog('Incorret PIN','ERROR')
        
    def showDialog(self,err_mes,header):
        self.error = QtWidgets.QMessageBox()
        self.error.setText(err_mes)
        self.error.setWindowTitle(header)
        self.error.exec_()
        
class CalendarWindow(QtWidgets.QDialog):
    def __init__(self):
        super(CalendarWindow,self).__init__()
        uic.loadUi(r'.\UI\calendar.ui',self)
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.createEntry)
        self.pushButton_3.clicked.connect(self.viewEntry)
        self.pushButton_2.clicked.connect(self.editEntry)
        self.pushButton_4.clicked.connect(self.changePin)
        self.dateEdit.setDisplayFormat('MMM d yyyy')
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
        self.dateEdit.dateChanged.connect(self.changeCalendarWidget)
        self.calendarWidget.selectionChanged.connect(self.currentDateSetter)
    
    def changePin(self):
        self.child_win=ChangePinWindow()     
        self.child_win.exec_()
        self.child_win.destroy()
    
    def changeCalendarWidget(self):
        self.calendarWidget.setSelectedDate(self.dateEdit.date())
    
    def currentDateSetter(self):
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
    
    def showDialog(self,err_mes,header):
        self.error = QtWidgets.QMessageBox()
        self.error.setText(err_mes)
        self.error.setWindowTitle(header)
        self.error.exec_()
        
    def createEntry(self):
        if logic.checkDate(self.dateEdit.date().toString('MMM d yyyy')) == True:
            self.showDialog('Date already occupied!','Error')
            return
        else:
            self.child_win=EntryWindow(self.dateEdit.date().toString('MMM d yyyy'))
            self.child_win.exec_()
            #self.child_win.destroy()
        
    def viewEntry(self):
        if logic.checkDate(self.dateEdit.date().toString('MMM d yyyy')) == True:
            self.child_win=ViewWindow(self.dateEdit.date().toString('MMM d yyyy'))
            self.child_win.exec_()
            #self.child_win.destroy()
        else:
            self.showDialog('No entry found..','Error')
            return
    
    def editEntry(self):
        if logic.checkDate(self.dateEdit.date().toString('MMM d yyyy')) == True:
            self.child_win=EditWindow(self.dateEdit.date().toString('MMM d yyyy'))
            self.child_win.exec_()
           # self.child_win.destroy()
        else:
            self.showDialog('No entry found..','Error')
            return
        
class ChangePinWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ChangePinWindow,self).__init__()
        uic.loadUi(r'.\UI\changepin.ui',self)
        self.lineEdit.setMaxLength(4)
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_3.setMaxLength(4)
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.changePinLogic)
    
    def changePinLogic(self):
        old = self.lineEdit.text()
        new = self.lineEdit_2.text()
        veri = self.lineEdit_3.text()
        
        if old == '' or new == '' or veri == '':
            self.showDialog('Some fields are left blank, parang tayo','Error </3')
            return
        try:
            old = int(old)
        except:
            self.showDialog("Pins are only in numerical form!","Error.")
            return
        else:
            old = self.lineEdit.text() 
        
        try:
            new = int(new)
        except:
            self.showDialog("Pins are only in numerical form!","Error.")
            return
        else:
            new = self.lineEdit_2.text()
        
        try:
            veri = int(veri)
        except:
            self.showDialog("Pins are only in numerical form!","Error.")
            return
        else:
            veri = self.lineEdit_3.text()
        if logic.changeP(old,new,veri) == 0:
            self.showDialog('PIN Successfully Changed!','Success')
            self.close()
            
        elif logic.changeP(old,new,veri) == 1:
            self.showDialog('PIN did not match!','Error')
        else:
            self.showDialog('Old PIN incorrect!','Error')
    
    def showDialog(self,err_mes,header):
        self.error = QtWidgets.QMessageBox()
        self.error.setText(err_mes)
        self.error.setWindowTitle(header)
        self.error.exec_()
        
class EntryWindow(QtWidgets.QDialog):
    def __init__(self,curr_date):
        super(EntryWindow,self).__init__()
        uic.loadUi(r'.\UI\entry.ui',self)
        self.setFixedSize(self.size())
        self.sel_date = curr_date
        self.photos = None
        self.pushButton.clicked.connect(self.createLogic)
        self.pushButton_2.clicked.connect(self.addPhotoLogic)
        
    def createLogic(self):
        text = self.plainTextEdit.toPlainText()
        if text == '':
            self.showDialog('Entry cannot be empty!','Error')
            return
        tags = self.lineEdit.text()
        
        try: 
            logic.createE(self.sel_date,text,tags,self.photos)
        except:
            logic.createE(self.sel_date,text,tags,None)

        self.showDialog('Entry Successfully Create!','Success!')
        self.close()
    
    def addPhotoLogic(self):
        self.photos = QtWidgets.QFileDialog.getOpenFileNames(None,"Open Image", r".\Sample Pictures", "Image Files (*.jpeg *.jpg)")
        if len(self.photos[0]) != 0:
            self.showDialog('Photo(s) Added!','Success')
                
    def showDialog(self,err_mes,header):
        self.error = QtWidgets.QMessageBox()
        self.error.setText(err_mes)
        self.error.setWindowTitle(header)
        self.error.exec_()
            
class ViewWindow(QtWidgets.QDialog):
    def __init__(self,curr_date):
        super(ViewWindow,self).__init__()
        uic.loadUi(r'.\UI\view.ui',self)
        self.sel_date = curr_date
        self.setFixedSize(self.size())
        self.setWindowTitle(curr_date)
        self.plainTextEdit.appendPlainText(logic.viewEnt(curr_date,'getTexts'))
        self.lineEdit.setText(logic.viewEnt(curr_date,'getTags'))
        self.pushButton_2.clicked.connect(self.showViewPhotos)
        self.pushButton.clicked.connect(self.deleteEntry)
        
    def showDialog(self,err_mes,header):
        self.error = QtWidgets.QMessageBox() 
        self.error.setText(err_mes)
        self.error.setWindowTitle(header)
        self.error.exec_()
        return

    def showViewPhotos(self):
        self.child_win=ViewPhotosWindow(self.sel_date,0)     
        self.child_win.exec_()
        self.child_win.destroy() 
    
    def deleteEntry(self):
        logic.deleteD()
        self.showDialog('Entry Deleted!',"Success!")
        self.close()

class ViewPhotosWindow(QtWidgets.QDialog):
    def __init__(self,curr_date,inx):
        super(ViewPhotosWindow,self).__init__()
        uic.loadUi(r'.\UI\viewphotos.ui',self)
        self.setFixedSize(self.size())
        
        if inx == 0:
            self.indx = 0
            self.fname = logic.viewEnt(curr_date,'getPhotos')
            print (self.fname)
            print (self.indx)
            self.pixmap = QtGui.QPixmap(self.fname[self.indx])
            self.pixmap_rz = self.pixmap.scaled(471,291, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmap_rz)
            inx = 1

        self.pushButton.clicked.connect(self.previousBtn)
        self.pushButton_2.clicked.connect(self.nextBtn)
            
    
    def nextBtn(self):
        self.indx = self.indx + 1
        print (self.indx)
        if self.indx >= len(self.fname):
            self.indx = len(self.fname) - 1
            print (self.indx)
            self.pixmap = QtGui.QPixmap(self.fname[self.indx])
            self.pixmap_rz = self.pixmap.scaled(471,291, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmap_rz)
        else:
            print (self.indx)
            self.pixmap = QtGui.QPixmap(self.fname[self.indx])
            self.pixmap_rz = self.pixmap.scaled(471,291, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmap_rz)
    
    def previousBtn(self):
        self.indx = self.indx - 1
        if self.indx <= 0:
            self.indx = 0
            print (self.indx)
            self.pixmap = QtGui.QPixmap(self.fname[self.indx])
            self.pixmap_rz = self.pixmap.scaled(471,291, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmap_rz)
        else:
            print (self.indx)
            self.pixmap = QtGui.QPixmap(self.fname[self.indx])
            self.pixmap_rz = self.pixmap.scaled(471,291, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmap_rz)  
    
class EditWindow(QtWidgets.QDialog):
    def __init__(self,curr_date):
        super(EditWindow,self).__init__()
        uic.loadUi(r'.\UI\edit.ui',self)
        self.setFixedSize(self.size())
        self.sel_date = curr_date
        self.setFixedSize(self.size())
        self.setWindowTitle(curr_date)
        self.plainTextEdit.appendPlainText(logic.viewEnt(curr_date,'getTexts'))
        self.lineEdit.setText(logic.viewEnt(curr_date,'getTags'))
        self.photos = logic.viewEnt(curr_date,'getPhotos')
        self.pushButton.clicked.connect(self.editEntryLogic)
        self.pushButton_2.clicked.connect(self.addPhotoLogic)
        self.pushButton_3.clicked.connect(self.removePhotoLogic)
        
    def showDialog(self,err_mes,header):
        self.error = QtWidgets.QMessageBox()
        self.error.setText(err_mes)
        self.error.setWindowTitle(header)
        self.error.exec_()
        return
    
    def removePhotoLogic(self):
        self.photos = None
        self.showDialog('All photos have been removed','Success!')
        
    def addPhotoLogic(self):
        self.photos = QtWidgets.QFileDialog.getOpenFileNames(None,"Open Image", r'.\Sample Pictures', "Image Files (*.jpeg *.jpg)")
        if len(self.photos[0]) != 0:
            self.showDialog('Photo(s) Added!','Success')
        else:
            self.photos = logic.viewEnt(self.sel_date,'getPhotos')
    
    def editEntryLogic(self):
        text = self.plainTextEdit.toPlainText()
        if text == '':
            self.showDialog('Entry cannot be empty!','Error')
            return

        tags = self.lineEdit.text()
        logic.editE(self.sel_date,text,tags,self.photos)
            
        self.showDialog('Entry Successfully Edited!','Success!')
        self.close()
        return

#if __name__ == '__main__':
#    import sys
#    logic = bLogic()
#    app = QtWidgets.QApplication(sys.argv)
#    mainwindow = MainWindow()
#    mainwindow.show()
#    sys.exit(app.exec_())
