# Noise Covariance Matrix for MEEG

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes a noise covariance matrix from the pre-stimulus baseline of MEG epochs with MNE-Python compute_covariance and outputs it as cov.fif.**

Reads the epochs, keeps MEG channels only, and estimates the covariance over the baseline (up to time 0) with the shrunk and empirical estimators and rank taken from the measurement info. Use it to obtain the noise covariance needed for MEG source estimation. The current code ignores all parameters (tmin, tmax, projs, method, keep_sample_mean, rank) and uses fixed settings.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/epochs` |
| 📤 **Outputs** | `neuro/meeg/mne/covariance` · `report/html` · `generic/image/png` |
| 🐳 **Container** | `brainlife/mne:1.2.1` |
| ⚙️ **Resources** | 8 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.829](https://doi.org/10.25663/brainlife.app.829) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `epo1` | `neuro/meeg/mne/epochs` | yes | Epoched MEG data in MNE epochs .fif format. Epochs must include a pre-stimulus baseline before time 0. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/covariance` | Noise covariance matrix (cov.fif). |
| `out_dir_report` | `report/html` | HTML report (currently written to a different directory by the code, so it may be empty). |
| `out_figs` | `generic/image/png` | Covariance figure directory (the plotting code is disabled, so it may be empty). |

<details>
<summary><b>⚙️ Parameters</b> (6)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `tmin` | string | `None` | Start time for baseline. If None start at first sample. |
| `tmax` | string | `None` | End time for baseline. If None end at last sample. |
| `projs` | string | `None` | List of projectors to use in covariance calculation, or None to indicate that the projectors from the epochs should be inherited. If None, then projectors from all epochs must match. |
| `method` | string | `empirical` | The method used for covariance estimation. If ‘empirical’ (default), the sample covariance will be computed. A list can be passed to perform estimates using multiple methods. If ‘auto’ or a list of methods, the best estimator will be determined based on log-likelihood and cross-validation on unseen data. Valid methods are ‘empirical’, ‘diagonal_fixed’, ‘shrunk’, ‘oas’, ‘ledoit_wolf’, ‘factor_analysis’, ‘shrinkage’, and ‘pca’ |
| `keep_sample_mean` | boolean | `true` | If False, the average response over epochs is computed for each event type and subtracted during the covariance computation. This is useful if the evoked response from a previous stimulus extends into the baseline period of the next. Note. This option is only implemented for method=’empirical’. |
| `rank` | string | `None` | This controls the rank computation that can be read from the measurement info or estimated from the data. When a noise covariance is used for whitening, this should reflect the rank of that covariance, otherwise amplification of noise components can occur in whitening. |

</details>

📚 **References used by this App:**
- Avesani P, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.672-blue.svg)](https://doi.org/10.25663/brainlife.app.672)

This Brainlife app computes the noise covariance matrix for combined MEG and EEG data using the `mne.compute_covariance` function.



1) Input file is:

    * `epochs` evoked data file
    
2) Input parameters are:

* `tmin` Start time for baseline.

* `tmax` End time for baseline.

* `projs` List of projectors to use in covariance calculation.

* `method` The method used for covariance estimation.

* `rank` This controls the rank computation that can be read from the measurement info or estimated from the data.


3) Ouput files are:
    * Noise matrix 
    * a html report
   

## Authors
- Guiomar Niso (guiomar.niso@gmail.com)
- Antonio Caulín (antoniocaulinatienzar@gmail.com)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*- brainlife.io Publishing and Apps:*

Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

*- MNE-Python package:* 

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  **MEG and EEG data analysis with MNE-Python**. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University
