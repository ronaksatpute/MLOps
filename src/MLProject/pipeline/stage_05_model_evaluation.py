from src.MLProject.config.configuration import ConfigurationManager
from src.MLProject.components.model_evaluation import ModelEvaluation
from src.MLProject import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        
        # create the component instance
        model_evaluation = ModelEvaluation(model_evaluation_config=model_evaluation_config)
        # run evaluation
        model_evaluation.log_into_mlflow()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
