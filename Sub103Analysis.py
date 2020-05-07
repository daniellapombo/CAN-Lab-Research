# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:17:15 2020


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

Objective: on a micro scale, process subject data by applying various filters, 
data segmentation and feature selection methods

Goal: create preprocessed data comprised of soley the subject's resting state, 
default mode network EEG data for eyes closed (Need to clarify if want eyes closed or open)

Procedure:
    1. Import Data
    2. Establish Montage
    3. Port Code Interpretation
    4. Data selection and filtering
        a. Default Mode Network
        b. Eye blink removal
    5. Power Spectrum Analysis

Refer to https://docs.google.com/presentation/d/1KgqIV7h4On8QL0ae-ZGp_TLPF9DS60skc1tUxqWO8dc/edit?usp=sharing
for further information in regards to the code and analysis
"""

#PID: 103
filename = 'C:\\Users\\danie\\Documents\\School\\CAN Lab\\103\\141176103_122.bdf'
raw = mne.io.read_raw_bdf(filename, preload = True)

#print(raw)
#print(raw.info)
#print(raw.info["chs"])
#print(raw.info["ch_names"])


print(mne.channels.get_builtin_montages()) #Print out all built in montages
montage = mne.channels.make_standard_montage("standard_alphabetic")
montage.plot()
