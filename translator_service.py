from deep_translator import GoogleTranslator

def translate_text(text, dest_language):
    translator = GoogleTranslator(source='auto', target=dest_language)
    translated = translator.translate(text)
    return translated

print(translate_text("Hello, how are you?", "fr"))  # Example usage