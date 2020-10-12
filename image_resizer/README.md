# Image Resizer

Resizes an image based on the specified width and height.

The following arguments can be specified:

- **file** The input image path/filename.
- **width** Width in pixels. If not specified, the image is resized based on the specified height, keeping the aspect ratio.
- **height** Height in pixels. If not specified, the image is resized based on the specified width, keeping the aspect ratio.

## Usage

```bash
python.exe image_resizer.py --width 200 --height 400 --file input_image.jpg
```

## Output
The resized image file named **output** with the same extension of the input file is generated within the same folder of the **image_resizer.py** script.
