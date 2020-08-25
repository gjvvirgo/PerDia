#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:03:10 2018

@author: unixuser
"""
import sys
sys.path.insert(0,'/home/chavez/Downloads/PerDia/DB')
from DB import DataBase

from Entry_Class import Entry

class Date:
    
    def __init__(self,selected_date):
        self.day = selected_date
        self.database = DataBase()
        self.slot = True
    
    def createEntry(self,txt,tgs,phts):
        entry = Entry(self.day,'new')
        entry.addText(txt)
        word = tgs.split()
        entry.addTag(word,False)
        entry.addPhoto(phts,False)
        entry.storeValues('new')
        
    
    def dateAvailability(self):
        if self.day in self.database.getDates():
            return True
        else:
            return False

    def deleteEntry(self):
        self.database.delDataDate(self.day)
    
    def sendData(self,getWhat):
        entry = Entry(self.day,'old')
        if getWhat == 'getTexts':
            return entry.editText('getTexts')
        elif getWhat == 'getTags':
            return entry.editText('getTags')
        elif getWhat == 'getPhotos':
            return entry.editText('getPhotos')
    
    def editEntry(self,txt,tgs,phts):
        entry = Entry(self.day,'old')
        entry.addText(txt)
        word = tgs.split()
        entry.addTag(word,True)
        entry.addPhoto(phts,True)
        entry.storeValues('old')
        
#    def viewEntry(self):
#        entry = Entry(self.day)
if __name__ == '__main__':
    sample = Date('Mar 18 2018')
    print (sample.sendData('getPhotos'))
    
        
        