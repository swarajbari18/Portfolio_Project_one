from portfolio_project_one.config.configuration import ConfigurationManager
from portfolio_project_one.components.data_validation import DataValidation
from portfolio_project_one import logger

STEP_NAME = '02 ---- Data Validation Step'


class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validated_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_columns()


def run_data_validation():

    try:
        logger.info(f' >>>>>>> Step {STEP_NAME} started <<<<<<<<<<<')
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f' >>>>>>> Step {STEP_NAME} completed <<<<<<<<<<<\n\nx====================x')

    except Exception as e:
            logger.exception(e)
            raise e