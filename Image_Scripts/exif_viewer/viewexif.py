import argparse
import PIL.Image
import PIL.ExifTags
import sys


def exif_reader(file_path):

    try:
        img = PIL.Image.open(file_path)
    except PIL.UnidentifiedImageError as e:
        print("UnidentifiedImageError: %s" % e)
        sys.exit(1)

    exif = {
        PIL.ExifTags.TAGS[y]: x
        for y, x in img._getexif().items()
        if y in PIL.ExifTags.TAGS
    }

    return exif


def printer(exif):

    Artist = exif.get("Artist", "Not found")
    DateTimeOriginal = exif.get("DateTimeOriginal", "Not found")
    Make = exif.get("Make", "Not found")
    Model = exif.get("Model", "Not found")
    BodySerialNumber = exif.get("BodySerialNumber", "Not found")
    LensModel = exif.get("LensModel", "Not found")
    LensSpecification = exif.get("LensSpecification", "Not found")
    LensSerialNumber = exif.get("LensSerialNumber", "Not found")
    Flash = exif.get("Flash", "Not found")
    FocalLength = exif.get("FocalLength", "Not found")
    ExifImageWidth = exif.get("ExifImageWidth", "Not found")
    ExifImageHeight = exif.get("ExifImageHeight", "Not found")
    FNumber = exif.get("FNumber", "Not found")
    ISOSpeedRatings = exif.get("ISOSpeedRatings", "Not found")
    WhiteBalance = exif.get("WhiteBalance", "Not found")
    ExposureMode = exif.get("ExposureMode", "Not found")
    ExposureTime = exif.get("ExposureTime", "Not found")
    Software = exif.get("Software", "Not found")
    ExifVersion = exif.get("ExifVersion", "Not found").decode("utf-8")

    clean_info = """
    Artist                : %s
    Date of Creation      : %s
    Camera Manufacturer   : %s
    Camera Model          : %s
    Camera Serial Number  : %s
    Lens Model            : %s
    LensSpecification     : %s
    Lens Serial Number    : %s
    Flash                 : %s
    Focal Length          : %s
    Image Resolution      : %s X %s pixels
    F-Number              : %s
    ISO Speed Ratings     : %s
    White Balance         : %s
    Exposure Mode         : %s
    Exposure Time         : %s
    Software Used         : %s
    Exif Version          : %s
    """ % (
        Artist,
        DateTimeOriginal,
        Make,
        Model,
        BodySerialNumber,
        LensModel,
        LensSpecification,
        LensSerialNumber,
        Flash,
        FocalLength,
        ExifImageWidth, ExifImageHeight,
        FNumber,
        ISOSpeedRatings,
        WhiteBalance,
        ExposureMode,
        ExposureTime,
        Software,
        ExifVersion,
    )
    print(clean_info)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="The path to file.")
    args = parser.parse_args()
    file_path = args.file_path
    exif = exif_reader(file_path)
    printer(exif)


if __name__ == "__main__":
    main()
