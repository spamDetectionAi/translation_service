from flask import Flask, request, jsonify
from translator_service import translate_text
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    lang = data.get('lang')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    translated = translate_text(text, lang)
    return translated
print("Script is starting...")



if __name__ == '__main__':
    print("Main block is executing...")
    app.run(host='0.0.0.0', port=5001, debug=True)
    print("This line won't print until the server stops")
else:
    print(f"Script is being imported as: {__name__}")