""" 
# draw boundary box GT and prediction from csv file

# CSV_FILE - CSV_FILE for GT and prediction
# for prediction CSV_FILE is only required for filenames and image_dir is only required for image path
# for ground truth CSV_FILE is required for bboxes and image_dir is required for image path

# IMAGE_DIR - directory of images for GT and prediction

# input_txt_dir is the directory where the txt files are stored (prediction)
# txt file format - filename, score, xmin, ymin, xmax, ymax

# OUTPUT_DIR - directory to save the images with bboxes
"""

import pandas as pd
import cv2
import os
import argparse

args = argparse.ArgumentParser()
args.add_argument('--csv_file', type=str, help='csv file for bboxes')
args.add_argument('--image_dir', type=str, default='identity-card')
args.add_argument('--input_txt_dir', type=str, default='tmp_output')
args.add_argument('--output_dir', type=str, default='tmp_output')
args = args.parse_args()

df = pd.read_csv(args.csv_file)
filenames = df['filename'].values
image_dir = args.image_dir
input_txt_dir = args.input_txt_dir
predicted_image_output_dir = args.output_dir

os.makedirs(predicted_image_output_dir, exist_ok=True)
        
class DRAW_BBOX:
    
    def __init__(self, filenames):
        self.filenames = filenames
    
    def replace_ext(self, input_string):
        exts = ['.jpg', '.jpeg', '.JPG', '.png']
        for ext in exts:
            input_string = input_string.replace(ext, '.txt')
        return input_string

    def draw_rectangle(self, img_obj, xmin, ymin, xmax, ymax, score=None):
        cv2.rectangle(img_obj, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
        if score:
            txt_coordinate = (xmin + 20, ymin + 20)
            cv2.putText(img_obj, str(score), txt_coordinate, 3, 2, (0, 255, 0))
        
        return img_obj
    
    def draw_bboxes_gt(self):
        """ for ground truth """
        for idx, filename in enumerate(self.filenames):
            print('Processing {}/{}'.format(idx, len(self.filenames)))

            img_obj = cv2.imread(os.path.join(image_dir, filename))
            filtered = df[df['filename'] == filename]

            for index, row in filtered.iterrows():
                xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                
                img_obj = self.draw_rectangle(img_obj, xmin, ymin, xmax, ymax, None)
            
            cv2.imwrite(os.path.join(predicted_image_output_dir, filename), img_obj)


    def draw_bboxes_prediction(self):
        """ for prediction """
        for idx, filename in enumerate(self.filenames):
            print('Processing {}/{}'.format(idx, len(self.filenames)))
            
            txt_filename = self.replace_ext(filename)
            txt_file_path = os.path.join(input_txt_dir, txt_filename)

            if os.path.isfile(txt_file_path):
                with open(txt_file_path, 'r') as fo:
                    content = fo.read().splitlines()

                img_obj = cv2.imread(os.path.join(image_dir, filename))
                for line in content:
                    split = line.split(' ')
                    bbox = [int(x) for x in split[-4:]]
                    
                    xmin, ymin, xmax, ymax = bbox[0], bbox[1], bbox[2], bbox[3]
                    
                    score = float(split[-5])
                    score = round(score, 2) * 100
                    
                    img_obj = self.draw_rectangle(img_obj, xmin, ymin, xmax, ymax, score)

                cv2.imwrite(os.path.join(predicted_image_output_dir, filename), img_obj)

if __name__ == '__main__':
    draw_bbox = DRAW_BBOX(filenames)
    #draw_bbox.draw_bboxes_gt()
    draw_bbox.draw_bboxes_prediction()
    

# python draw_bbox_for_detection.py --csv_file CSV_FILE --image_dir IMAGE_DIR --input_txt_dir INPUT_TXT_DIR --output_dir OUTPUT_DIR