import torch
import torch.nn as nn

class ConvolutionBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        self.in_channels = in_channels
        self.out_channels = out_channels

        super().__init__()

        self.layers = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=(3, 3), padding=1),
            nn.LeakyReLU(),
            nn.BatchNorm2d(out_channels),
            nn.Conv2d(out_channels, out_channels, kernel_size=(3, 3), padding=1, stride=2),
            nn.LeakyReLU(),
            nn.BatchNorm2d(out_channels)
        )

    def forward(self, X):
        y = self.layers(X)
        return y
    
class ConvolutionalClassifier(nn.Module):
    def __init__(self, output_size):
        self.output_size = output_size

        super().__init__()

        self.blocks = nn.Sequential(
            ConvolutionBlock(1, 32),
            ConvolutionBlock(32, 64),
            ConvolutionBlock(64, 128),
            ConvolutionBlock(128, 256),
            ConvolutionBlock(256, 512)
        )
        self.layers = nn.Sequential(
            nn.Linear(512, 50),
            nn.LeakyReLU(),
            nn.BatchNorm1d(50),
            nn.Linear(50, output_size),
            nn.LogSoftmax(dim=-1)
        )

    def forward(self, X):
        assert X.dim() > 2, 'Dimension Error: Dimension should be greater than 2'

        if X.dim() == 3:
            X = X.reshape(-1, 1, X.shape[-2], X.shape[-1])
        z = self.blocks(X)
        y = self.layers(z.squeeze())

        return y
