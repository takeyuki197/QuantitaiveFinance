import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class FeedForwardNetwork(nn.Module):
    def __init__(self, input_size=1, 
                 output_size=1, hidden_size=32):
        nn.Module.__init__(self)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        self.fc4 = nn.Linear(hidden_size, hidden_size)
        self.output = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        x = F.leaky_relu(self.fc1(x))
        x = F.leaky_relu(self.fc2(x))
        x = F.leaky_relu(self.fc3(x))
        x = F.leaky_relu(self.fc4(x))
        x = self.output(x)
        return x