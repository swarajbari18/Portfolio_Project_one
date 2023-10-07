from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)      # you don't have to give self in a dataclass CLASS
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path