# ######################################
# # FULL-TRAINING SEGMENTATION CONFIGS #
# ######################################

import os
from operator import itemgetter
from default_configs import *

# TODO: Change configs based on the requirements of the experiment
# For references, go the sibling python file "default_configs.py".

# CUSTOM CONFIGS BLOCK -- start:

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

# CUSTOM CONFIGS BLOCK -- end:

def run_exps():
    # Loops for running the finetune experiments
    for model in models:
        for dataset in datasets:
            # Model specific cfgs
            cfg = models_configs[model]
            batch_size, lr = itemgetter("batch_size", "lr")(cfg)
            for seed in seeds:
                exp_name = f"{model}_{dataset}_seed_{seed}"
                batch_size = 32
                task_name = "pred"
                # Define bash command here for individual experiments
                command = f"python src/eval.py \
                    experiment={model}.yaml \
                    experiment_name={exp_name} \
                    ckpt_path=logs/train/runs/{exp_name}/checkpoints/best.ckpt \
                    datamodule={dataset}.yaml \
                    datamodule.batch_size={batch_size} \
                    trainer.accelerator={accelerator} \
                    trainer.precision={precision} \
                    trainer.devices={devices} \
                    prompt_type={prompt_type} \
                    seed={seed} \
                    logger=csv.yaml \
                    tags='[{model}, {dataset}, {prompt_type}, seed_{seed}]' \
                    task_name={task_name} \
                    output_masks_dir=output_masks/{model}/{dataset}/{prompt_type}/seed_{seed}"
                
                # Log command in terminal
                print(f"RUNNING COMMAND \n{command}")

                # Run the command
                if os.system(command=command) != 0:
                    # Break the experimentation loop if error is detected
                    print(f"!!! ERROR - COMMAND FAILED!!! \n{command}")
                    exit()

if __name__ == "__main__":
    run_exps()