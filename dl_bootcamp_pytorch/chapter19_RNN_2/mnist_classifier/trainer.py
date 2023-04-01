from copy import deepcopy
import numpy as np
import torch
import torch.nn as nn

class Trainer():
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
    
    def _train(self, X, y, config):
        self.model.train()

        X, y = self._batchify(X, y, batch_size=config.batch_size, random_split=True)
        total_loss = 0

        for i, (X_i, y_i) in enumerate(zip(X, y)):
            y_hat_i = self.model(X_i)
            loss_i = self.crit(y_hat_i, y_i)

            self.optimizer.zero_grad()
            loss_i.backward()
            self.optimizer.step()

            if config.verbose >= 2:
                print(f'Train Iteration {i + 1}/{len(X)}: loss={float(loss_i):.6f}')

            total_loss += float(loss_i)
        
        return total_loss / len(X)
    
    def _validate(self, X, y, config):
        self.model.eval()

        X, y = self._batchify(X, y, batch_size=config.batch_size, random_split=False)
        total_loss = 0

        with torch.no_grad():
            for i, (X_i, y_i) in enumerate(zip(X, y)):
                y_hat_i = self.model(X_i)
                loss_i = self.crit(y_hat_i, y_i)

                if config.verbose >= 2:
                    print(f'Valid Iteration {i + 1}/{len(X)}: loss={float(loss_i):.6f}')

                total_loss += float(loss_i)
        
        # 원본은 한칸 뒤에 있던데, 상관없더라도 여기가 맞을 것 같은데?
        return total_loss / len(X)
    
    def train(self, train_data, valid_data, config):
        lowest_loss = np.inf
        best_model = None

        for i in range(config.n_epochs):
            train_loss = self._train(train_data[0], train_data[1], config)
            valid_loss = self._validate(valid_data[0], valid_data[1], config)

            if valid_loss < lowest_loss:
                lowest_loss = valid_loss
                best_model = deepcopy(self.model.state_dict())
            
            print(print(f'Epoch {i + 1}/{config.n_epochs}: train_loss={train_loss:.6f}  valid_loss={valid_loss:.6f}  lowest_loss={lowest_loss:.6f}'))

        self.model.load_state_dict(best_model)