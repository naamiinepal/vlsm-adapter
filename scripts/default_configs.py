from typing import Literal

"""
    DEFAULT CONFIGS BLOCK -- start
        Do not make any new changes to this block because it has to be used for future references
"""
accelerator = "gpu"
devices = [0]
precision = "16-mixed"

models = [
    "cris",
    "clipseg",
    "san",
    "clipseg_dense_adapter_vlc",
    "clipseg_dense_adapter_vl",
    "clipseg_dense_adapter_v",
    "clipseg_shallow_adapter_vlc",
    "clipseg_shallow_adapter_vl",
    "clipseg_shallow_adapter_v",
]

models_configs = {
    "cris": {"batch_size": 32, "lr": 0.001},
    "clipseg": {"batch_size": 32, "lr": 0.001},
    "san": {"batch_size": 32, "lr": 0.0003},
    "clipseg_dense_adapter_vlc": {"batch_size": 32, "lr": 0.001},
    "clipseg_dense_adapter_vl": {"batch_size": 32, "lr": 0.001},
    "clipseg_dense_adapter_v": {"batch_size": 32, "lr": 0.001},
    "clipseg_shallow_adapter_vlc": {"batch_size": 32, "lr": 0.0003},
    "clipseg_shallow_adapter_vl": {"batch_size": 32, "lr": 0.0003},
    "clipseg_shallow_adapter_v": {"batch_size": 32, "lr": 0.0003},
}

datasets = [
    "kvasir_polyp",
    "bkai_polyp", 
    "clinicdb_polyp",
    "isic",
    "dfu",
    "camus",
    "busi",
    "chexlocalize",
]

task_name: Literal["pred", "eval", "train"] = "eval"

seeds = [41, 42, 43]

prompt_type = "random"
"""
    DEFAULT CONFIGS BLOCK -- end
"""
