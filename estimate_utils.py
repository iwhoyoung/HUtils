import operator

# deepbit performance index
import numpy as np
import torch
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader


def get_fpr_at_95_recall(labels, scores):
    recall_point = 0.95
    # Sort label-score tuples by the score in descending order.
    temp = zip(labels, scores)
    # operator.itemgetter(1)按照第二个元素的次序对元组进行排序，reverse=True是逆序，即按照从大到小的顺序排列
    # sorted_scores.sort(key=operator.itemgetter(1), reverse=True)
    sorted_scores = sorted(temp, key=operator.itemgetter(1), reverse=True)

    # Compute error rate
    # n_match表示测试集正样本数目
    n_match = sum(1 for x in sorted_scores if x[0] == 1)
    n_thresh = recall_point * n_match
    tp = 0
    count = 0
    for label, score in sorted_scores:
        count += 1
        if label == 1:
            tp += 1
        if tp >= n_thresh:
            break
    return float(count - tp) / (len(sorted_scores) - n_match)


# calculate mean and standard deviate of dataset
def get_mean_and_std(train_data):
    """
    Compute mean and variance for training data
    :param train_data: 自定义类Dataset(或ImageFolder即可)
    :return: (mean, std)
    """
    print('Compute mean and variance for training data.')
    print(len(train_data))
    train_loader = torch.utils.data.DataLoader(
        train_data, batch_size=1, shuffle=False, num_workers=0,
        pin_memory=True)
    mean = torch.zeros(3)
    std = torch.zeros(3)
    for X, _ in train_loader:
        for d in range(3):
            mean[d] += X[:, d, :, :].mean()
            std[d] += X[:, d, :, :].std()
    mean.div_(len(train_data))
    std.div_(len(train_data))
    print("mean:",list(mean.numpy())," std:",list(std.numpy()))
    return list(mean.numpy()), list(std.numpy())


def gen_performance_plot(data, x_label, y_label, title):
    plt.plot(data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    # plt.grid()
    # plt.legend()
    plt.savefig("performance.jpg")
    plt.clf()

