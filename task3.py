import os
import csv
import shutil
from random import sample
from typing import List


def copy(old: str, new: str) -> None:
    """
    The function copies images from the source directory to the new
    one and writes information about the images to a CSV file
    """
    abs_path = os.path.abspath(new)
    rel_path = os.path.relpath(new)
    random_number = sample(list(range(0, 10001)), 5005)
    count = 0
    for name in os.listdir(old):
        path = os.path.join(os.path.abspath(old), name)
        list_img = os.listdir(path)
        for img in list_img:
            new_n = str(random_number[count]).zfill(5)
            shutil.copy(os.path.join(path, img), os.path.join(new, F'{new_n}.jpg'))
            with open("annotasion3.csv", "a") as f:
                writer = csv.writer(f, delimiter=",", lineterminator="\r")
                writer.writerow([os.path.join(abs_path, F'{new_n}.jpg'),
                                 os.path.join(rel_path, F'{new_n}.jpg'), name])
                count += 1


def main() -> None:

    old_d = 'dataset'
    new_d = 'dataset3'

    if not os.path.isdir(new_d):
        os.mkdir(new_d)

    copy(old_d, new_d)


if __name__ == "__main__":
    main()