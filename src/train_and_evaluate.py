# load train test files
# Train algorithm
# Save metrics and parameters

import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib                          # to save the models
import json


def evaluate_metrics(actual, predicted):
    rmse = mean_squared_error(actual, predicted)
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)
    return rmse, r2, mae


def train_and_evaluate(config_path):
    config = read_params(config_path)

    # While running using main function  use this line

    # train_data_path = os.path.join(os.path.split(os.getcwd())[0], config["split_data"]["train_path"])
    # test_data_path = os.path.join(os.path.split(os.getcwd())[0], config["split_data"]["test_path"])
    # model_dir = os.path.join(os.path.split(os.getcwd())[0], config["model_dir"])
    # params_json_path = os.path.join(os.path.split(os.getcwd())[0], config["report"]["params"])
    # scores_json_path = os.path.join(os.path.split(os.getcwd())[0], config["report"]["scores"])

    # While running through dvc repo command use this line

    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    model_dir = config["model_dir"]
    params_json_path = config["reports"]["params"]
    scores_json_path = config["reports"]["scores"]

    test_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    lr = ElasticNet(alpha=alpha,
                    l1_ratio=l1_ratio,
                    random_state=random_state)
    lr.fit(train_x, train_y)

    predict_qualities = lr.predict(test_x)

    (rmse, mae, r2) = evaluate_metrics(test_y, predict_qualities)

    print("ElasticNet model(alpha=%f,l1_ratio=%f)" % (alpha, l1_ratio))
    print("RMSE %s" % rmse)
    print("MAE %s" % mae)
    print("R2 %s" % r2)

    with open(scores_json_path, 'w') as f:
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        json.dump(scores, f, indent=4)

    with open(params_json_path, 'w') as f:
        params = {
            "alpha": alpha,
            "l1_ratio": l1_ratio,
        }
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(lr, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=os.path.join(os.path.split(os.getcwd())[0], "params.yaml"))
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)