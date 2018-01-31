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
        #print(new_element.data)
        #print(self.length)
    def question5(self, first, m):
        count = 0
        if(self.length == 0):
            return None
        if(self.length < m):
            return "Please enter a valid number to fetch node"
        while(first.next) and count <= (self.length - m - 1):
            count += 1
            #print(str(count) + " " + str(first.data))
            first = first.next
            #print(first.data)
        return first.data

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

li = LinkedList()
print(li.question5(e1,1))
# output - None
li.push(e1)
li.push(e2)
li.push(e3)
li.push(e4)
print(li.question5(e1,2))
# output - 3
print(li.question5(e1,5))
# output - Please enter a valid number to fetch node
