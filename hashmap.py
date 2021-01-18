
class HashTable:
    def __init__(self):
        self.MAX = 100
        # List comprehension for the array with size 100 and value as None
        # self.arr = [None for i in range(self.MAX)]
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # ord return the unicode(ascii) of the character
            h += ord(char)

        return h % self.MAX

    # def add_key_val(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    # def get_val(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        # self.arr[h] = val
        found = False

        # Has to understand these lines of code
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return print(element[1])
        # return print(self.arr[h])

    def __delitem__(self, key):
        h = self.get_hash(key)
        # self.arr[h] = None
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
t["march 6"] = 263
t["march 9"] = 363
t["march 12"] = 663
t["march 17"] = 999


t["march 9"]
del t["march 9"]

t["march 6"]
t["march 17"]
