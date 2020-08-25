#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:14:06 2018

@author: unixuser
"""
import sys
sys.path.insert(0,'/home/chavez/Downloads/PerDia/DB')

from DB import DataBase

class Entry:
    
    def __init__(self,selected_date,status):
    #data hardcode for now, should come from database
        self.database = DataBase()
        self.date = selected_date
        self.photo = []
        self.tag = []
        self.text = None        
        if status == 'old':
            loaded_values = self.database.getData(self.date)
            self.text = loaded_values[0]
            self.tag.extend(loaded_values[1].split(','))
            self.photo.extend(loaded_values[2].split(','))            
    
    def addPhoto(self, loc,isEdit):
        if loc == None:
            self.photo = []
        elif loc != self.photo and isEdit == True:
            self.photo = loc[0]
        elif loc != self.photo and isEdit == False:
            self.photo.extend(loc[0])
            
    
    def addTag(self, tags,isEdit):
        if tags != self.tag and isEdit == False:
            self.tag.extend(tags)
        elif tags != self.tag and isEdit == True:
            self.tag = tags
    
    def addText(self, texts):
        self.text = texts
          
    def editText (self,getWhat):
        if getWhat == 'getTexts':
            return self.text
        elif getWhat == 'getTags':
            return self.tag
        elif getWhat == 'getPhotos':
            return self.photo
    
    def storeValues(self,status):
        if status == 'new':
            joined_tag = ' '.join(self.tag)
            joined_photos = ','.join(self.photo)
            self.database.addDataEntry(self.date,self.text,joined_tag,joined_photos)
        elif status == 'old':
            self.database.updateEntryText(self.date,self.text)
            joined = ' '.join(self.tag)
            self.database.updateEntryTags(self.date,joined)
            joined = ','.join(self.photo)
            self.database.updateEntryPhotos(self.date,joined)

    
    
    
    



        
        