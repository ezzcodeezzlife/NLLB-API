from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from translation_service import translate, tokenizer
import os

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

class TranslationResponse(BaseModel):
    translated_text: str

@app.post("/translate", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    try:
        translated_text = translate(request.text, request.source_lang, request.target_lang)
        return TranslationResponse(translated_text=translated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
def read_index():
    with open(os.path.join(os.path.dirname(__file__), "index.html"), "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/languages")
def get_languages():
    """
    Get the list of supported languages.

    Returns:
        dict: A dictionary with language codes as keys and language names as values.
    """
    return tokenizer.lang_code_to_id
