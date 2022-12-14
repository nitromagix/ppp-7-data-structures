


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.ref
                
    def end(self):
        current = self.head
        while (current.ref):
            current = current.ref
        return current

    def add_to_start(self, to_insert):
        new = Node.create_node_from(to_insert)
        if self.head is None:
            self.head = new
            return

        new.ref = self.head
        self.head = new

    def add_to_end(self, to_insert):
        new = Node.create_node_from(to_insert)
        if self.head is None:
            self.head = new
            return

        end = self.end()
        end.ref = new

    def add_item_after_value(self, value, to_insert):
        new = Node.create_node_from(to_insert)
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
            print(f"Add failed. {value} is not in the list")
            
    def remove_item(self, value):
        if self.head is None:
            print("Could not delete. The list is empty")
            return
        
        if self.head.value == value:
            self.head = self.head.ref

        previous = self.head
        current = self.head.ref
        found = False
        while (current):
            if current.value == value:
                found = True
                previous.ref = current.ref                
                
            previous = current
            current = current.ref
            
        if not found:
            print(f"Could not delete. {value} is not in the list")    
            


class Node:
    def __init__(self, value, ref=None):
        self.value = value
        self.ref = ref

    @staticmethod
    def create_node_from(input):
        if type(input) is int:
            return Node(input)
        elif type(input) is Node:
            return Node(input.value, input.ref)
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
print("")

ll.remove_item(44)
ll.print_linked_list()
