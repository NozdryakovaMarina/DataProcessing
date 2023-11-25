import os
import csv
import shutil
from typing import List


def  change(old: str, new: str, type: List[str]) -> None:
    """
    The function copies images from the old directory to the new one,
    changing the name and writes information about the images to a CSV file
    """
    abs_path = os.path.abspath(new)
    rel_path = os.path.relpath(new)
    for name in type:
        path = os.path.join(os.path.abspath(old), name)
        list_img = os.listdir(path)
        for img in list_img:
            shutil.copy(os.path.join(path, img), os.path.join(new, F'{name}_{img}'))
            with open('annotation2.csv', 'a') as f_csv:
                writer = csv.writer(f_csv, delimiter=',', lineterminator='\r')
                writer.writerow([os.path.join(abs_path, F'{name}_{img}'),
                                 os.path.join(rel_path, F'{name}_{img}'), name])


def main() -> None:
    types = ['polar_bear', 'brown_bear']

    old_d = 'dataset'
    new_d = 'dataset2'

    if not os.path.isdir(new_d):
        os.mkdir(new_d)
        
    change(old_d, new_d, types)


if __name__ == "__main__":
    main()