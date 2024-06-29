# 1. Viết class và cài phương thức softmax.
import torch
import torch.nn as nn


class softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        result = torch.exp(x)/torch.sum(torch.exp(data))
        return result


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x)
        result = torch.exp(x - c) / torch.sum(torch.exp(x - c))
        return result


if __name__ == '__main__':
    data = torch . tensor([1, 2, 3])
    softmax = softmax()
    output = softmax(data)
    print(output)

    data = torch . Tensor([1, 2, 3])
    softmax_stable = softmax_stable()
    output = softmax_stable(data)
    print(output)
