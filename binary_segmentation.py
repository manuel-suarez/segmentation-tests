import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import cv2
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

DATA_DIR = './data/CamVid/'

# load repo with data if it is not exists
if not os.path.exists(DATA_DIR):
    print('Loading data...')
    os.system('git clone https://github.com/alexgkendall/SegNet-Tutorial ./data')
    print('Done!')