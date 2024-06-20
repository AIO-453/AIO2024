class MyQueue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return "True"
        else:
            return "False"

    def is_full(self):
        if len(self.queue) == self.capacity:
            return "True"
        else:
            return "False"

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        else:
            return self.queue.pop(0)

    def enqueue(self, value):
        if len(self.queue) == self.capacity:
            return "Queue is full"
        else:
            self.queue.append(value)

    def front(self):
        return self.queue[0]


if __name__ == '__main__':
    queue1 = MyQueue(capacity=5)
    queue1 . enqueue(1)
    queue1 . enqueue(2)
    print(queue1 . is_full())
    print(queue1 . front())
    print(queue1 . dequeue())
    print(queue1 . front())
    print(queue1 . dequeue())
    print(queue1 . is_empty())
