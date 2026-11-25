<h1 align="center">Noise Covariance Matrix for MEEG</h1>

<p align="center">
  Computes a noise covariance matrix from the pre-stimulus baseline of MEG epochs with MNE-Python compute_covariance and outputs it as cov.fif.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.829"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.829-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes a noise covariance matrix from the pre-stimulus baseline of MEG epochs with MNE-Python compute_covariance and outputs it as cov.fif.**

Reads the epochs, keeps MEG channels only, and estimates the covariance over the baseline (up to time 0) with the shrunk and empirical estimators and rank taken from the measurement info. Use it to obtain the noise covariance needed for MEG source estimation. The current code ignores all parameters (tmin, tmax, projs, method, keep_sample_mean, rank) and uses fixed settings.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/epochs` |
| **Outputs** | `neuro/meeg/mne/covariance` · `report/html` · `generic/image/png` |
| **Container** | `brainlife/mne:1.2.1` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.829](https://doi.org/10.25663/brainlife.app.829) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `epo1` | `neuro/meeg/mne/epochs` | yes | Epoched MEG data in MNE epochs .fif format. Epochs must include a pre-stimulus baseline before time 0. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/covariance` | Noise covariance matrix (cov.fif). |
| `out_dir_report` | `report/html` | HTML report (currently written to a different directory by the code, so it may be empty). |
| `out_figs` | `generic/image/png` | Covariance figure directory (the plotting code is disabled, so it may be empty). |

<details>
<summary><b>Parameters</b> (6)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `tmin` | string | `None` | Start time for baseline. If None start at first sample. |
| `tmax` | string | `None` | End time for baseline. If None end at last sample. |
| `projs` | string | `None` | List of projectors to use in covariance calculation, or None to indicate that the projectors from the epochs should be inherited. If None, then projectors from all epochs must match. |
| `method` | string | `empirical` | The method used for covariance estimation. If ‘empirical’ (default), the sample covariance will be computed. A list can be passed to perform estimates using multiple methods. If ‘auto’ or a list of methods, the best estimator will be determined based on log-likelihood and cross-validation on unseen data. Valid methods are ‘empirical’, ‘diagonal_fixed’, ‘shrunk’, ‘oas’, ‘ledoit_wolf’, ‘factor_analysis’, ‘shrinkage’, and ‘pca’ |
| `keep_sample_mean` | boolean | `true` | If False, the average response over epochs is computed for each event type and subtracted during the covariance computation. This is useful if the evoked response from a previous stimulus extends into the baseline period of the next. Note. This option is only implemented for method=’empirical’. |
| `rank` | string | `None` | This controls the rank computation that can be read from the measurement info or estimated from the data. When a noise covariance is used for whitening, this should reflect the rank of that covariance, otherwise amplification of noise components can occur in whitening. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.829](https://doi.org/10.25663/brainlife.app.829), choose `neuro/meeg/mne/epochs` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/covariance`, `report/html`, `generic/image/png`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:1.2.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "epo": "/path/to/epo1/epo",
       "tmin": "None",
       "tmax": "None",
       "projs": "None",
       "method": "empirical",
       "keep_sample_mean": true,
       "rank": "None"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Noise Covariance Matrix for MEEG. brainlife.io App. [doi:10.25663/brainlife.app.829](https://doi.org/10.25663/brainlife.app.829)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Guiomar Niso
- Antonio Caulín

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
