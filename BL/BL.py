#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 19:06:05 2018

@author: unixuser
"""
#import sys
#from PyQt5 import QtCore, QtGui, QtWidgets, uic 
#from UI import MainWindow, CalendarWindow, ChangePinWindow, EntryWindow, ViewWindow
import sys
sys.path.insert(0,r'.\DB')

from User_Class import User
from Date_Class import Date
#from Entry_Class import Entry
user = User()

class bLogic:
    def verifyPin(self,value):
        return user.verifyLogin(value)

    def changeP(self, old, new, veri):
        return user.changePin(old,new,veri)
        
    def createE(self,sel_date,text,tags,photos):
        self.date.createEntry(text,tags,photos)
    
    def deleteD(self):
        self.date.deleteEntry()
    
    def checkDate(self,sel_date):
        self.date = Date(sel_date)
        return self.date.dateAvailability()
    
    def viewEnt(self,sel_date, getWhat):
        self.date = Date(sel_date)
        if getWhat == 'getTexts':
            return self.date.sendData('getTexts')
        elif getWhat == 'getTags':
            tags = self.date.sendData('getTags')
            return ' '.join(str(p) for p in tags)
        elif getWhat == 'getPhotos':
            return self.date.sendData('getPhotos')
    
    def editE(self,sel_date,text,tags,photos):       
        self.date.editEntry(text,tags,photos)
    
    

#if __name__ == '__main__':
#    sample = bLogic()
#    print (sample.viewEnt('Mar 18 2018','getPhotos'))