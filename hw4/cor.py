import numpy as np


def correlate_Pirson(first_list: list, second_list: list):
    return np.corrcoef(first_list, second_list)
