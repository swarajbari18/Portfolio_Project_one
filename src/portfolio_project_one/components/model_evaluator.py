import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path

from portfolio_project_one.utils.common import save_json
from portfolio_project_one.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_metrics(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)
        return rmse, mae, r2

    def log_metrics_to_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(columns= self.config.target_column)
        y_test = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme   # if we don't have a remote server uri, then this will return file, 
                                                                                # since the mlflow also runs locally
        with mlflow.start_run():

            predictions = model.predict(X_test)
            (rmse, mae, r2) = self.evaluate_metrics(y_test, predictions)

            #  Saving metrics at local machine
            scores = {'rmse': rmse, 'mae': mae, 'r2_score': r2}
            save_json(path= Path(self.config.metric_file_name), data= scores)

            #  logging metrics to mlflow
            mlflow.log_metric("Root Mean Squared Error", rmse)
            mlflow.log_metric("Mean Absolute Error", mae)
            mlflow.log_metric("R2 Square", r2)

            # Model Registry does not work with file store
            if tracking_url_type_store != "file":
                #  Register the model
                #  There are several other ways to use Model Registry as well
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")

            else:
                mlflow.sklearn.log_model(model, "model")