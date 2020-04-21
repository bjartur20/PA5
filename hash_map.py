from collections.abc import MutableMapping
from random import randrange
from bucket import *

class HashMap():
    def __init__(self, cap=11, p=109345121):
        self._table = [Bucket() for _ in range(cap)]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift ) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        return self.find(k)

    def __setitem__(self, k, v):
        try:
            self.insert(k, v)
        except ItemExistsException:
            self.update(k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        self.remove(k)
        self._n -= 1

    def _resize(self, c):
        og_length = self._n
        old = self._table
        self._table = [Bucket() for _ in range(c)]
        for bucket in old:
            for item in bucket:
                self[item.key] = item.data
        self._n = og_length

    # Required functions
    def insert(self, key, data):
        idx = self._hash_function(key)
        try:
            self._table[idx][key]
            raise ItemExistsException()
        except NotFoundException:
            self._table[idx][key] = data
            self._n += 1

    def update(self, key, data):
        idx = self._hash_function(key)
        bucket = self._table[idx]
        for item in bucket:
            if item.key == key:
                bucket[key] = data
                return
        raise NotFoundException()

    def find(self, key):
        idx = self._hash_function(key)
        bucket = self._table[idx]
        try:
            return bucket[key]
        except:
            raise NotFoundException()
        
    def contains(self, key):
        idx = self._hash_function(key)
        bucket = self._table[idx]
        for item in bucket:
            if item.key == key:
                return True
        return False

    def remove(self, key):
        idx = self._hash_function(key)
        bucket = self._table[idx]
        bucket.remove(key)
        self._n -= 1


if __name__ == "__main__":
    m = HashMap()