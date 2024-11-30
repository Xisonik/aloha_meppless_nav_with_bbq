from dataclasses import asdict, dataclass
from typing import Any, DefaultDict, Dict, Optional, Tuple, Union
import numpy as np

from pathlib import Path
d = Path().resolve()#.parent
general_path = str(d) + "/standalone_examples/Aloha_graph/Aloha"

@dataclass
class MainConfig:
    tuning: bool = True
    headless: bool = True
    reward_mode: int = 1
    cup_usd_path: str = general_path + "/assets/objects/bowl.usd"
    jetbot_asset_path: str = general_path + "/assets/aloha/ALOHA_with_sensor_02.usd"
    # room_usd_path: str = general_path + "/assets/scenes/sber_kitchen/sber_kitchen_ft.usd"
    room_usd_path: str = general_path + "/assets/scenes/scenes_sber_kitchen_for_BBQ/kitchen.usd"
    camera_paths: str = "/jetbot/fl_link4/visuals/realsense/husky_rear_left"
    goal_image_path: str = general_path + '/img/goal.png'
    goalb_image_path: str = general_path + '/img/goal_bowl.png'
    train_log_dir: str = general_path + "/models/SAC"
    load_policy: str = general_path + "/models/SAC/GRM_v1p2f0_85000_steps.zip"
    log_path: str = general_path + "/log.txt"
    camera_usd_local_path = general_path + '/assets/aloha/aloloha_v03_cameras.usd'
    camera_image_saved_path = general_path + "/img/"
    loss_path:str = general_path+'/loss.pt'
    load_emb_nn:str = general_path + "/scene_embedding_epoch_180000.pth"
    training_mode:int = 0
    scene_file_test: str = general_path + "/scene/scene_test/"
    scene_file_train: str = general_path + "/scene/scene_train/"
    eval:bool = False
    eval_radius:float = 0.6
    eval_angle:float = np.pi/6
