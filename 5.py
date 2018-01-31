class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    length = 0
    head = None
    def push(self, new_element):
        global length
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        self.length += 1
