#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:37:58 2018

@author: caseygoldstein
"""

import pandas as pd

songbase = ['3005 - Childish Gambino',
'Ain’t No Mountain High Enough - Marvin Gaye',
'Another Brick in the Wall (Part II)  - Pink Floyd',
'Comfortably Numb - Pink Floyd',
'Dangerously - Charlie Puth',
'Hive Knight - Hollow Nights',
'Lose my Soul - Toby Mac',
'Mantis Lords - Hollow Nights',
'Mystic Rhythms - Rush',
'Pink Panther Theme Song',
'Resting Grounds - Hollow Nights',
'Say You Won’t Let Go - James Arthur',
'Sound of the Shire - Lord of the Rings',
'Take Me Home, Country Roads - John Denver',
'The Happy Song - Pharrell',
'Walk on Water - Britt Nicole',
'We Don’t Talk Anymore - Charlie Puth',
'XX Intro - XX']

print(songbase)

songFrame = pd.DataFrame(songbase)

print(songFrame)