# câu 12 a
class MyQueue:
    def __init__(self, capacity):
        self . __capacity = capacity
        self . __queue = []

    def isEmpty(self):
        return len(self . __queue) == 0

    def is_full(self):
        return len(self . __queue) == self . __capacity

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self . __queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        else:
            self . __queue.append(value)

    def front(self):
        # Your Code Here
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self . __queue[0]
    # End Code Here


if __name__ == '__main__':
    queue1 = MyQueue(capacity=5)
    queue1 . enqueue(1)
    assert queue1 . is_full() == False
    queue1 . enqueue(2)
    print(queue1 . front())
