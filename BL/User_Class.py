#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 23:04:03 2018

@author: unixuser
"""
import sys
sys.path.insert(0,'/home/chavez/Downloads/PerDia/DB')

from DB import DataBase

class User:
    
    def __init__(self):
        self.database = DataBase()
        
    def changePin(self, oldPin, newPin, confirmPin):
        if self.database.getPIN('Hannah Tan') == oldPin:
            if newPin == confirmPin:
                self.database.updatePIN('Hannah Tan',newPin)
                return 0
            else:
                return 1
        else:
            return 2
    
    def verifyLogin(self, inputPin):
        
        if self.database.getPIN('Hannah Tan') == inputPin:
            return True
        else:
            return False
        