#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:14:16 2018

@author: caseygoldstein
"""
printToSong = {}
def addfingerprintstodatabase (fingerprints):
    for i in range (len(fingerprints)):
        holderfingerprint = fingerprints[i]
        printToSong[holderfingerprint[0]] = (1,holderfingerprint[1])
        
        
        