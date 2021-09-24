# HUtils
a comprehensive utils.

estimate_utils：
===
1.calculating FPR@95 recall rate.
```python
get_fpr_at_95_recall(labels, scores)
```
2.calculating mean and standard deviate of dataset.
```python
get_mean_and_std(train_data)
```
3.generate a 2-D figure.
```python
gen_performance_plot(data, x_label, y_label, title)
```

file_utils：
===
Help on module file_utils:
```python
NAME
    file_utils

FUNCTIONS
    read_csv(path, file_name)
        read csv file.
        :param path: where the file is.
        :param file_name: the file name.
        :return: return the result of reading file.

    read_csv_path(path)
        read csv file.
        :param path: where the file is.
        :return: return the result of reading file.

    save_csv_file(dataset, path, file_name, header=True, index=False)
        save data into a file
        :param dataset: the data needed to save.
        :param path: where you want to save the file.
        :param file_name: the file name.
        :param header: whether saving the header.
        :param index: whether saving the index.
        :return: whether it is success.

    tif2png_cv(original_path, saved_path)
        transform tif file into png via CV package.
        :param original_path: the path of tif file.
        :param saved_path: the saved path of png file.
        :return: none

    tif2png_pil(original_path, saved_path)
        transform tif file into png via PIL package.
        :param original_path: the path of tif file.
        :param saved_path: the saved path of png file.
        :return: none
```

Usage
===
Add the utils you need to your project and then just use it.
