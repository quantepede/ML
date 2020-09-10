class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head

        if not (isinstance(position, int) and position >= 1):
            raise TypeError("Position needs to be an integer greater than 0")

        for i in range(1, position):
            if current.next:
                current = current.next
            else:
                raise Exception(f"Position: {position} is out of bound, there are only {i} elements in the list.")

        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        current = self.head

        if not (isinstance(position, int) and position >= 1):
            raise TypeError("Position needs to be an integer greater than 0")

        if position == 1:
            self.head = new_element
            new_element.next = current

        else:
            for i in range(1, position-1):
                if current.next:
                    current = current.next
                else:
                    return None

            placeholder = current.next
            current.next = new_element
            new_element.next = placeholder

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head

        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break

                else:
                    current = current.next

            else:
                print(f"{value} is not found in the list ")

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)



# Test get_position
# Should print 3
print("Should print 3", ll.head.next.next.value)
# Should also print 3
print("Should also print 3", ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print("Should print 4 now", ll.get_position(3).value)

print("Test delete")
ll.delete(5)
# Should print 2 now
print("Should print 2 now", ll.get_position(1).value)
# Should print 4 now
print("Should print 4 now", ll.get_position(2).value)
# Should print 3 now
print("Should print 3 now", ll.get_position(3).value)
print("Should print 3 now", ll.get_position(4).value)

ll.insert_first(e2)
print("Should print 4 now", ll.get_position(4).value)
# first = ll.delete_first()
#
# print("Should print 1 now", ll.get_position(1).value)