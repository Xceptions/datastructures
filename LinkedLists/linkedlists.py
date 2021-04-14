class Node:
    """
    Node class contains the attributes of each node.
    Only callable by our LinkedList class
    -----
    Returns: None
    """
    def __init__(self, val = None):
        self.val = val
        self.next = None


class LinkedList:
    """ Main LinkedList class will be callable """

    def __init__(self):
        # initialize the head to None. The first value that comes into the class
        # should be turned into the head
        self.head = None

    def add(self, n):
        # if our head is none, then we have to add the first node as our head
        if self.head == None:
            self.head = Node( n )
            return True
        # iterate through the list by shifting the pointer until you get to the end of the list
        # this is where you'll add the node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node( n )

    def printlist(self):
        # follows the same iteration principle as add above, but you print instead
        itr = self.head
        while itr:
            print(itr.val)
            itr = itr.next

    def reverse(self):
        # we are going to play around with three nodes
        prev = None
        current = self.head
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev
        self.printlist()
            


    def getIndexOf(self, val):
        """
        I don't think this function exists in a linkedlist
        I only built it to solidify my manipulation of linkedlists
        -----
        Returns: Index of node that contains the specified value, else False
        """
        count = 0
        itr = self.head
        while itr.next:
            if itr.val == val:
                return count
            else:
                itr = itr.next
                count += 1
        return False # did not find it

    def swapIndexes(self, a, b):
        pass

    def swapValues(self, i, j):
        pass

    def sortList(self):
        pass





"""
TEST FUNCTIONS
"""

def test_adding_to_linked_list(obj, a):
    for x in a:
        obj.add(x)

def test_printing_of_linked_list(obj):
    obj.printlist()

def test_reversing_of_linked_list(obj):
    obj.reverse()
    # obj.printlist()

def test_getIndexOf_value(obj, x):
    print(obj.getIndexOf(x))

if __name__ == "__main__":
    obj = LinkedList() # instantiate a linked list

    test_adding_to_linked_list(obj, [1,3,4,5,2,6])

    test_printing_of_linked_list(obj)

    test_reversing_of_linked_list(obj)

    # test_getIndexOf_value(obj, 2)

    # test_getIndexOf_value(obj, 7)
