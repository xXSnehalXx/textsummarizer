from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from textsummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion= DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed started <<<<\n\nx============x<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_validation= DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed started <<<<\n\nx============x<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_transformation= DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed started <<<<\n\nx============x<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_transformation= ModelTrainerPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed started <<<<\n\nx============x<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_transformation= ModelEvaluationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed started <<<<\n\nx============x<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e