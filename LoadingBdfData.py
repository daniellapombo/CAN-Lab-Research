# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:03:36 2020

@author: danie
"""

import mne
import os
import numpy as np

#PID: 103
filename = 'C:\\Users\\danie\\Documents\\School\\CAN Lab\\103\\141176103_122.bdf'
raw = mne.io.read_raw_bdf(filename, preload = True)

print(raw)
print(raw.info)

f  = open('SID103Info.txt', 'w')
f.write(str(raw))
print(raw, file = f)
print(raw.info, file = f)
f.close