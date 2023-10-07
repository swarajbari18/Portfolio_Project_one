from portfolio_project_one.constants import *
from portfolio_project_one.utils.common import read_yaml, create_directories

from portfolio_project_one.entity.config_entity import DataIngestionConfig



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