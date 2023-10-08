import os
import pandas as pd

from portfolio_project_one import logger
from portfolio_project_one.entity.config_entity import DataValidationConfig




class DataValidation:

    def __init__(
        self,
        config: DataValidationConfig
    ):
        self.config = config

    def validate_all_columns(self) -> bool:   # this only checks if the column name exits, we can also add validaate datatype
        try:
            validation_status = None

            df = pd.read_csv(self.config.unzipped_data_dir)
            all_columns = list(df.columns)

            all_schema = self.config.all_schema

            for column in all_columns:
                if column not in all_schema.keys():   
                    validation_status = False
                    #  this means we should not go ahead
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'''******{column}******* is an anmoly, its not in schema.yaml, deal with this first then run pipeline again
                                    VALIDATION STATUS:  {validation_status}''')

                        logger.info(f'Validation has failed for column : {column}, Check svhema.yaml, Status File and DataFrame.')
                    break   # break the loop so that we dont go ahead and end up getting a pass status at the end
                    
                elif str(df[column].dtype) == all_schema[column]:       # after or we check for datatype(personal code)
                    validation_status = True                           # column exists and datatype is satisfied
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'''VALIDATION STATUS:  {validation_status}''')
                    logger.info(f'Validation is Succesfull')

                else:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'''******{column}******* is an anmoly, its datatype is a mismatch, deal with this first then run pipeline again
                                    VALIDATION STATUS:  {validation_status}''')

                        logger.info(f'Validation has failed for column : {column}, Check schema.yaml, Status File and DataFrame.')
                    break

            return validation_status

        except Exception as e:
            logger.info(f'Error Occured while Data_Validation')
            raise e