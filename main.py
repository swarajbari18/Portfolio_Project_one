from portfolio_project_one import logger
# One very odd question may arise to mind tht why did we not import it like 
# from src.portfolio_project_one
# mentioning src was not necesarry because we pip installed the project_porfolio_one as a library when we wrote our setup.py and ran -e . 
# and ran -e . in our requirements.txt

logger.info("WELCOME TO OUR CUSTOM PROJECT")

from portfolio_project_one.pipeline.step1_data_ingestion import run_data_ingestion

run_data_ingestion()  # run data ingestion pipeline