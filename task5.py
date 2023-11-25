import os


class Iterator:
    def __init__(self, type_name: str):
        self.type_name = type_name
        self.counter = 0
        self.data = os.listdir(os.path.join('dataset', type_name))
        self.limit = len(self.data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            path = os.path.join(self.type_name, self.data[self.counter])
            self.counter += 1
            return path
        else:
            raise StopIteration
        

def main() -> None:

    type1 = 'polar_bear'

    name : Iterator = Iterator(type1)

    for i in range(66):
        print(next(name))


if __name__ == "__main__":
    main()