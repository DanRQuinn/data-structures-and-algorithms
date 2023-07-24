
class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None


class Hashtable:
    """
    Implement a Hashtable Class with the following methods:

set
Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.
get
Arguments: key
Returns: Value associated with that key in the table
has
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.
keys
Returns: Collection of keys
hash
Arguments: key
Returns: Index in the collection for that key
    """


    def __init__(self, _size):
        self._size = _size
        self._bucket = [None] * _size

    # This method sets the key and value pair in the table.
    # If the key already exists in the table, the value will be replaced.
    def set(self, key, value):
        index = self.hash(key)
        while self._bucket[index] is not None:
            if self._bucket[index][0] == key:
                self._bucket[index][1] = value
                return
            index = (index + 1) % self._size

        self.table[index] = (key, value)

    # This method returns the value associated with the given key.
    # If the key does not exist in the _bucket, None is returned.
    def get(self, key):
        index = self.hash(key)
        while self._bucket[index] is not None:
            if self._bucket[index][0] == key:
                return self._bucket[index][1]
            index = (index + 1) % self._size

        return None

    # This method returns True if the given key exists in the _bucket, False otherwise.
    def has(self, key):
        index = self.hash(key)
        while self._bucket[index] is not None:
            if self._bucket[index][0] == key:
                return True
            index = (index + 1) % self._size

        return False

    # This method returns a list of all the keys in the _bucket.
    def keys(self):
        keys = []
        for item in self._bucket:
            if item is not None:
                keys.append(item[0])
        return keys

    # This method returns the index in the _bucket for the given key.
    def hash(self, key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code % self._size


if __name__ == "__main__":
    hashtable = Hashtable(10)
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    print(hashtable.get("key1"))
    print(hashtable.get("key2"))
    print(hashtable.has("key1"))
    print(hashtable.has("key3"))
    print(hashtable.keys())
