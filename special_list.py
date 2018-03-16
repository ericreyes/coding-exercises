
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

    def add(self, new_number):
        # We have a the structure like: [1]
        if self.root is None:
            new_node = Node()
            new_node.size = 1
            new_node.elements.append(new_number)
            self.head = new_node
            self.root = new_node
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
        self.head = new_node

    def get(self, index):
        # index -> 3, must get me 6
        # must retrieve from right to left
        # [3] <- [6, 9] <- [12, , , ]




        if index == 1:
            return self.root.elements[0]

        all_elements = []
        while self.head is not None:
            self.head.elements.reverse()
            all_elements.extend(self.head.elements)
            self.head = self.head.next
        print('get element from right to left with index {}, result: {}'.format(index, all_elements[-index]))
        return all_elements[-index]

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print('Node: {}'.format(tmp.elements))
            tmp = tmp.next


# This should be the end goal:
my_list = SpecialLinkedList()

for i in range(0, 100, 3):
    my_list.add(i)
my_list.print_list()
my_list.get(10)
# my_list.add(1)
# assert my_list.head.elements[0] == 1



