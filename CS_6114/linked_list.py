class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head= Node()

    def append(self,data):
        new_node= Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        elems= []
        cur_node = self.head
        while cur_node.next != None:
            cur_node= cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_linked_list = linked_list()

my_linked_list.display()

my_linked_list.append('1')
my_linked_list.display()
