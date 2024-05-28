import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Initialize the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=os.getenv("HF_TOKEN"))
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=os.getenv("HF_TOKEN"))

def translate(text: str, source_lang: str, target_lang: str) -> str:
    """
    Translate the given text from the source language to the target language.

    Args:
        text (str): The text to translate.
        source_lang (str): The source language code (BCP-47).
        target_lang (str): The target language code (BCP-47).

    Returns:
        str: The translated text.
    """
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt")

    # Generate the translation
    translated_tokens = model.generate(
        **inputs, forced_bos_token_id=tokenizer.lang_code_to_id[target_lang], max_length=30
    )

    # Decode the translated tokens
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

    return translated_text
