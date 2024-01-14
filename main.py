from tumorclassification import logger
from tumorclassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Welcome to Kidney-Tumor Classification Project")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

