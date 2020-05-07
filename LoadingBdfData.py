# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:03:36 2020

@author: danie associated with the CANLab at Loyola University Chicago
"""
import inspect
import mne
from mne.channels import read_custom_montage
from mne.viz import plot_alignment
import os
import numpy as np
from mne._digitization._utils import _get_fid_coords

"""
CANLab VVE & Aggression Research: 
    
The following processes and analysizes Subject 103 Pre Non Violent Film BDF Data.

Objective: import Subject 103 BDF file and montage

Goal: import and establish a Raw EEG Object with an imported and established montage

Procedure:
    1. Import Data
    2. Establish Montage

Refer to https://docs.google.com/presentation/d/1KgqIV7h4On8QL0ae-ZGp_TLPF9DS60skc1tUxqWO8dc/edit?usp=sharing
for further information in regards to the code and analysis
"""

#PID: 103
filename = 'C:\\Users\\danie\\Documents\\School\\CAN Lab\\103\\141176103_122.bdf'
raw = mne.io.read_raw_bdf(filename, preload = True) #Import bdf file

#Output some of the file information in regards to electrodes, channels, times, etc.
#print(raw)
#print(raw.info)
#print(raw.info["chs"])
#print(raw.info["ch_names"])

#Write file information into a txt file for documentation/record keeping
## the file should contain channel, time information, and etc.
#f  = open('SID103Info.txt', 'w')
#f.write(str(raw))
#print(raw, file = f)
#print(raw.info, file = f)
#f.close

#Analysize all Built-in Montages for similarities w/ research montage
print(mne.channels.get_builtin_montages()) #Print out all built in montages
montage = mne.channels.make_standard_montage("standard_alphabetic")
montage.plot()


#Import and set custom research montage
#dig_montag = read_custom_montage(fname = "C:\\Users\\danie\\Documents\\School\\CAN Lab\\103\\141103_122.sfp")
#dig_montag.plot()


#Analyize source code for montage methods
##Is there a specific area in which has an error/does not work with research SFP and ELP files?
print(inspect.getsource(mne.channels.read_custom_montage))
print(inspect.getsource(_get_fid_coords))

print(_get_fid_coords(dig_montag.dig))
for d in dig_montag.dig:
    print(d['coord_frame'], d['kind'], d['ident'])
    print( d['r'], d['r'].ndim, type(d['r']), len(d['r']))
    print(d)
    print("")

#Attempt another form of importing and setting custom research montage
#digp = mne.channels.read_dig_polhemus_isotrak(fname = "C:\\Users\\danie\\Documents\\School\\CAN Lab\\103\\141103_122.elp")
#digp.plot()


