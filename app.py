from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)  # Yeh React ko block hone se bachayega (No CORS Error)

# Gemini Client Setup (Apni Gemini Key yahan dalo)
client = genai.Client(api_key="YAHAN APNI API KEY DAALO")

@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_msg = data.get('message', '')
        system_prompt = data.get('systemPrompt', '')

        # Gemini API Call with Strict JSON Mode
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"{system_prompt}\n\nUser Request: {user_msg}",
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            ),
        )
        
        return jsonify({"content": response.text})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    app = app
