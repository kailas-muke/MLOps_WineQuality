# We will do below task
# Read data from data source
# Save in data/raw for further process

import os
from get_data import read_params, get_data
import argparse


def load_and_save(config_path):
    config = read_params(config_path=config_path)
    df = get_data(config_path)
    new_cols = [str(col).replace(" ", "_") for col in df.columns]  # To avoid the space in the column name which can create issue further
    print("New columns are", new_cols)

    # While running using main function  use this line
    #  raw_data_path = os.path.join(os.path.split(os.getcwd())[0], config["load_data"]["raw_dataset_csv"])

    # While running through dvc repo command use this line
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=',', index=False, header=new_cols)  # save the data in csv file


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=os.path.join(os.path.split(os.getcwd())[0], "params.yaml"))
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)