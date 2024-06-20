# Câu hỏi 3c: Hoàn thành đoạn code sau đây theo công thức tính softmax.
import torch
import torch . nn as nn


class MySoftmax (nn . Module):
    def __init__(self):
        super() . __init__()

    def forward(self, x):
        # Your Code Here
        result = torch.exp(x)/torch.sum(torch.exp(data))
        return result


    # End Code Here
if __name__ == '__main__':
    data = torch . Tensor([1, 2, 300000000])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    assert round(output[0]. item(), 2) == 0.0
    print(output)
