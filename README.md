# NLLB FastAPI Translation Service

## Introduction
This project sets up a FastAPI service that uses the NLLB-200-Distilled model for translation requests. The service allows users to translate text between different languages using a RESTful API.

## Requirements
- Python 3.8 or higher
- pip (Python package installer)
- Hugging Face token (for accessing the NLLB-200-Distilled model)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/facebookresearch/fairseq.git
    cd fairseq
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install --editable ./
    pip install fastapi uvicorn transformers
    ```

4. Download the NLLB-200-Distilled model:
    ```bash
    wget https://tinyurl.com/nllb200densedst600mcheckpoint -O checkpoint.pt
    ```

## Usage
1. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

2. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

3. The server will be running at `http://127.0.0.1:8000`. You can access the translation endpoint at `http://127.0.0.1:8000/translate`.

## Endpoint Description
### POST /translate
- **Description**: Translates the given text from the source language to the target language.
- **Request Body**:
    ```json
    {
        "text": "Hello, world!",
        "source_lang": "eng_Latn",
        "target_lang": "fra_Latn"
    }
    ```
- **Response**:
    ```json
    {
        "translated_text": "Bonjour, le monde!"
    }
    ```

## Troubleshooting
- Ensure that the Hugging Face token is provided when initializing the tokenizer and model.
- If you encounter any issues with missing dependencies, make sure to install them using `pip install <dependency_name>`.
- For any other issues, refer to the official documentation of the libraries used in this project.
