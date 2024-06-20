# câu 9 b
class MyStack:
    def __init__(self, capacity):
        self . __capacity = capacity
        self . __stack = []

    def is_full(self):
        return len(self . __stack) == self . __capacity

    def push(self, value):
        # Your Code Here
        if self.is_full():
            raise OverflowError("Push to a full stack")
        self.__stack.append(value)


    # End Code Here
if __name__ == '__main__':
    stack1 = MyStack(capacity=5)
    stack1 . push(1)
    assert stack1 . is_full() == False
    stack1 . push(2)
    print(stack1 . is_full())
