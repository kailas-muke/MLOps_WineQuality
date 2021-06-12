# Split raw data
# Save it in data/processed folder

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params
import argparse


def split_and_save_data(config_path):
    config = read_params(config_path)

    # While running using main function  use this line

    # train_data_path = os.path.join(os.path.split(os.getcwd())[0], config["split_data"]["train_path"])
    # test_data_path = os.path.join(os.path.split(os.getcwd())[0], config["split_data"]["test_path"])
    # raw_data_path = os.path.join(os.path.split(os.getcwd())[0], config["load_data"]["raw_dataset_csv"])

    # While running through dvc repo command use this line

    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]

    test_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(raw_data_path, sep=",")
    train, test = train_test_split(df, random_state=random_state, test_size=test_ratio)

    train.to_csv(train_data_path, sep=',', index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=',', index=False, encoding="utf-8")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=os.path.join(os.path.split(os.getcwd())[0], "params.yaml"))
    parsed_args = args.parse_args()
    split_and_save_data(config_path=parsed_args.config)