from portfolio_project_one.config.configuration import ConfigurationManager
from portfolio_project_one.components.model_trainer import ModelTrainer
from portfolio_project_one import logger

STEP_NAME = '04 ---- Model Training Step'


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config= model_trainer_config)
        model_trainer.train()


def run_model_trainer():

    try:
        logger.info(f' >>>>>>> Step {STEP_NAME} started <<<<<<<<<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f' >>>>>>> Step {STEP_NAME} completed <<<<<<<<<<<\n\nx====================x')

    except Exception as e:
            logger.exception(e)
            raise e