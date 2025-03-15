from flask import Flask, request, jsonify
from grammar_checker import GrammarChecker

app = Flask(__name__)
checker = GrammarChecker()

@app.route("/", methods=["GET"])
def home():
    return "Grammar Checker API is running!", 200

@app.route('/correct', methods=['POST'])
def correct():
    data = request.get_json()
    text = data.get("text", "")
    corrected_text = checker.correct_text(text)
    return jsonify({"corrected_text": corrected_text})

if __name__ == "__main__":
    app.run(debug=True)