import pandas as pd


def tensor2str(tensor_2d):
    """
    convert tensor to string.
    :param tensor_2d: a tensor as input.
    :return: the corresponding string.
    """
    size = tensor_2d.shape
    result = []
    for i in range(size[0]):
        str_tensor = ''
        for j in range(size[1]):
            str_tensor += str(int(tensor_2d[i][j].item()))
        result.append(str_tensor)
    return result


def tensor2df(tensor_2d):
    """
    convert tensor to dataframe.
    :param tensor_2d: a tensor as input.
    :return: the corresponding dataframe.
    """
    size = tensor_2d.shape
    result = pd.DataFrame()
    for i in range(size[0]):
        list_tensor = []
        for j in range(size[1]):
            list_tensor.append('%.3f' % tensor_2d[i][j].item())
        result = result.append([list_tensor], ignore_index=True)
    return result
