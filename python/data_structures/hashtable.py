class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def display(self):
        return([self.key, self.value])


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._bucket = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)

        if self._bucket[index] is None:
            self._bucket[index] = Node(key, value)
        else:
            current = self._bucket[index]
            new_node = Node(key, value)
            new_node.next = current
            self._bucket[index] = new_node
            print(new_node)
            


    def get(self, key):
        index = self._hash(key)

        current = self._bucket[index]
        while current:
            if current.key == key:
                print(current.value)
                return current.value
            current = current.next

        raise KeyError(key)

    def has(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self):
        keys_list = []
        for node in self._bucket:
            current = node
            while current:
                keys_list.append(current.key)
                current = current.next
        return keys_list


if __name__== "__main__":
    pass
