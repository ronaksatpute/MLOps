from src.MLProject.config.configuration import ConfigurationManager
from src.MLProject.components.data_validation import DataValidation
from src.MLProject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)
        data_validation_status = data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e