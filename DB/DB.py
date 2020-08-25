#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:36:16 2018

@author: unixuser
"""

import sqlite3

class DataBase:
    def __init__(self):
        #CHANGE LOCATION /home/unixuser/Main_Form/DB/Journal.db ACCORDINGLY
        self.database = sqlite3.connect(r'F:\Program Files\Microsoft Visual Studio\Projects\PerDia\DB\Journal.db') 
        self.cursor = self.database.cursor()
        self.createDBs()
    
    def createDBs(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                name text,
                pin text
                )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS entry (
                date text,
                texts text,
                tags text,
                photos text
                )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS date (
                date text
                )""")

    def getPIN(self,name):
        pin = self.database.execute("SELECT pin FROM user WHERE  name = (:name)",{'name':name})
        for row in pin:
            pin = row[0]
        return pin
    
    def updatePIN(self,name,newPIN):
        self.cursor.execute("UPDATE user SET pin = (:newPIN) WHERE  name = (:name)",{'newPIN':newPIN, 'name':name})
        self.database.commit()

#    def addDataDate(self, date,text,tags,photos):
#        self.cursor.execute("SELECT * FROM date WHERE date = (:date)",{'date':date})
#        data = self.cursor.fetchall()
#        if len(data) != 0:
#            print ('existing')
#        else:
#            self.cursor.execute("INSERT INTO date VALUES (:date)",{'date':date})
#            self.database.commit()
#            self.addDataEntry(date,text,tags,photos)
#            print ('non-existing')

    
    def addDataEntry(self,date,text,tags,photos):
        self.cursor.execute("SELECT * FROM date WHERE date = (:date)",{'date':date})
        data = self.cursor.fetchall()
        if len(data) != 0:
            print ('existing')
        else:
            self.cursor.execute("INSERT INTO date VALUES (:date)",{'date':date})
            self.cursor.execute("INSERT INTO entry VALUES (:date, :texts, :tags, :photos)",{'date':date,'texts':text,'tags':tags,'photos':photos})
            self.database.commit()
    
    def delDataDate(self,date):
        self.cursor.execute("SELECT * FROM date WHERE date = (:date)",{'date':date})
        data = self.cursor.fetchall()
        if len(data) != 0:
            self.cursor.execute("DELETE FROM date WHERE date = (:date)",{'date':date})
            self.cursor.execute("DELETE FROM entry WHERE date = (:date)",{'date':date})
            self.database.commit()
        else:
            print ('nonexisting')
    
    def updateEntryText(self,date,newText):
        self.cursor.execute("SELECT * FROM date WHERE date = (:date)",{'date':date})
        data = self.cursor.fetchall()
        if len(data) != 0:
            self.cursor.execute("UPDATE entry SET text = (:newText)  WHERE date = (:date)",{'newText':newText,'date':date})
            self.database.commit()
        else:
            print ('nonexisting')    

    def updateEntryTags(self,date,newTags):
        self.cursor.execute("SELECT * FROM date WHERE date = (:date)",{'date':date})
        data = self.cursor.fetchall()
        if len(data) != 0:
            self.cursor.execute("UPDATE entry SET tags = (:newTags)  WHERE date = (:date)",{'newTags':newTags,'date':date})
            self.database.commit()
        else:
            print ('nonexisting')   

    def updateEntryPhotos(self,date,newPhotos):
        self.cursor.execute("SELECT * FROM date WHERE date = (:date)",{'date':date})
        data = self.cursor.fetchall()
        if len(data) != 0:
            self.cursor.execute("UPDATE entry SET photos = (:newPhotos)  WHERE date = (:date)",{'newPhotos':newPhotos,'date':date})
            self.database.commit()
        else:
            print ('nonexisting')   

    def getData(self,date):
        self.cursor.execute("SELECT * FROM date WHERE date = (:date)",{'date':date})
        data = self.cursor.fetchall()
        if len(data) != 0:
            data = self.database.execute("SELECT text, tags, photos FROM entry WHERE  date = (:date)",{'date':date})
            for row in data:
                text = row[0]
                tags = row[1]
                photos = row[2]
            values = [text,tags,photos]
            return values
        else:
            print ('nonexisting')

    def getDates(self):
        dates = self.database.execute("SELECT date FROM date")
        vals = list(sum(dates,()))
        return vals


if __name__ == '__main__':
    database = DataBase()
    print (database.getData('Mar 18 2018'))
    


    

        