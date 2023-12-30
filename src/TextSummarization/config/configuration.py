from TextSummarization.constants import *
from TextSummarization.utils.common import read_yaml, create_directories
from TextSummarization.constants import CONFIG_FILE_PATH
from TextSummarization.entity import DataIngestionConfig

# copy paste the entrie configuraiton Manager from the 01_data_ingestion.ipynb
# CONFIG_FILE_PATH is defined in __init__.py in constants
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)

        # reading params.yaml here. 
        self.params = read_yaml(params_filepath)

        # create_directories is in the common.py inside utils folder
        # artifacts_root is in config.yaml (using Config Box here also)
        create_directories([self.config.artifacts_root])

    # so any changes made in the config.yaml will be reflected here..
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

