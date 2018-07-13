#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:14:16 2018

@author: caseygoldstein
"""

import songmatch

def addfingerprintstodatabase (fingerprints, song_id):
    for i in range(len(fingerprints)):
        holderfingerprint = fingerprints[i]
        songmatch.songDatabase[holderfingerprint[0]] = (song_id, holderfingerprint[1])
    
        
        
        