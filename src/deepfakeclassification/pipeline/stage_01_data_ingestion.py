from deepfakeclassification.config.configuration import ConfigurationManager
from deepfakeclassification.components.data_ingestion import DataIngestion
from deepfakeclassification import logger
import os

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        if(os.path.exists(data_ingestion_config.unzip_dir)):
            logger.info(f"Data already exists in {data_ingestion_config.unzip_dir} and hence skipping data download")
        else:
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e