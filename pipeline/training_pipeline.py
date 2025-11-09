from utils.common_function import *
from config.paths_config import *
from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining


if __name__ == "__main__":
    ## Data Ingestion
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ## Data Processing
    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()

    ## Model Training
    model_trainer = ModelTraining(train_path=PROCESSED_TRAIN_DATA_PATH,
                                  test_path=PROCESSED_TEST_DATA_PATH,
                                  model_output_path=MODEL_OUTPUT_PATH)
    model_trainer.run()