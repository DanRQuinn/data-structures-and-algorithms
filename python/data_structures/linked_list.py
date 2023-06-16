class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

class LinkedList:
    def __init__(self, head=None, values=None, insert=None):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        if self.head == None:
            return "NULL"
        else:
            current = self.head
            output = ""
            while current:
                output += f"{{ {current.value} }} -> "
                current = current.next
            output += "NULL"
            return output

    def includes(self, value):
        current = self.head
        while current:
         if current.value == value:
             return True
         current = current.next
        return False



class TargetError:
    pass
