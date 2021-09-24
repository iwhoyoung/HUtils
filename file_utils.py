import os

import cv2
import pandas as pd
from PIL import Image


def read_csv_path(path):
    return pd.read_csv(path)


def read_csv(path, file_name):
    return pd.read_csv(path + (r'/%s.csv' % file_name))


def save_csv_file(dataset, path, file_name, header=True, index=False):
    if not os.path.exists(path):
        os.makedirs(path)
    # header = None代表没有表头
    dataset.to_csv(path + (r'/%s.csv' % file_name), header=header, index=index)


def tif2png_pil(original_path, saved_path):
    counts = 0
    files = os.listdir(original_path)
    for file in files:
        try:
            if file.endswith('tif'):
                tif_file = os.path.join(original_path, file)

                file = file[:-3] + 'png'
                png_file = os.path.join(saved_path, file)
                im = Image.open(tif_file)
                im.save(png_file)
                print(png_file)
                counts += 1
        finally:
            continue

    print('%d done' % counts)


def tif2png_cv(original_path, saved_path):
    counts = 0
    files = os.listdir(original_path)
    for file in files:
        try:
            if file.endswith('tif'):
                tif_file = os.path.join(original_path, file)

                file = file[:-3] + 'png'
                png_file = os.path.join(saved_path, file)
                im = cv2.imread(tif_file)
                cv2.imwrite(png_file, im)
                print(png_file)
                counts += 1
        finally:
            continue

    print('%d done' % counts)