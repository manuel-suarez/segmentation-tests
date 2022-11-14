import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import cv2
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Data directories
DATA_DIR = './oil_spill_data/'
x_train_dir = os.path.join(DATA_DIR, 'train', 'images')
y_train_dir = os.path.join(DATA_DIR, 'train', 'labels_1D')

x_valid_dir = os.path.join(DATA_DIR, 'val', 'images')
y_valid_dir = os.path.join(DATA_DIR, 'val', 'labels_1D')

x_test_dir = os.path.join(DATA_DIR, 'test', 'images')
y_test_dir = os.path.join(DATA_DIR, 'test', 'labels_1D')