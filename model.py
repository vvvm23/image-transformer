import torch
import torch.nn as nn
import torch.nn.functional as F

class ImageTransformer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x

if __name__ == '__main__':
    model = ImageTransformer()
    x = torch.randn(1, 3, 32, 32)
    y = model(x)
    print(y)
    print("Input Shape:\t", x.shape)
    print("Output Shape:\t", y.shape)
