import math
# Implement a data structure with some special requirements:
# SpecialLinkedList: add, and get

# add should work like:
# my_list.add(1)
# [1]
# my_list.add(2)
# my_list.add(3)
# [1] <- [2, 3]
# my_list.add(4)
# [1] <- [2, 3] <- [4, _, _, _] and so on ...

# get should start from the right. Instead of starting from very beginning.
# if we do my_list.get(2) from
# [1] <- [2, 3]
# we get 2


class Node(object):
    """docstring for Node"""
    def __init__(self):
        self.next = None
        self.size = 0
        self.elements = []


class SpecialLinkedList(object):
    """docstring for SpecialLinkedList"""
    def __init__(self):
        self.head = None
        self.root = None
        self.tail = None

    def add(self, new_number):
        # We have a the structure like: [1]
        if self.root is None:
            new_node = Node()
            new_node.size = 1
            new_node.elements.append(new_number)
            self.head = new_node
            self.root = new_node
            self.tail = new_node
            return
        else:
            # this checks this case:  my_list.add(3) --- [1](root) <- [2, _](head)
            if len(self.head.elements) < self.head.size:
                self.head.elements.append(new_number)
                return

        # this covers my_list.add(2) --- [1](root) <- [2, _](head)
        # my_list.add(4) [1](root) <- [2, 3] <- [4, _, _, _](head)
        self._add(self.head, new_number)

    def _add(self, node, new_number):
        new_node = Node()
        new_node.size = node.size * 2
        new_node.elements.append(new_number)
        new_node.next = node
        node.tail = new_node
        self.head = new_node

    def get(self, index):
        if index == 0:
            return self.root.elements[0]

        tmp = self.head
        total_elements = self.get_total_elements()
        while tmp is not None:
            for element in tmp.elements:
                if total_elements == index:
                    return element
                total_elements -= 1
            tmp = tmp.next

    def get_total_elements(self):
        n = int(math.sqrt(self.head.next.size))
        powers = [2**i for i in range(0, n + 1)]
        total = sum(powers) + len(self.head.elements)
        return total

    def get_from_root(self, index):
        if index == 0:
            return self.root.elements[0]

        i_counter = 0
        tmp = self.root
        while tmp is not None:
            for element in tmp.elements:
                if i_counter == index:
                    return element
                i_counter += 1

            tmp = tmp.tail
        return 'not found'

        # index -> 3, must get me 6
        # must retrieve from right to left
        # [3] <- [6, 9] <- [12, 15 ,16 ,19 ]                <- [12, 15 ,16 ,19, 12, 15 ,16 ,19 ]
        #                       4

        # I've got Size of self.head and I have how many elements that node has.

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print('Node: {}'.format(tmp.elements))
            tmp = tmp.next


# This should be the end goal:
my_list = SpecialLinkedList()

for i in range(0, 7):
    my_list.add(i)
my_list.print_list()
#my_list.get_total_elements()
assert my_list.get(2) == 2, 'Fuck, got number {}, expected: {}'.format(my_list.get(2), my_list.get_from_root(2))
