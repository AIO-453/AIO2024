# Câu hỏi 11a:
class MyQueue:
    def __init__(self, capacity):
        self . __capacity = capacity
        self . __queue = []

    def is_full(self):
        return len(self . __queue) == self . __capacity

    def enqueue(self, value):
        # Your Code Here
        if len(self . __queue) == self . __capacity:
            return "Queue is full"
        else:
            self . __queue.append(value)
    # End Code Here


if __name__ == '__main__':
    queue1 = MyQueue(capacity=5)
    queue1 . enqueue(1)
    assert queue1 . is_full() == False
    queue1 . enqueue(2)
    print(queue1 . is_full())
