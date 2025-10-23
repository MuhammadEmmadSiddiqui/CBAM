import torch
import torch.nn as nn
import torch.nn.functional as F

class CBAM(nn.Module):
    def __init__(self, channels, reduction=16):
        super(CBAM, self).__init__()
        # Initialize the Channel Attention and Spatial Attention modules
        self.channel_attention = ChannelAttention(channels, reduction)
        self.spatial_attention = SpatialAttention()

    def forward(self, x):
        # Apply channel attention first, then spatial attention
        x = self.channel_attention(x)
        x = self.spatial_attention(x)
        return x

class ChannelAttention(nn.Module):
    def __init__(self, channels, reduction=16):
        super(ChannelAttention, self).__init__()
        # A simple MLP-based channel attention mechanism
        self.mlp = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),  # Global average pooling
            nn.Conv2d(channels, channels // reduction, 1, bias=False),
            nn.ReLU(),
            nn.Conv2d(channels // reduction, channels, 1, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        # Apply the channel attention mechanism to the input tensor
        avg_out = self.mlp(x)
        return x * avg_out  # Scale the input tensor by the attention map

class SpatialAttention(nn.Module):
    def __init__(self):
        super(SpatialAttention, self).__init__()
        # A spatial attention mechanism using a convolutional layer
        self.conv = nn.Conv2d(2, 1, 7, padding=3, bias=False)  # 7x7 convolution
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # Compute the spatial attention map
        avg_out = torch.mean(x, dim=1, keepdim=True)  # Average along channels
        max_out, _ = torch.max(x, dim=1, keepdim=True)  # Max along channels
        combined = torch.cat([avg_out, max_out], dim=1)  # Concatenate avg and max
        attention_map = self.sigmoid(self.conv(combined))  # Apply convolution and sigmoid
        return x * attention_map  # Scale the input tensor by the attention map
