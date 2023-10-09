from portfolio_project_one.config.configuration import ConfigurationManager
from portfolio_project_one.components.model_evaluator import ModelEvaluation
from portfolio_project_one import logger

STEP_NAME = '05 ---- Model Evaluation Step'


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_configuration()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.log_metrics_to_mlflow()


def run_model_evaluator():

    try:
        logger.info(f' >>>>>>> Step {STEP_NAME} started <<<<<<<<<<<')
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f' >>>>>>> Step {STEP_NAME} completed <<<<<<<<<<<\n\nx====================x')

    except Exception as e:
            logger.exception(e)
            raise e