from class_Queue import Node, Queue

main_queue = Queue()


def choice(number, queue):
    if number == 1:
        result = queue.is_empty()
        if result:
            print('очередь пуста')
        else:
            print('очередь не пуста')
    elif number == 2:
        result_2 = queue.is_full()
        print(result_2)
        if result_2:
            print('очередь заполнена')
        else:
            print('очередь не заполнена')
    elif number == 3:
        if queue.is_full():
            print('очередь заполнена')
            return
        else:
            return queue.enqueue(input('введите данные: '))
    elif number == 4:
        return queue.dequeue()
    elif number == 5:
        return queue.show_queue()
    else:
        return 'ваше число не верно'


user_choice = int(input(
    'Сделайте ваш выбор:\n1: IsEmpty — проверка очереди на пустоту;\n2: IsFull — проверка очереди на заполнение;\n3: Enqueue — добавление элемента в очередь;\n4: Dequeue — удаление элемента из очереди;\n5: Show — отображение всех элементов очереди на экран;\n0: Выход!\n:'))
while user_choice != 0:
    choice(user_choice, main_queue)
    user_choice = int(input('\nваш выбор: '))
else:
    print('До свидания ')
