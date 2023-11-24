import os
import csv
import shutil
from typing import List

def get_abs(type_name: str) -> List[str]:
    """
    The function returns a list of absolute paths for images of a certain type passed 
    to the function, after copying the images to another directory
    """
    abs_path = os.path.abspath('dataset2')
    list_img = os.listdir(abs_path)
    type_img = [name for name in list_img if type_name in name]
    img_abs = list(map(lambda name: os.path.join(abs_path, name), type_img))
    return img_abs


def get_rel(type_name: str) -> List[str]:
    """
    The function returns a list of relative paths for images of a certain type passed 
    to the function after copying the images to another directory
    """
    rel_path = os.path.relpath('dataset2')
    list_img = os.listdir(rel_path)
    type_img = [name for name in list_img if type_name in name]
    img_rel = list(map(lambda name: os.path.join(rel_path, name), type_img))
    return img_rel


def  change(old: str, new: str, type: List[str]) -> None:
    """
    The function copies images from the old directory to the new one,
    changing the name
    """
    abs_path = os.path.abspath(new)
    rel_path = os.path.relpath(new)
    for name in type:
        path = os.path.join(os.path.abspath(old), name)
        list_img = os.listdir(path)
        for img in list_img:
            shutil.copy(os.path.join(path, img), os.path.join(new, F'{name}_{img}'))


def main() -> None:

    type1 = 'polar_bear'
    type2 = 'brown_bear'

    types = ['polar_bear', 'brown_bear']

    old_d = 'dataset'
    new_d = 'dataset2'

    if not os.path.isdir(new_d):
        os.mkdir(new_d)
        
    change(old_d, new_d, types)
    
    polarbear_abs = get_abs(type1)
    polarbear_rel = get_rel(type1)
    brownbear_abs = get_abs(type2)
    brownbear_rel = get_rel(type2)


    with open('annotation2.csv', 'w') as f_csv:
        writer = csv.writer(f_csv, delimiter=',', lineterminator='\r')
        for abs_path, rel_path in zip(polarbear_abs, polarbear_rel):
            writer.writerow([abs_path, rel_path, type1])
        for abs_path, rel_path in zip(brownbear_abs, brownbear_rel):
            writer.writerow([abs_path, rel_path, type2])


if __name__ == "__main__":
    main()