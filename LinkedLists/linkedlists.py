class Node:
    """
    Node class contains the attributes of each node.
    Not callable. Only used by our LinkedList class
    -----
    Returns: None
    """
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    """ Main LinkedList class will be callable """

    def __init__(self):
        """
        Initialize the head to None. The first value that comes into the class should
        be turned into the head
        -----
        Returns: None
        """
        self.head = None

    def add(self, n):
        """
        If: our head is none, then we add the element to our list as our node
        Else: we iterate through the list by shifting the pointer until we get to the end. Then add the node
        -----
        Returns: Bool
        """
        if self.head is None:
            self.head = Node(n)
            return True
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(n)
        return True

    def printlist(self):
        """
        Iterate through the linkedlist and print the value on each iteration
        -----
        Returns: None
        """
        itr = self.head
        while itr:
            print(itr.val)
            itr = itr.next

    def reverse(self):
        """
        For each node, save its next node, make its next to be its previous,
        the previous to be the current, and the current to be the next
        -----
        Returns: None
        """
        prev = None
        current = self.head
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev

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
        return False  # did not find it

    def deleteNode(self, val):
        """
        Iterate through the list until you find the value, then set its previous.next to its next
        -----
        Returns: True if deleted, else False
        """
        if self.head.val == val:
            self.head = self.head.next
            return True
        itr = self.head
        while itr.next:
            if itr.next.val == val:
                itr.next = itr.next.next
                return True
            itr = itr.next
        return False  # the node did not exist

    def swapIndexes(self, a, b):
        pass

    def swapValues(self, i, j):
        pass

    def sortLinkedList(self):
        """
        To sort the linkedlist, I'm going to traverse it, save all the values, do a normal sort, then
        create a new linked list with the values
        """
        temp_list = []
        itr = self.head
        while itr.next:
            temp_list.append(itr.val)
            itr = itr.next
        temp_list.append(itr.val)
        temp_list.sort()
        newlist = LinkedList()
        for x in temp_list:
            newlist.add(x)
        return newlist


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
    obj.printlist()


def test_getIndexOf_value(obj, x):
    print(obj.getIndexOf(x))


def test_deletion_of_node(obj, x):
    obj.deleteNode(x)
    obj.printlist()


def test_sort_linked_list(obj):
    obj.sortLinkedList().printlist()


if __name__ == "__main__":
    obj = LinkedList()  # instantiate a linked list

    test_adding_to_linked_list(obj, [1, 3, 4, 5, 2, 6])

    # test_printing_of_linked_list(obj)

    # test_reversing_of_linked_list(obj)

    # test_deletion_of_node(obj, 2)

    # test_getIndexOf_value(obj, 2)

    # test_getIndexOf_value(obj, 7)

    test_sort_linked_list(obj)
