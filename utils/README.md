# AI Lawyer

This project is an AI application capable of writing and editing contracts. It uses Python and TensorFlow.

## Project Structure

- `data/contracts/`: This folder contains the contract data used for training the model.
- `models/`: This folder contains the trained model.
- `src/`: This folder contains the main application code.
  - `main.py`: This is the main entry point of the application.
  - `contract_generator.py`: This file contains the code for generating contracts.
  - `contract_editor.py`: This file contains the code for editing contracts.
- `tests/`: This folder contains the tests for the application.
- `utils/`: This folder contains utility scripts for data preprocessing and model training.
- `requirements.txt`: This file lists the Python dependencies required for this project.

## Setup

1. Install the required dependencies:


pip install -r requirements.txt


2. Run the main application:


python src/main.py


## Testing

To run the tests, use the following command:


python -m unittest discover tests
