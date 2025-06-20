class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        """Adds an element to the start of the linked list.
        
        Time Complexity: O(1)
        """
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        return
    
    def append(self, data):
        """Adds an element to the end of the linked list.
        
        Time Complexity: O(n)
        where n = length of linked list
        """
        new_node = Node(data)
        if self.head:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:
            self.head = new_node
        return
    
    def insert_at(self, index, data):
        """Inserts an element to the linked list at the specified index if the index exists.
        
        Time Complexity: O(n)
        where n = length of linked list
        """
        if index == 0:
            self.prepend(data)
        else:
            if self.head:
                position = 0
                curr_node = self.head
                prev_node = None
                while curr_node.next and position < index:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    position += 1
                if position == index and curr_node:
                    new_node = Node(data)
                    new_node.next = prev_node.next
                    prev_node.next = new_node
                else:
                    raise IndexError(f"Index {index} out of range")
            else:
                raise Exception("Cannot insert at index > 0 to an empty linked list")
    
    def pop_first(self):
        """Removes the first element of the linked list and returns it.
        
        Time Complexity: O(1)
        """
        if self.head:
            popped = self.head.data
            self.head = self.head.next
            return popped
        else:
            return None
        
    def pop_last(self):
        """Removes the last element of the linked list and returns it.
        
        Time Complexity: O(n)
        where n = length of linked list
        """
        if self.head:
            curr_node = self.head
            prev_node = None
            while curr_node.next:
                prev_node = curr_node
                curr_node = curr_node.next
            if prev_node:
                prev_node.next = None
                return curr_node.data
            else:
                self.head = None
                return curr_node.data
        else:
            None
    
    def remove_at(self, index):
        """Removes the element at the given index and returns it.
        
        Time Complexity: O(n)
        where n = length of linked list
        """
        if self.head:
            if index == 0:
                self.pop_first()
            else:
                curr_node = self.head
                prev_node = None
                position = 0
                while curr_node.next and position < index:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    position += 1
                if position == index and curr_node:
                    prev_node.next = curr_node.next
                    return curr_node.data
                else:
                    raise IndexError(f"Index {index} out of range")
        else:
            raise Exception("Cannot perform remove operation on an empty linked list")
    
    def __str__(self):
        """Returns a user friendly string representation of this linked list.
        
        To use this method, simple run print(linked_list) and the print() method
        will invoke the __str__ method to get the string representation.
        
        Time Complexity: O(n)
        where n = length of linked list
        """
        string_repr = ""
        if self.head:
            curr_node = self.head
            string_repr += f"{curr_node.data}"
            while curr_node.next:
                curr_node = curr_node.next
                string_repr += f" -> {curr_node.data}"
        return string_repr
    
    def __len__(self):
        if self.head:
            curr_node = self.head
            length = 1
            while curr_node.next:
                curr_node = curr_node.next
                length += 1
            return length
        else:
            return 0


ll = LinkedList()

print("Appending to empty linked list")
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
print(ll)

print("Inserting at index 3")
ll.insert_at(3, 7)
print(ll)

print("Popping the first element")
ll.pop_first()
print(ll)

print("Popping the last element")
ll.pop_last()
print(ll)

print("Removing element at index 2")
ll.remove_at(2)
print(ll)

print(f"Length of linked list is {len(ll)}")

ll.pop_first()
ll.pop_first()
ll.pop_first()
ll.pop_first()

print(ll)
