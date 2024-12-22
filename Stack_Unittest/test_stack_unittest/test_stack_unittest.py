import unittest

from stack import Node, Stack

class TestStack(unittest.TestCase):
    test_stack = Stack(5)
    test_node = Node('test_data')


    def test_01_node_init(self):
        self.assertEqual(TestStack.test_node.data, 'test_data')




