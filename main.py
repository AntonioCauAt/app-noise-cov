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
epochs_fname = config.pop('fname')  
# Read in the epochs file
epo = mne.read_epochs(epochs_fname) 
# since we computed our forward model for MEG only, we drop the EEG channels
# MEEG configuration for true and false
epo.pick_types(meg=True, eeg=False)

# Compute noise covariance matrix
noise_cov = mne.compute_covariance(epo, tmax=0.,
                                   method=['shrunk', 'empirical'],
                                   rank='info')
print(noise_cov['method'])

# == SAVE RESULTS ==

# Opcional: si tienes una solución forward, guárdala
# fwd_fname = os.path.join('out_dir', 'fwd.fif')
# mne.write_forward_solution(fwd_fname, fwd, overwrite=True)

# SAVE FIGURE
fig = mne.viz.plot_cov(noise_cov, epo.info)
fig_fname = os.path.join('out_dir', 'noise_cov.png')
fig.savefig(fig_fname)

# SAVE REPORT
report = mne.Report(title='Report')
report.add_figs_to_section(fig, 'Noise Covariance', section='Covariance')
report_path = os.path.join('out_dir_report', 'report.html')
report.save(report_path, overwrite=True)

