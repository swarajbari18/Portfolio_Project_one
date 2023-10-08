import os
from portfolio_project_one import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from portfolio_project_one.entity.config_entity import DataTransformationConfig 


class DataTransformtion:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    def train_test_split(self):
        df = pd.read_csv(self.config.data_path)
        # print(df)
        train_set, test_set = train_test_split(df,test_size= self.config.test_size, random_state= self.config.random_state)
        train_set.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = False)
        test_set.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False)

        logger.info("Splitted data into training and test datasets")
        logger.info(f' Training dataset shape:  {train_set.shape}')
        logger.info(f' Testing dataset shape:  {test_set.shape}')

        print(f' Training dataset shape:  {train_set.shape}. \n Testing dataset shape:  {test_set.shape}')