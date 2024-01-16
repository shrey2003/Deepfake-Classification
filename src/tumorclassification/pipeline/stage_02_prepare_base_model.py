from tumorclassification.config.configuration import ConfigurationManager
from tumorclassification.components.prepare_base_model import PrepareBaseModel 
from tumorclassification import logger
import os

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            if not os.path.exists(prepare_base_model_config['base_model_path']):
                prepare_base_model.get_base_model()
                prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Starting {STAGE_NAME} <<<<<<")
        obj= PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Completed {STAGE_NAME} <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e