# VLSM-Adapter: Finetuning Vision-Language Segmentation Efficiently with Lightweight Blocks



## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Pretrained Model Preparation](#pretrained-model-preparation) 
  - [Dataset Preparation](#dataset-preparation)
  - [Finetuning](#finetuning)

## Installation

To get started, it's recommended to create a Python (preferably v3.10) environment using either Conda or venv. This helps to manage dependencies and ensure a consistent runtime environment.

1. **Conda:**
  ```bash
    conda create --name your_env_name python=3.10
    conda activate your_env_name
  ```
**OR**

2. **venv:**
  ```bash
    python -m venv your_env_name
    source your_env_name/bin/activate
  ```

Once your environment is active, install the required packages from `requirements.txt` using pip:
```bash
pip install -r requirements.txt
```

## Usage

### Pretrained Model Preparation
Because the pretrained weights of *BiomedCLIP* and *CLIPSeg* are readily available in the *Hugging Face Model Hub* you do not need to save the weights manually. However, the [pretrained weights](https://github.com/DerrickWang005/CRIS.pytorch/issues/3) of *CRIS* were extracted and then saved within the folder `pretrained/`. Please refer to the config file [cris.yaml](configs/model/cris.yaml) for more information.

### Dataset Preparation
Before running any experiments, you need to ensure that the provided dataset is correctly placed within the `data/` folder at the root of the project. The directory structure of the `data/` folder should look like this:
```
data/
│
├── bkai_polyp/
│   ├── anns/
│   │   ├── test.json
│   │   ├── train.json
│   │   └── val.json
│   ├── images/
│   └── masks/
│
├── [other dataset folders...]
│
└── kvasir_polyp/
    ├── anns/
    │   ├── test.json
    │   ├── train.json
    │   └── val.json
    ├── images/
    └── masks/
```
Each dataset folder (`bkai_polyp`, `busi`, `camus`, etc.) contains three sub-directories: `anns`, `images`, and `masks`. The anns directory contains prompt files (`test.json`, `train.json`, `val.json`), while `images` and `masks` hold input images and target masks respectively.


### Finetuning

If you need to run fine-tuning for your model, you can do so using the following script:
```bash
python scripts/finetune.py
```
This script will start the fine-tuning process, which is essential for customizing the model for specific tasks. For running inference, please update the defaults configs (such as `ckpt_path`, `models`, etc.) in `scripts/inference.py` to get the evulation metric or generate the output masks (in the original resolution).



### Acknowledgement
We would like to thank [Lightning-Hydra-Template](https://github.com/ashleve/lightning-hydra-template) for providing a modifiable framework for running multiple experiments while tracking the hyperparameters.