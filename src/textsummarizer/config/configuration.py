import textsummarizer.constants.constants as constants
from textsummarizer.utils.common import read_yaml, create_directories
from textsummarizer.entity import (DataIngestionConfig)
from pathlib import Path

class ConfigurationManager:
    def __init__(
            self,
            params_file_path: Path= constants.PARAMS_FILE_PATH,
            config_file_path: Path= constants.CONFIG_FILE_PATH,):
        
        self.config= read_yaml(config_file_path)
        self.params= read_yaml(params_file_path)

        create_directories([self.config.artifacts_root,])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir =  config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        return data_ingestion_config
