import torch


def load_mnist(is_train=True, flatten=True):
    from torchvision import datasets, transforms

    dataset = datasets.MNIST('../../data', train=is_train, transform=transforms.Compose([transforms.ToTensor()]))

    X = dataset.data.float() / 255.
    y = dataset.targets

    if flatten:
        X = X.reshape(X.size(0), -1)

    return X, y


def split_data(X, y, train_ratio=.8):
    train_cnt = int(X.size(0) * train_ratio)
    valid_cnt = X.size(0) - train_cnt
    cnts = [train_cnt, valid_cnt]

    indices = torch.randperm(X.size(0))
    X = torch.index_select(X, dim=0, index=indices).split(cnts, dim=0)
    y = torch.index_select(y, dim=0, index=indices).split(cnts, dim=0)

    return X, y


def get_hidden_sizes(input_size, output_size, n_layers):
    step_size = int((input_size - output_size) / n_layers)

    hidden_sizes = []
    current_size = input_size
    for i in range(n_layers - 1):
        hidden_sizes += [current_size - step_size]
        current_size = hidden_sizes[-1]

    return hidden_sizes
