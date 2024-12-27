class Node:
    """Класс узел с данными и ссылкой на следующий узел"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс очередь с головой, хвостом и её размером"""

    def __init__(self, head=None, tail=None, size_of_queue=4):
        self.head = head
        self.tail = tail
        self.size_of_queue = size_of_queue
        self.counter = 0

    def enqueue(self, data):
        """Метод добавления элемента в очередь"""
        if self.counter < self.size_of_queue:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                self.tail.next_node = new_node
            self.tail = new_node
            self.counter += 1
            return 'ok'
        else:
            return 'queue is overflow'

    def dequeue(self):
        """Метод удаления элемента из очереди"""
        if self.head is None:
            return 'уже и так пусто'
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
            return dequeue_item.data

    def is_empty(self):
        """Проверка очереди на пустоту"""
        if self.head is None:
            return True
        else:
            return False

    def get_queue_len(self):
        """Получение длины очереди"""
        items_counter = 0
        if self.head is None:
            return items_counter
        return self.counter

    def is_full(self):
        """Проверка очереди на заполненность """
        if self.size_of_queue == self.get_queue_len():
            return True, print("очередь полна")
        else:
            return False, print("очередь не полна")

    def show_queue(self):
        if not self.is_empty():
            temp_head = self.head
            while temp_head:
                print(temp_head.data, end=' ')
                temp_head = temp_head.next_node
            return f'  :очередь перед вами, она состоит из {self.get_queue_len()} элементов'
        return f'пустота..... ,{self.get_queue_len()} элементов'


if __name__ == '__main__':
    q1 = Queue()
    print(q1.enqueue('A'))
    print(q1.enqueue('B'))
    print(q1.enqueue('C'))
    print(q1.enqueue('D'))
    print(q1.enqueue('E'))
    # print(q1.enqueue('F'))
    print()
    print(q1.is_empty())
    print(q1.is_full())
    print()
    print(q1.show_queue())
    print()
    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
    print()
    print(q1.is_empty())
    print(q1.is_full())
    print()
    print(q1.show_queue())
