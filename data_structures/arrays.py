# implementation of array
class Array:
    def __init__(self, sizeOfArray, arrayType=int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems = [arrayType(0)] * sizeOfArray
        self.arrayType = arrayType

    def __str__(self):
        return " ".join([str(i) for i in self.arrayItems])

    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if self.arrayItems[i] == keyToSearch:
                return i
        return -1

    def insert(self, keyToInsert, position):
        if self.sizeOfArray > position:
            for i in range(self.sizeOfArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print("Array size is:", self.sizeOfArray)

    def delete(self, keyToDelete, position):
        if self.sizeOfArray > position:
            for i in range(position, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
        else:
            print("Array size is:", self.sizeOfArray)


if __name__ == "__main__":
    # test array
    a = Array(10)
    print(a)
    print(a.search(2))
    a.insert(2, 5)
    print(a)
    a.delete(2, 5)
    print(a)
