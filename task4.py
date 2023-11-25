import os


def get_type(type_name: str) -> str:
    """
    The function returns the relative path to files of the specified type when instances end, the function returns None.
    """
    path = os.path.join('dataset', type_name)
    list_img = os.listdir(path)
    list_img.append(None)
    for i in range(len(list_img)):
        yield os.path.join(path, list_img[i]) if list_img[i] is not None else None


def main() -> None:

    type1 = 'polar_bear'
    # type2 = 'brown_bear'

    print(*get_type(type1))


if __name__ == "__main__":
    main()