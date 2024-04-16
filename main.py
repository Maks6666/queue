# Створіть клас черги для роботи із символьними зна- ченнями. Ви маєте створити реалізації для операцій над елементами:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.
# На старті додатка відобразіть меню, в якому корис- тувач може вибрати необхідну операцію.


from queue import Queue

class Line:
    def __init__(self):
        self.queue = Queue()

    def queue_is_empty(self):
        return self.queue.empty()

    def queue_is_full(self):
        return self.queue.full()

    def add_element(self, element):
        self.queue.put(element)

    def remove_element(self):
        if not self.queue.empty():
            return self.queue.get()
        else:
            return None

    def print(self):
        temp_queue = Queue()

        while not self.queue.empty():
            client = self.queue.get()
            print(client, end=' <- ')
            temp_queue.put(client)


line = Line()
print(line.queue_is_empty())
print(line.queue_is_full())

line.add_element(5)
print(line.queue_is_empty())


line.remove_element()
print(line.queue_is_empty())

line.add_element(3)
line.add_element(2)
line.remove_element()
line.add_element(1)
line.print()