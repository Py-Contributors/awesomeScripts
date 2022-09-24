import cv2
import uuid
import os
import random
from PIL import Image
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image_dir", required=True, help="path to input image directory")
ap.add_argument("-n", "--num_image_require", required=True, help="number of image required")
ap.add_argument("-f", "--csv_file", required=True, help="path to csv file")
args = vars(ap.parse_args())

image_dir = args['image_dir']
csv_file = args['csv_file']
num_image_require = int(args['num_image_require'])

df = pd.read_csv(csv_file, index_col=[0])
duplicated = df[df['filename'].duplicated()]['filename'].values
print("Total Annotation Shape", df.shape)
df = df[df['filename'].isin(duplicated) == False]
print("Total Images shape", df.shape)
filenames = df['filename'].values

def get_cropped_img(filename):
    img = cv2.imread(os.path.join(image_dir, filename), 0)
    filtered = df[df['filename'] == filename]
    xmin, ymin, xmax, ymax = filtered['xmin'].values[0], filtered['ymin'].values[0], filtered['xmax'].values[0], filtered['ymax'].values[0]
    cropped_img = img[ymin : ymax, xmin : xmax]
    return cropped_img

def save_image_and_get_df_output(img1, img2):
    output_filename = str(uuid.uuid4()) + '.jpeg'
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
    new_corr = [[0, 0, w1, h1], [w1, 0, w1+w2, h2]]
    cv2.imwrite('synthetic_data/{}'.format(output_filename), vis)
    output_shape = vis.shape
    l1 = [output_filename, 'card', *new_corr[0], *output_shape[:2]]
    l2 = [output_filename, 'card', *new_corr[1], *output_shape[:2]]
    new_df = pd.DataFrame([l1, l2], columns=['filename', 'class', 'xmin', 'ymin', 'xmax', 'ymax', 'height', 'width'])
    return new_df


def main(num_image_require):
    output = []
    for i in range(num_image_require):
        print('Processing {}'.format(i))
        random_images = random.sample(list(filenames), 2)
        img1 = get_cropped_img(random_images[0])
        img2 = get_cropped_img(random_images[1])
        new_df = save_image_and_get_df_output(img1, img2)
        output.append(new_df)
    out_df = pd.concat(output)
    out_df.to_csv('synthetic_data/out_df.csv', index=False)

if __name__ == '__main__':
    num_image_require = 4000
    main(num_image_require)