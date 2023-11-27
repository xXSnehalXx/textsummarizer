import os
from textsummarizer.logging import logger
from textsummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config= config
    ##IN THIS STEP YOU CAN ALSO CHECK FOR DATA TYPE COLUMN VERIFICATION AND STUFF
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status= None
            all_files= os.listdir(os.path.join("artifacts","data_ingestion","samsumdata","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status= False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status= True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")

            return validation_status
            
        except Exception as e:
            raise e
         
