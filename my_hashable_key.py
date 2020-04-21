from random import Random

class MyHashableKey():
    def __init__(self, int_val, str_val):
        self.int = int_val
        self.str = str_val

    def __eq__(self, other):
        return self.int == other.int and self.str == other.str

    def __hash__(self):
        # Hash the string value
        mask = (1 << 32) - 1
        hash_code = 0
        for char in self.str:
            hash_code = (hash_code << 5 & mask) | (hash_code >> 27)
            hash_code += ord(char)

        # Use the int value 
        hash_code += self.int
        if hash_code < 0:
            hash_code = hash_code * -1 + 1

        return hash_code

if __name__ == "__main__":
    rand = Random()
    lis_size = 13
    lis = [0] * lis_size

    for _ in range(13000):
        int_val = rand.randint(-100,100)
        str_val = ''.join([chr(rand.randint(100,300)) for _ in range(5)])
        key = MyHashableKey(int_val, str_val)
        index = hash(key) % lis_size
        lis[index] += 1

    print(lis)