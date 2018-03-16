# To find out if a user is in a certain city, we have to see if they are between IP1 and IP2
# Implement a data structure that can hold 2 IPs and a city. IP format:  255.255.255.255

tuples_list = [('10.0.0.0', '15.0.0.0', 'Boston'),
               # ('20.0.0.0', '25.0.0.0', 'NY'),
               ('9.255.255.255', '9.0.0.0', 'Germany'),
               ('30.0.0.0', '35.0.0.0', 'Mexico'),
               # ('5.0.0.0', '6.0.0.0', 'Cairo'),
               ('253.0.0.0', '255.0.0.0', 'France'),
               ('255.0.0.1', '255.0.0.5', 'Ucrania'),
               ]


class Node(object):
    '''docstring for Node'''
    def __init__(self, ip, city):
        super(Node, self).__init__()
        self.ip = ip
        self.city = city

        self.left = None
        self.right = None


class BinaryTree(object):
    '''docstring for BinaryTree
    root: Node
    The root of the tree which is of class Node
    '''

    def __init__(self):
        super(BinaryTree, self).__init__()
        self.root = None
        self.number_of_nodes = 0

    def add(self, node):
        if self.root is None:
            self.root = node
            self.number_of_nodes = 1
        else:
            self.number_of_nodes += 1
            self._add(self.root, node)

    def _add(self, node, new_node):
        if is_node_greater_than_new_node(node.ip, new_node.ip):
            if node.left is None:
                node.left = new_node
                print ('added ' + new_node.city + ' to left child for ' + node.city)
            else:
                self._add(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
                print ('added ' + new_node.city + ' to right child for ' + node.city)
            else:
                self._add(node.right, new_node)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        print 'number of nodes: ', self.number_of_nodes

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print node.ip + ' ' + node.city + ' '
            self._print_tree(node.right)

    def find_node(self, ip):
        if self.root is not None:
            return self._find_node(self.root, ip)

    def _find_node(self, node, ip):
        if node is not None:
            if node.ip == ip:
                return node
            else:
                return self._find_node(node.left, ip) or self._find_node(node.right, ip)

    def find_city_from_ip(self, ip):
        if self.root is not None:
            return self._find_city_from_ip(self.root, ip)

    def _find_city_from_ip(self, node, ip):
        if node is not None:
            if is_ip_in_range(ip, node.ip, node.left.ip):
                return node.left.city
            elif is_ip_in_range(ip, node.ip, node.right.ip):
                return node.right.city
            else:
                return self._find_city_from_ip(node.left, ip) or self._find_city_from_ip(node.right, ip)


def is_ip_in_range(ip, ip1, ip2):
    ip_list = ip.split('.')
    ip1_list = ip1.split('.')
    ip2_list = ip2.split('.')
    for ip1_number, ip2_number, ip_number in zip(ip1_list, ip2_list, ip_list):
        print ip_number, ip1_number, ip2_number
        if ip_number >= ip1_number and ip_number <= ip2_number:
            return True
    return False


def is_node_greater_than_new_node(ip1, ip2):
    ip1_list = ip1.split('.')
    ip2_list = ip2.split('.')

    for ip1_number, ip2_number in zip(ip1_list, ip2_list):
        if int(ip1_number) > int(ip2_number):
            return True
    return False


def make_tree():
    root = Node('20.0.0.0', 'NY')
    tree = BinaryTree()

    tree.add(root)
    for tupl in tuples_list:
        node1 = Node(tupl[0], tupl[2] + '1')
        node2 = Node(tupl[1], tupl[2] + '2')
        tree.add(node1)
        tree.add(node2)
    return tree

tree = make_tree()
node = tree.find_node('9.255.255.255')
# print (node.city)

ip_to_find = '255.0.0.3'
print 'Found user in {} with IP {}'.format(tree.find_city_from_ip(ip_to_find), ip_to_find)
