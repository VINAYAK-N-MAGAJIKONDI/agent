from deep_translator import GoogleTranslator

def translate_prompt_to_english(prompt: str) -> str:
    return GoogleTranslator(source='auto', target='en').translate(prompt)
