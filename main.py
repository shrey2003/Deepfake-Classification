from deepfakeclassification import logger
from deepfakeclassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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

STAGE_NAME_1 = "Prepare Base Model Stage"

try:
    logger.info(f">>>>>> Starting {STAGE_NAME_1} <<<<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Completed {STAGE_NAME_1} <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e

