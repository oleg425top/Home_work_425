class Node:
    """инициализируем узел, с данными, и ссылкой на след. узел"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """инициализируем стек с его максимальным размером"""
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """метод добавления элементов в стек"""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стек переполнен")
            return "Стек переполнен"

    def pop(self):
        """метод удаления элементов из стека"""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стек пуст"

    def is_empty(self):
        """метод проверки стека на пустоту. Возвращает bool"""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """метод проверки стека на заполненность"""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """метод очистки стека"""
        while self.top:
            self.pop()

    def get_data(self, index):
        """метод получения элемента стека по индексу"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """метод определения размера стека"""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """метод подсчета целых чисел в стеке"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter

# node = Node(5)
# node_2 = Node(6, node)
# print(node.data)
# print(node_2.next_node.data)
# stack = Stack()
# stack.push(1)
# stack.push("sta")
# stack.push(2)
# stack.push(2.5)
# stack.push(5)
# print(stack.get_data(0))
# stack.push("sta")
# print(stack.counter_int())
