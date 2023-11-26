from dataclasses import dataclass
from pathlib import Path

#below is an entity that defines the return type of a function
@dataclass(frozen= True) #(not a python class but a dataclass)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    