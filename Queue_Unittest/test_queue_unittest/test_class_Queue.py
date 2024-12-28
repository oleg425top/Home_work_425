import  unittest
from class_Queue import Node, Queue

class QueueUnittest(unittest.TestCase):
    queue =Queue()
    def test_01_is_empty(self):
        self.assertEqual(QueueUnittest.queue.is_empty(), True)

    def test_02_is_full(self):
        self.assertEqual(QueueUnittest.queue.is_full(), (False, None))

