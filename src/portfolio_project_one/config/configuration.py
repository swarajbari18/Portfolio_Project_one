from portfolio_project_one.constants import *
from portfolio_project_one.utils.common import read_yaml, create_directories

from portfolio_project_one.entity.config_entity import (DataIngestionConfig,
                                                        DataValidationConfig, 
                                                        DataTransformationConfig, 
                                                        ModelTrainerConfig,
                                                        ModelEvaluationConfig) 



class ConfigurationManager:                  
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,                     # These were all defined in constants
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifact_root])



    def get_data_ingestion_config(self) -> DataIngestionConfig:   # return type is the entity we created

        config = self.config.data_ingestion

        create_directories([config.root_dir])     # we did define the root directory but i never had such a directory,  this is solved here

        data_ingestion_configuration = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_configuration
    
    def get_data_validated_config(self) -> DataValidationConfig:                    # only copy this function to Configuration Manager# kyuki upar ka function toh same hi hai
        config = self.config.data_validation                                        # kyuki upar ka function toh same hi ha
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            unzipped_data_dir = config.unzipped_data_dir,
            all_schema = schema
        )

        return data_validation_config
    


    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation
        
        parameters = self.params.data_transformation
        
        create_directories([config.root_dir])

        data_transformation_configuration = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            test_size= parameters.test_size,
            random_state= parameters.random_state
        )

        return data_transformation_configuration
    


    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            alpha= params.alpha,
            l1_ratio= params.l1_ratio,
            target_column= schema.name
        )

        return model_trainer_config
    

    def get_model_evaluation_configuration(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            model_path= config.model_path,
            all_params= params,
            metric_file_name= config.metric_file_name,
            target_column= schema.name,
            mlflow_uri= "https://dagshub.com/swarajbari18/Portfolio_Project_one.mlflow"
        )
        return model_evaluation_config