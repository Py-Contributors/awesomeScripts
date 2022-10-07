# Draw BBox for Ground Truth and Detection

This is a simple tool to draw bounding box for ground truth and detection. 

### Draw boundary box GT and prediction from csv file

### CSV_FILE - CSV_FILE for GT and prediction
- For prediction **CSV_FILE** is only required for filenames and image_dir is only required for image path
- For ground truth **CSV_FILE** is required for bboxes and image_dir is required for image path

### IMAGE_DIR - directory of images for GT and prediction

### input_txt_dir is the directory where the txt files are stored (prediction)
- txt file format 
  - - filename, score, xmin, ymin, xmax, ymax
  - - filename, score, xmin, ymin, xmax, ymax

### OUTPUT_DIR - directory to save the images with bboxes

## Usages

```bash
python draw_bbox_for_detection.py --csv_file CSV_FILE --image_dir IMAGE_DIR --input_txt_dir INPUT_TXT_DIR --output_dir OUTPUT_DIR
```