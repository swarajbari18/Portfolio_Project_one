from portfolio_project_one import logger
# One very odd question may arise to mind tht why did we not import it like 
# from src.portfolio_project_one
# mentioning src was not necesarry because we pip installed the project_porfolio_one as a library when we wrote our setup.py and ran -e . 
# and ran -e . in our requirements.txt

logger.info("Welcome to   SWARAJ BARI' s  Custom End-to-End Project")



from portfolio_project_one.pipeline.step1_data_ingestion import run_data_ingestion
from portfolio_project_one.pipeline.step2_data_validation import run_data_validation
from portfolio_project_one.pipeline.step3_data_transformation import run_data_transformation
from portfolio_project_one.pipeline.step4_model_training import run_model_trainer
from portfolio_project_one.pipeline.step5_model_evaluation import run_model_evaluator




run_data_ingestion()  # run data ingestion pipeline
run_data_validation()  # run data validation pipeline
run_data_transformation()  # run data transformation pipeline
run_model_trainer()  # run model trainer
run_model_evaluator()  # run model evaluation pipeline