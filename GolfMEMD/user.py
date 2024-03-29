import os
import copy
from typing import List, Dict

import numpy as np
import matplotlib.pyplot as plt

from joint import Joint


class User():
    
    def __init__(self, user_name: str, set_joint: Dict[int, str], ballistic: str, impact_list: List[int], output: str):
        self.user = user_name
        self.joint = set_joint['j_num']
        self.joint_name = set_joint['j_name']
        self.ballistic = ballistic # ballistic -> 弾道の意味
        self.impact_list = impact_list
        self.output(output_dir=output)
    
    def output(self, output_dir):
        self.output_dir = output_dir
        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)
        if not os.path.isdir(os.path.join(self.output_dir, self.user)):
            os.mkdir(os.path.join(self.output_dir, self.user))
        if not os.path.isdir(os.path.join(self.output_dir, self.user, self.ballistic)):
            os.mkdir(os.path.join(self.output_dir, self.user, self.ballistic))
        if not os.path.isdir(os.path.join(self.output_dir, self.user, self.ballistic, self.joint_name)):
            os.mkdir(os.path.join(self.output_dir, self.user, self.ballistic, self.joint_name))
        self.save_path = os.path.join(self.output_dir, self.user, self.ballistic, self.joint_name)

    def _update_joint(self, select_joint):
        self.joint = select_joint['j_num']
        self.joint_name = select_joint['j_name']

    def _update_ballistic(self, ballistic):
        self.ballistic = ballistic

    def update_content(self, select_joint=None, ballistic=None):
        if select_joint is not None:
            self._update_joint(select_joint)
        if ballistic is not None:
            self._update_ballistic(ballistic)

