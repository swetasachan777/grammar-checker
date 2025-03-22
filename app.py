from flask import Flask, request, jsonify
from grammar_checker import GrammarChecker

# Initialize Flask app
app = Flask(_name_)

# Load the grammar checker model
checker = GrammarChecker()

@app.route("/", methods=["GET"])
def home():
    return "Grammar Checker API is running!", 200

@app.route("/correct", methods=["POST"])
def correct():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    corrected_text = checker.correct_text(text)

    return jsonify({"corrected_text": corrected_text})

if _name_ == "_main_":
    app.run(debug=True)