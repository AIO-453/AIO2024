# 3. Thực hiện xây dựng class Stack với các phương thức (method) sau đây
class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None for _ in range(self.capacity)]
        # print(self.stack)

    def is_empty(self):
        if self.stack == [None for _ in range(self.capacity)]:
            return "True"
        else:
            return "False"

    def is_full(self):
        if self.stack.count(None) == 0:
            return "True"
        else:
            return "False"

    def pop(self):
        if self.stack[-1] == None:
            result = self.stack[self.stack.index(None)-1]
            self.stack[self.stack.index(None)-1] = None
            return result
        else:
            result = self.stack[-1]
            self.stack[self.capacity-1] = None
            return result

    def push(self, item):
        if self.is_full() != "True":
            self.stack.insert(self.stack.index(None), item)
            self.stack.pop(-1)
        else:
            print("stack is full")

    def top(self):
        if self.is_full() != "True":
            result = self.stack[self.stack.index(None)-1]
            return result
        else:
            result = self.stack[-1]
            return result


if __name__ == '__main__':
    stack1 = MyStack(capacity=5)
    stack1 . push(1)
    stack1 . push(2)
    print(stack1 . is_full())
    print(stack1 . top())
    print(stack1 . pop())
    print(stack1 . top())
    print(stack1 . pop())
    print(stack1 . is_empty())
