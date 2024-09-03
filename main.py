# Evoked is a datatype that contains the result of averaging an Epochs structure based on several criteria.
import mne
import json
import os
import numpy as np
import matplotlib.pyplot as plt

#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)


# == CONFIG PARAMETERS ==
fname_epochs = config['epochs']




# Read the epochs file
epo = mne.read_epochs(fname_epochs)  

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

'''
# SAVE FIGURE: Create and save a fig of the covariance matrix
fig = mne.viz.plot_cov(noise_cov, epo.info)
fig_fname = os.path.join('out_figs', 'noise_cov.png')
fig.savefig(fig_fname)
'''
# SAVE REPORT: Create and save a report that includes the previous figure
report = mne.Report(title='Report')
report.add_figs_to_section(fig, 'Noise Covariance', section='Covariance')
report_path = os.path.join('out_dir_report', 'report.html')
report.save(report_path, overwrite=True)





