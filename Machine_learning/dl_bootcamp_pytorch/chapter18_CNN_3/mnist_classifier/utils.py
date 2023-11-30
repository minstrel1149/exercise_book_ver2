import torch
from mnist_classifier.models.cnn import ConvolutionalClassifier
from mnist_classifier.models.fc import ImageClassifier

def load_mnist(is_train=True, download=False, flatten=True):
    from torchvision import datasets, transforms

    dataset = datasets.MNIST('../../data', train=is_train, download=download, transform=transforms.Compose([transforms.ToTensor()]))

    X = dataset.data.float() / 255
    y = dataset.targets

    if flatten:
        X = X.reshape(X.shape[0], -1)

    return X, y

def split_data(X, y, train_ratio=0.8):
    train_cnt = int(X.shape[0] * train_ratio)
    valid_cnt = X.shape[0] - train_cnt

    indices = torch.randperm(X.shape[0])
    X = torch.index_select(X, dim=0, index=indices).split([train_cnt, valid_cnt], dim=0)
    y = torch.index_select(y, dim=0, index=indices).split([train_cnt, valid_cnt], dim=0)

    return X, y

def get_hidden_sizes(input_size, output_size, n_layers):
    step_size = int((input_size - output_size) / n_layers)

    hidden_sizes = []
    current_size = input_size
    for _ in range(n_layers - 1):
        hidden_sizes.append(current_size - step_size)
        current_size = hidden_sizes[-1]
    
    return hidden_sizes

def get_model(input_size, output_size, config, device):
    if config.model == 'fc':
        model = ImageClassifier(input_size=input_size, output_size=output_size,
                                hidden_sizes=get_hidden_sizes(input_size, output_size, config.n_layers),
                                use_batch_norm=not config.use_dropout, dropout_p=config.dropout_p).to(device)
    elif config.model == 'cnn':
        model = ConvolutionalClassifier(output_size).to(device)
    else:
        raise NotImplementedError
    
    return model