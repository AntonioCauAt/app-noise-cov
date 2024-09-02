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

# Read the epochs file
epochs_fname = config.pop('fname') 
epo = mne.read_epochs(epochs_fname)  

# Configuration depending on what we want
epo.pick_types(meg=True, eeg=False)

# Compute noise covariance matrix
noise_cov = mne.compute_covariance(epo, tmax=0.,
                                   method=['shrunk', 'empirical'],
                                   rank='info')
print(noise_cov['method'])

# == SAVE RESULTS ==

# SAVE COVARIANCE MATRIX: Save as .fif
cov_fname = os.path.join('out_dir', 'cov.fif')
mne.write_cov(cov_fname, noise_cov)

# SAVE FIGURE: Create and save a fig of the covariance matrix
fig = mne.viz.plot_cov(noise_cov, epo.info)
fig_fname = os.path.join('out__figs', 'noise_cov.png')
fig.savefig(fig_fname)

# SAVE REPORT: Create and save a report that includes the previous figure
report = mne.Report(title='Report')
report.add_figs_to_section(fig, 'Noise Covariance', section='Covariance')
report_path = os.path.join('out__dir_report', 'report.html')
report.save(report_path, overwrite=True)





