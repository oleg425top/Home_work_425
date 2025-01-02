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
    test_ll_2 = LinkedList()
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

    def test_04_insert_at_end(self):
        self.assertEqual(TestLinkedList.test_ll_2.insert_at_end('end_data_2'), None)
        self.assertEqual(TestLinkedList.test_ll_2.head.data, 'end_data_2')
        self.assertEqual(TestLinkedList.test_ll.insert_at_end('end_data_1'), 'Узел с данными end_data_1 добавлен в конец списка')
        self.assertEqual(TestLinkedList.test_ll.head.next_node.next_node.data, 'end_data_1')

    def test_05_remove_node_position(self):
        self.assertEqual(TestLinkedList.test_ll.remove_node_position(3), 'Удален узел с данными end_data_1 позиции 3')
        self.assertEqual(TestLinkedList.test_ll.remove_node_position(6),'Ничего не удалено')

    def test_06_insert_at_position(self):
        self.assertEqual(TestLinkedList.test_ll.insert_at_position('insert_data2', 2), 'Узел с данными insert_data2 добавлен на позицию 2')
        self.assertEqual(TestLinkedList.test_ll_2.insert_at_position('insert_data3', 1), 'Узел с данными insert_data3 добавлен на позицию 1')

    def test_07_print_ll(self):
        self.assertEqual(TestLinkedList.test_ll.print_ll(), 'Данные списка выведены')

    def test_08_get(self):
        self.assertEqual(TestLinkedList.test_ll.get('insert_data3'), (False, None))
        self.assertEqual(TestLinkedList.test_ll.get('insert_data2'), (True, 'insert_data2'))

    def test_09_change_data(self):
        self.assertEqual(TestLinkedList.test_ll.change_data('insert_data2', 'insert_data3'), 'Заменены данные в узле № 2')
        self.assertEqual(TestLinkedList.test_ll.change_data('insert_data2', 'insert_data5'), 'Данные не обнаружены')