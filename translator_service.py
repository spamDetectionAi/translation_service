from deep_translator import GoogleTranslator

def translate_text(text, dest_language='en'):
    translator = GoogleTranslator(source='auto', target=dest_language)
    translated = translator.translate(text)
    return translated