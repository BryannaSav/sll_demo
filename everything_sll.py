class Node: 
    def __init__(self, value): #__init__ takes care of Class creation and attributes it has
        print("Making a new node!!! Using the passed in value ", value)
        self.val = value
        self.next = None

class Sll:
    def __init__(self):
        print("Making a new SLL!!!")
        self.head = None
    def add_to_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    def print_sll_nodes(self):
        runner = self.head
        while runner != None:
            print("Current Node Value: ", runner.val)
            runner = runner.next




##SLL TESTING GROUND

#Making a new SLL
my_sll = Sll()

#Putting stuff in our sll to test it
my_sll.add_to_front(1)
my_sll.add_to_front(5)
my_sll.add_to_front(9)

#Using our built in to print vals
my_sll.print_sll_nodes()