
class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None


class Hashtable:
  def __init__(self, size=1024):
    self.size = size
    self._buckets = [None] * size

  def hash(self, key):
    """_summary_

    Args:
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    return hash(key) % self.size

  def set(self, key, value):
    """_summary_

    Args:
        key (_type_): _description_
        value (_type_): _description_
    """
    index = self.hash(key)

    if self._buckets[index] is None:
      self._buckets[index] = Node(key, value)
    else:
      current = self._buckets[index]
      while current:
        if current.key == key:
          current.value = value
          return
        if current.next is None:
          break
        current = current.next

      new_node = Node(key, value)
      print(new_node)
      current.next = new_node


  def get(self, key):
    """_summary_

    Args:
        key (_type_): _description_

    Raises:
        KeyError: _description_

    Returns:
        _type_: _description_
    """
    index = self.hash(key)

    current = self._buckets[index]
    while current:
      if current.key == key:
        print(current.value)
        return current.value
      current = current.next

    raise KeyError(key)

  def has(self, key):
    """_summary_

    Args:
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
      self.get(key)
      return True
    except KeyError:
      return False

  def keys(self):
    """_summary_

    Returns:
        _type_: _description_
    """
    keys_list = []
    for node in self._buckets:
      current = node
      while current:
        keys_list.append(current.key)
        current = current.next
    return keys_list

  def contains(self, key):
    """
    Args: key (_type_): _description_
    Returns: _type_: _description_
    """
    index = self.hash(key)
    current = self._buckets[index]
    while current:
      if current.key == key:
        return True
      current = current.next
    return False
