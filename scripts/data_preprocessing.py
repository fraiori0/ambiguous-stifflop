import pandas as pd
import numpy as np
import os
import sklearn as sk


# path to this file
local_dir = os.path.dirname(os.path.abspath(__file__))


def load_data():
    """
    Load the data from the resources/datasets folder
    :return: train_data, test_data
    """
    data_dir = os.path.join(
        local_dir,
        os.pardir,
        "resources",
        "datasets",
    )
    test_data = pd.read_csv(os.path.join(data_dir, "test_data.csv"), index_col=0)
    train_data = pd.read_csv(os.path.join(data_dir, "train_data.csv"), index_col=0)
    return train_data, test_data
