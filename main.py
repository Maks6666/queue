# ресторан

from queue import Queue

class OrderQueue:
    def __init__(self):
        self.order_queue = Queue()
    def add_order(self, order):
        self.order_queue.put(order)
        print(f"Order {order} is added to queue")

    def handle_orders(self):
        if not self.order_queue.empty():
            print("Orders handling begins:")
            while not self.order_queue.empty():
                order = self.order_queue.get()
                print(f"Current order: {order}")
            print("All orders are handled.")
        else:
            print("Queue is empty.")


restaurant_queue = OrderQueue()
restaurant_queue.add_order("Pizza")
restaurant_queue.add_order("Steak")
restaurant_queue.add_order("Soup")

restaurant_queue.handle_orders()
