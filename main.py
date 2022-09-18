

from platform import node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.ref

    def add_to_start(self, to_insert):
        new = Node.create_node_from_value(to_insert)
        if self.head is None:
            self.head = new
            return

        new.ref = self.head
        self.head = new

    def add_to_end(self, to_insert):
        new = Node.create_node_from_value(to_insert)
        if self.head is None:
            self.head = new
            return

        current = self.head
        while (current.ref):
            current = current.ref
        current.ref = new

    def add_item_after_value(self, value, to_insert):
        new = Node.create_node_from_value(to_insert)
        if self.head is None:
            self.head = new
            return

        current = self.head
        found = False
        while (current):
            if current.value == value:
                found = True
                next = current.ref
                current.ref = new
                new.ref = next
            current = current.ref
            
        if not found:
            print(f"Add failed. {value} is not in list")
            
    def remove_item(self, value):
        if self.head is None:
            print("Could not delete. List is empty")
            return
        
        if self.head.value == value:
            self.head = self.head.ref

        previous = self.head
        current = self.head.ref
        while (current):
            if current.value == value:
                previous.ref = current.ref                
                
            previous = current
            current = current.ref
            
            


class Node:
    def __init__(self, value, ref=None):
        self.value = value
        self.ref = ref

    @staticmethod
    def create_node_from_value(value):
        if type(value) is int:
            return Node(value)
        elif type(value) is Node:
            return value
        return None


node1 = Node(12)
node2 = Node(22)
node3 = Node(3)
ll = LinkedList(node1)

ll.add_to_start(node2)
ll.add_to_start(node3)
ll.add_to_start(47)
ll.print_linked_list()
print("")

node4 = Node(23)
ll.add_to_end(node4)
ll.add_to_end(38)
ll.print_linked_list()
print("")

node5 = Node(99)
ll.add_item_after_value(3, node5)
ll.add_item_after_value(23, 11)
ll.print_linked_list()
print("")

ll.remove_item(47)
ll.print_linked_list()
print("")

ll.remove_item(23)
ll.print_linked_list()