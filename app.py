from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# API key
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

if not SARVAM_API_KEY:
    raise ValueError("SARVAM_API_KEY not found in .env file")

headers = {
    "api-subscription-key": SARVAM_API_KEY,
    "Content-Type": "application/json"
}

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "Sarvam AI Flask API running successfully"


# ---------------- TRANSLATE ----------------
@app.route("/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "JSON body required"}), 400

        text = data.get("text")
        source = data.get("source_language", "en-IN")
        target = data.get("target_language", "te-IN")

        payload = {
            "input": text,
            "source_language_code": source,
            "target_language_code": target,
            "model": "mayura:v1",
            "enable_preprocessing": True
        }

        response = requests.post(
            "https://api.sarvam.ai/translate",
            json=payload,
            headers=headers
        )

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- TEXT TO SPEECH ----------------
@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.get_json()
        text = data.get("text")

        payload = {
            "inputs": [text],
            "target_language_code": data.get("language", "te-IN")
        }

        response = requests.post(
            "https://api.sarvam.ai/text-to-speech",
            json=payload,
            headers=headers
        )

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- SPEECH TO TEXT ----------------
@app.route("/stt", methods=["POST"])
def stt():
    try:
        file = request.files.get("file")

        if not file:
            return jsonify({"error": "Audio file required"}), 400

        files = {
            "file": (file.filename, file.stream, file.content_type)
        }

        response = requests.post(
            "https://api.sarvam.ai/speech-to-text",
            files=files,
            headers={"api-subscription-key": SARVAM_API_KEY}
        )

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)