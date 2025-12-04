import os
from box.exceptions import BoxValueError
import yaml
from src.MLProject import logger
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error converting YAML content to ConfigBox: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    


def create_directories(path_to_directories: list) -> None:
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")



def save_json(path: Path, data: Any) -> None:
    """Saves data to a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (Any): The data to save.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully saved to JSON file at: {path}")
    except Exception as e:
        logger.error(f"Error saving data to JSON file: {e}")
        raise e
    


def load_json(path: Path) -> Any:
    """Loads data from a JSON file.

    Args:
        path (Path): The path to the JSON file.
    Returns:
        Any: The data loaded from the JSON file.
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Data successfully loaded from JSON file at: {path}")
            return data
    except Exception as e:
        logger.error(f"Error loading data from JSON file: {e}")
        raise e 
    


def save_bin(path: Path, data: Any) -> None:
    """Saves data to a binary file using joblib.

    Args:
        path (Path): The path to the binary file.
        data (Any): The data to save.
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Data successfully saved to binary file at: {path}")
    except Exception as e:
        logger.error(f"Error saving data to binary file: {e}")
        raise e
    


def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.
    Returns:
        Any: The data loaded from the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Data successfully loaded from binary file at: {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from binary file: {e}")
        raise e
    


def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes.

    Args:
        path (Path): The path to the file.
    Returns:
        str: The size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"File size for {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"
