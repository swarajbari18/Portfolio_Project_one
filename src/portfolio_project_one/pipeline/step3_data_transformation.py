from portfolio_project_one.config.configuration import ConfigurationManager
from portfolio_project_one.components.data_transformation import DataTransformtion
from portfolio_project_one import logger
from portfolio_project_one.config.configuration import ConfigurationManager


STEP_NAME = '03 ---- Data Transformation Step'



class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
    
    def check_validation(self, config_manager: ConfigurationManager=ConfigurationManager):
        
        config = config_manager().config.data_validation
        status_file_path = config.STATUS_FILE
        try:
            with open(status_file_path) as f:
                data = f.read()
                status = data.strip().split()[-1]
            return status
        except Exception as e:
            logger.exception(e)
            raise(e)      




    def main(self):
        
        status = self.check_validation()

        if status == 'True':
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformtion(config= data_transformation_config)
            data_transformation.train_test_split() # at default random state is None and test_size is 20 percent

        else:
            logger.info("Data not Validated")
            raise Exception("Your data is not validated")



def run_data_transformation():
    try:
        logger.info(f' >>>>>>> Step {STEP_NAME} started <<<<<<<<<<<')
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f' >>>>>>> Step {STEP_NAME} completed <<<<<<<<<<<\n\nx====================x')

    except Exception as e:
            logger.exception(e)
            raise e
