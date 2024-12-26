import unittest
from LinkedListClass import Node, LinkedList

class TestNode(unittest.TestCase):

    def test_01_node_init(self):
        test_node = Node('test_data')
        self.assertEqual(test_node.data, 'test_data')
        self.assertEqual(test_node.next_node, None)
        test_node_2 = Node('test_data_2', test_node)
        self.assertEqual(test_node_2.data, 'test_data_2')
        self.assertEqual(test_node_2.next_node, test_node)
        self.assertEqual(test_node_2.next_node.data, 'test_data')

class TestLinkedList(unittest.TestCase):
    test_ll = LinkedList()
    def test_02_Ll_init(self):

        self.assertEqual(TestLinkedList.test_ll.head, None)

    def test_03_insert_at_head(self):
        self.assertEqual(TestLinkedList.test_ll.insert_at_head('test_data_2'),
                         'Узел с данными test_data_2 добавлен в начало списка')
        self.assertEqual(TestLinkedList.test_ll.head.data, 'test_data_2')
        self.assertEqual(TestLinkedList.test_ll.head.next_node, None)
        self.assertEqual(TestLinkedList.test_ll.insert_at_head('test_data_3'),
                         'Узел с данными test_data_3 добавлен в начало списка')
        self.assertEqual(TestLinkedList.test_ll.head.next_node.data, 'test_data_2')