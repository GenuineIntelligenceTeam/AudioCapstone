#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:14:16 2018

@author: caseygoldstein
"""
printToSong = {}
def addfingerprintstodatabase (fingerprints, song_id):
    for i in range(len(fingerprints)):
        holderfingerprint = fingerprints[i]
        printToSong[holderfingerprint[0]] = (song_id, holderfingerprint[1])
    print(printToSong)
        
        
        