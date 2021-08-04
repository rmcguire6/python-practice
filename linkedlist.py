# my_linked_list = {'head': {'value':10, 'next': {
#     'value': 5, 'next': {'value': 16, 'next': None}
# }}}
class LinkedList:
    def __init__(self, value):
        self.head = {'head': {'value': value, 'next': None}}
        self.tail = self.head
        self.length = 1
    def append(self, value):
        self.node = {'value': value, 'next': None}
        self.tail[next] = self.node
        self.tail = self.node

a_list = LinkedList(10)
a_list.append(5)
a_list.append(16)
print(a_list.head)
