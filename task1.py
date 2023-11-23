import os
import csv
from typing import List


def get_abs_path(type_name: str) -> List[str]:
    """
    The function returns a list of absolute paths for all images of a certain type passed to the function
    """
    abs_path = os.path.abspath('dataset')
    type_path = os.path.join(abs_path, type_name)
    list_img = os.listdir(type_path) 
    img_abs = list(map(lambda name: os.path.join(type_path, name), list_img))
    return img_abs


def get_rel_path(type_name: str) -> List[str]:
    """
    The function returns a list of relative paths for all images of a certain type passed to the function
    """
    rel_path = os.path.relpath('dataset')
    type_path = os.path.join(rel_path, type_name)
    list_img = os.listdir(type_path)
    img_rel = list(map(lambda name: os.path.join(type_path, name), list_img))
    return img_rel


def main() -> None:

    type1 = 'polar_bear'
    type2 = 'brown_bear'

    polarbear_abs = get_abs_path(type1)
    polarbear_rel = get_rel_path(type1)
    brownbear_abs = get_abs_path(type2)
    brownbear_rel = get_rel_path(type2)


    with open('annotation1.csv', 'w') as f_csv:
        writer = csv.writer(f_csv, delimiter=',', lineterminator='\r')
        for abs_path, rel_path in zip(polarbear_abs, polarbear_rel):
            writer.writerow([abs_path, rel_path, type1])
        for abs_path, rel_path in zip(brownbear_abs, brownbear_rel):
            writer.writerow([abs_path, rel_path, type2])


if __name__ == "__main__":
    main()