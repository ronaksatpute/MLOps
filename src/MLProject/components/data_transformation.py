import os
import src.MLProject as logger
from src.MLProject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

        train_data_path = os.path.join(self.config.root_dir, "train.csv")
        test_data_path = os.path.join(self.config.root_dir, "test.csv")

        train_data.to_csv(train_data_path, index=False)
        test_data.to_csv(test_data_path, index=False)

        print(f"Train and test data saved at {train_data_path} and {test_data_path} respectively.")
        print(train_data.shape)
        print(test_data.shape)