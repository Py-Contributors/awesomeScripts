from imutils import paths
import numpy as np
import argparse
import cv2
import os


def dhash(image, hash_size=8):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hash_size + 1, hash_size))

    diff = resized[:, :-1]

    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
ap.add_argument(
    "-r",
    "--remove",
    type=int,
    default=-1,
    help="whether or not duplicates should be removed. (i.e. dry run)",
)
args = vars(ap.parse_args())

print("[INFO] computing image hashes...")
image_paths = list(paths.list_images(args["dataset"]))
hashes = {}

for image_path in image_paths:
    image = cv2.imread(image_path)
    h = dhash(image)

    p = hashes.get(h, [])
    p.append(image_path)
    hashes[h] = p

for (h, hashed_paths) in hashes.items():
    if len(hashed_paths) > 1:
        if args["remove"] <= 0:
            montage = None

            for p in hashed_paths:

                image = cv2.imread(p)
                image = cv2.resize(image, (150, 150))

                if montage is None:
                    montage = image
                else:
                    montage = np.hstack([montage, image])

            print("[INFO] hash : {}".format(h))
            cv2.imshow("Montage", montage)
            cv2.waitKey(0)
        else:
            for p in hashed_paths[1:]:
                os.remove(p)
