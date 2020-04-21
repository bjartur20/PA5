class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Bucket():

    class Node():
        def __init__(self, key=None, data=None, next=None):
            self.key = key
            self.data = data
            self.next = next

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self._size = 0

    def __str__(self):
        ret_str = ''
        walker = self.head
        while walker is not None:
            ret_str += str(walker.key) + ':' + str(walker.data) + '\n'
            walker = walker.next
        return ret_str

    def __len__(self):
        return self._size

    def __iter__(self):
        walker = self.head
        while walker is not None:
            yield walker
            walker = walker.next

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __ites__(self):
        walker = self.head
        while walker is not None:
            yield walker
            walker = walker.next

    def insert(self, key, data):
        if not self.contains(key):
            new_node = self.Node(key, data)
            if self._size == 0:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self._size += 1
        else:
            raise ItemExistsException()
    
    def update(self, key, data):
        if self.contains(key):
            node = self._find_node(key)
            node.data = data
        else:
            raise NotFoundException()

    def find(self, key):
        node = self._find_node(key)
        if node:
            return node.data
        raise NotFoundException()

    def contains(self, key):
        if self._find_node(key):
            return True
        return False

    def remove(self, key):
        node = self._find_node(key)
        if node:
            walker = self.head
            while walker is not None:
                if walker.next == node:
                    walker.next = walker.next.next
                    if node is self.tail:
                        self.tail = walker
                    self._size -= 1
                    return
                elif walker == node:
                    self.head = walker.next
                    self._size -= 1
                    return
                walker = walker.next
        else:
            raise NotFoundException()

    def _find_node(self, key):
        walker = self.head
        while walker is not None:
            if walker.key == key:
                return walker
            walker = walker.next