from class_Queue import Node, Queue

main_queue = Queue()


def choice(number, queue):
    if number == 1:
        result = queue.is_empty()
        if result:
            print('очередь пуста')
        else:
            print('очередь не пуста')
    if number == 2:
        result_2 = queue.is_full()
        if result_2:
            print('очередь заполнена')
        else:
            print('очередь не заполнена')
    if number == 3:
        full = queue.is_full()
        if full:
            print('очередь уже заполнена')
            return
        else:

            return queue.enqueue(input('введите данные: ')), print('данные введены')
    if number == 4:
        return queue.dequeue()
    if number == 5:
        return queue.show_queue()


user_choice = int(input(
    'Сделайте ваш выбор:\n1: IsEmpty — проверка очереди на пустоту;\n2: IsFull — проверка очереди на заполнение;\n3: Enqueue — добавление элемента в очередь;\n4: Dequeue — удаление элемента из очереди;\n5: Show — отображение всех элементов очереди на экран;\n0: Выход!\n:'))
while user_choice != 0 and user_choice <= 5:
    choice(user_choice, main_queue)
    user_choice = int(input('\nваш выбор: '))
else:
    print('До свидания/ вы ввели некорректные данные ')
