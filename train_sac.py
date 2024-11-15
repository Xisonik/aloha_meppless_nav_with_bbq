# Copyright (c) 2021-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

import argparse

import carb
import torch as th
from tasks.env_gt_nav import AlphaBaseEnv
#from tasks.test import AlphaBaseEnv
from stable_baselines3 import SAC
from stable_baselines3.common.callbacks import CheckpointCallback


log_dir = "/home/kit/.local/share/ov/pkg/isaac-sim-2023.1.1/standalone_examples/base_aloha_env/Aloha/models/SAC"
my_env = AlphaBaseEnv(headless=True)


checkpoint_callback = CheckpointCallback(save_freq=10000, save_path=log_dir, name_prefix="new_era")

total_timesteps = 2500000

model = SAC("MlpPolicy", my_env, verbose=1,tensorboard_log=log_dir,)# device="cuda", 

model.learn(total_timesteps=total_timesteps, callback=checkpoint_callback)

model.save(log_dir + "/SAC_policy")

my_env.close()
