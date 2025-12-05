from src.MLProject.entity.config_entity import ModelEvaluationConfig
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.MLProject.utils.common import save_json
from pathlib import Path    

class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig):
        self.model_evaluation_config = model_evaluation_config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):

        test_data_path = pd.read_csv(self.model_evaluation_config.test_data_path)
        model = joblib.load(self.model_evaluation_config.model_path)

        test_x = test_data_path.drop(columns=[self.model_evaluation_config.target_column])
        test_y = test_data_path[self.model_evaluation_config.target_column]

        mlflow.set_registry_uri(self.model_evaluation_config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Save metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(
                path=Path(self.model_evaluation_config.metric_file_name),
                data=scores
            )

            # Log metrics
            mlflow.log_metric("RMSE", rmse)
            mlflow.log_metric("MAE", mae)
            mlflow.log_metric("R2_Score", r2)
            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    model,
                    "model",
                    registered_model_name="ElasticnetModel"
                )
            else:
                mlflow.sklearn.log_model(model, "model")
