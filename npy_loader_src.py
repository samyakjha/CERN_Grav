import torch
import numpy as np
import torchvision.transforms as transforms

def npy_loader(path):
    sample = torch.from_numpy(np.load(path))
    return sample