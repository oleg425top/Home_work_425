import unittest

from stack import Node, Stack

class TestNode(unittest.TestCase):
    test_node = Node('test_data')


    def test_01_node_init(self):
        self.assertEqual(TestNode.test_node.data, 'test_data')

class TestStack(unittest.TestCase):
    test_stack = Stack(2)

    def test_02_stack_init(self):
        self.assertEqual(TestStack.test_stack.stack_size, 2)

    def test_03_push(self):
        self.assertEqual(TestStack.test_stack.push(10), None)
        self.assertEqual(TestStack.test_stack.push(11), None)
        self.assertEqual(TestStack.test_stack.push(12), 'Стек переполнен')

    def test_04_is_full(self):
        self.assertEqual(TestStack.test_stack.is_full(), True)

    def test_05_pop(self):
        self.assertEqual(TestStack.test_stack.pop(), 11)
        self.assertEqual(TestStack.test_stack.pop(), 10)
        self.assertEqual(TestStack.test_stack.pop(), 'Стек пуст')

    def test_06_is_full(self):
        self.assertEqual(TestStack.test_stack.is_full(), False)


    def test_07_is_empty(self):
        self.assertEqual(TestStack.test_stack.is_empty(), True)

    def test_08_clear_stack(self):
        self.assertEqual(TestStack.test_stack.clear_stack(), None)
        self.assertEqual(TestStack.test_stack.is_empty(), True)







