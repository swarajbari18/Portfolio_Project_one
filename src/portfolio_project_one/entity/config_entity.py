from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)      # you don't have to give self in a dataclass CLASS
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzipped_data_dir: Path
    all_schema: dict