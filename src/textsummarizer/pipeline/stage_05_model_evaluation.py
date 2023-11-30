
from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.model_evaluation import ModelEvaluation
from textsummarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config= ConfigurationManager()
        model_trainer_config= config.get_model_evaluation_config()
        model_trainer_config= ModelEvaluation(config= model_trainer_config)
        model_trainer_config.train()