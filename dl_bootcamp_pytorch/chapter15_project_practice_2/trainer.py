from copy import deepcopy
import numpy as np
import torch
import torch.nn as nn

class Trainer(nn.Module):
    def __init__(self, model, optimizer, crit):
        self.model = model
        self.optimizer = optimizer
        self.crit = crit

        super().__init__()

    def _batchify(self, X, y, batch_size=256, random_split=True):
        if random_split:
            indices = torch.randperm(X.shape[0], device=X.device)
            X = torch.index_select(X, dim=0, index=indices)
            y = torch.index_select(y, dim=0, index=indices)
        
        X = X.split(batch_size, dim=0)
        y = y.split(batch_size, dim=0)

        return X, y