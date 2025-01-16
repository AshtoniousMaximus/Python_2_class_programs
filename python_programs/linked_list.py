# linked lists program
# created by Ashton Pankey
# revised on 10/22/2024

# creates a class Node
class Node:
    # creates an init method that takes contents and next
    def __init__ (self, contents = None, next = None) -> None:
        self.contents = contents
        self.next = next
    # creates a repr method that prints the contents of the node
    def __repr__ (self)-> str:
        return f"this node contains: {self.contents}"

# creates three nodes with their contents 
node_1 = Node(contents = 1)
two = Node(contents = 2)
three = Node(contents = 3)

# creates a Linked_list class for linked lists
class Linked_List:
    # creates an init method that takes a Node
    def __init__(self,head:Node):
        self.head = head

    # creates a repr method that prints out the contents of the linked list in a more readable format
    def __repr__(self)->str:
        # creates an empty list 
        list_contents = []
        # sets the current node to the head of the list
        current_node = self.head
        # creates a while loop to run while the current node is not None
        while current_node is not None:
            # adds the current node to the list
            list_contents.append(str(current_node.contents))
            # moves to the next node
            current_node = current_node.next
        # adds None after the nodes to show that they go to nothing
        list_contents.append('None')
        # returns the list as a readable string into the terminal
        return ' -> '.join(list_contents)
    
    # creates the append_right method that takes a Node
    def append_right(self,node_to_add: Node):
        # start at the head
        current_node = self.head
        # creates a while loop to go throught until at the last node
        while current_node.next is not None:
            # progresses to the next node
            current_node = current_node.next
        # once at the end, it adds another node to the tail of the list
        current_node.next = node_to_add

    # creates the append_left method that takes a Node
    def append_left(self,node_to_add: Node):
        # sets old_head to the head of the list
        old_head = self.head
        # sets the head of the list to the node to add
        self.head = node_to_add
        # adds the original head as the next in line past the new head
        self.head.next = old_head

    # creates the pop left method 
    def pop_left(self):
        # sets old_head equal to the current head of the list
        old_head = self.head
        # sets the next along the list as the new head, disregarding the old head in the process
        self.head = self.head.next
        # returns the old_head which was the previous head
        return old_head
    
    # creates the pop_right method
    def pop_right(self):
        # sets the current node the the head of the list
        current_node = self.head
        # goes to the end node
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        # removes the end node
        previous_node.next = None
        # returns the end node
        return current_node
    
    # checks if the thing n is in the contents
    def list_contains(self,n):
        # sets the current node to the head of the list
        current_node = self.head
        # runs through the list until it is the last node
        while current_node is not None:
            # if the current node contains n, the method returns true, otherwise it keeps going until the list ends
            if current_node.contents == n:
                return True
            # progresses through the list
            current_node = current_node.next
        # if the node is not found, the method returns false
        return False
           
    # creates the method reverse_list to reverse lists
    def reverse_list(self):
        # sets the current_node to the head of the list
        current_node = self.head
        # sets the previous node to None
        prev = None
        # creates a while loop to run intil the current node is None
        while current_node is not None:
            # assigns the next node to beyond
            beyond = current_node.next
            # sets the next node to the previous node
            current_node.next = prev
            # sets prev to the current node
            prev = current_node
            # makes the current node the next node
            current_node = beyond
        # after the while loop, the head is set as prev
        self.head = prev


# creates Linky the Linked_list
Linky = Linked_List(node_1)
# prints what Linky is
print(Linky)
# adds the node two to the right end of the list
Linky.append_right(two)
# adds the node three to the right end of the list
Linky.append_right(three)
# prints what Linky is now
print(Linky)
# removes the head from the list
Linky.pop_left()
# prints what Linky is now
print(Linky)
# removes the rightmost node of the list
Linky.pop_right()
# prints what Linky is now
print(Linky)
# removes the head from the list
Linky.pop_left()
# prints what Linky is now
print(Linky)
# adds node_1 to the start of the Linky list
Linky.append_left(node_1)
# prints what Linky is now
print(Linky)
# adds the node two to the right side of the linky list
Linky.append_right(two)
# prints what Linky is now
print(Linky)
# adds the node three to the right side of the linky list
Linky.append_right(three)
# prints what Linky is now
print(Linky)
# checks if Linky contains the value 3 somewhere
print(Linky.list_contains(3))
# reverses the Linky list with the function reverse_list
Linky.reverse_list()
# prints what Linky is now
print(Linky)

