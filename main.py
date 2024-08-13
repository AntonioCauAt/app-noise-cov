# set up environment
import os
import json
import mne

import numpy as np


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)
    
# Read the meg file
epochs = config.pop('fname')
# Read in the epochs file
epo = mne.read_epochs(epochs)