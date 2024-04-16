# Створіть клас черги з пріоритетами для роботи із символьними значеннями.
# Ви маєте створити реалізації для операцій над еле- ментами черги:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ InsertWithPriority — додати елемент з пріоритетом у
# чергу;
#
# ■ PullHighestPriorityElement — видалення елемента з найвищим пріоритетом із черги;
# ■ Peek — повернення найбільшого за пріоритетом еле- мента. Зверніть увагу, що елемент не видаляється з черги;
# ■ Show — відображення на екрані всіх елементів черги. Показуючи елемент, також необхідно вказати і його пріоритет.
# На старті додатка відобразіть меню, в якому корис- тувач може вибрати необхідну операцію.



from queue import PriorityQueue

class Line:
    def __init__(self):
        self.queue = PriorityQueue()

    def queue_is_empty(self):
        return self.queue.empty()

    def queue_is_full(self):
        return self.queue.full()


    def add_element(self, element, priority):
        self.queue.put((priority, element))

    def delete_element(self):
        if self.queue.empty():
            print("Queue is emtpy")
            return

        priority, element = self.queue.get()

        print(f'Element {element} is deleted')

    def peek(self):
        if not self.queue.empty():
            priority, symbol = self.queue.queue[0]
            print(f"Peek element: {symbol}")
        else:
            print("Queue is empty")

    def show(self):
        if not self.queue.empty():
            for priority, symbol in self.queue.queue:
                print(priority, symbol)
        else:
            return False

line = Line()
print(line.queue_is_empty())
print(line.queue_is_full())

line.add_element(4, "A")
print(line.queue_is_empty())

line.delete_element()
print(line.queue_is_empty())

line.add_element(1, "B")
line.add_element(4, "A")
print(line.peek())

line.show()

