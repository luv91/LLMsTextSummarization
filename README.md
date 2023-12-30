## Text Summarization with Deployment

## Workflow

1. Update config.yaml
2. Update params.yaml

### Done for Data ingestion, data validation, data transformation,
### model trainer and model evaluation. 
3. Update entity ( updating __init__.py in entity folder inside src/TextSummarization for each of DataIngestion, DataValidation, DataTransformation, ModelTrainer and ModelEvaluation )

4. Update the configuration manager (in configuration.py) in src config folder
5. Update the components
     * Creating .py files for data ingestion, data validation, data transformation, model trainer, model evaluation

6. Update the pipeline in the (01_data_ingestion.ipynb, later in data_ingestion.py). 
    * Similarly done for all components of the pipeline

7. Update the main.py
8. Update the app.py

