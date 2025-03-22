import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Define the model path (update if needed)
MODEL_PATH = "grammar_corrector_model"

class GrammarChecker:
    """Grammar correction using a trained T5 model."""
    
    def _init_(self, model_path=MODEL_PATH):
        try:
            self.tokenizer = T5Tokenizer.from_pretrained(model_path)
            self.model = T5ForConditionalGeneration.from_pretrained(model_path)
            print("✅ Model loaded successfully!")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            self.tokenizer = None
            self.model = None

    def correct_text(self, text):
        """Corrects the grammar of the input text using the model."""
        if not self.model or not self.tokenizer:
            return "Model not loaded properly!"

        input_text = f"fix grammar: {text}"
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)

        with torch.no_grad():
            outputs = self.model.generate(inputs, max_length=256)

        corrected_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return corrected_text

if __name__ == "_main_":
    checker = GrammarChecker()
    
    # Sample sentences to test
    test_sentences = [
        "She go to school every day.",
        "He have a two cat.",
        "Their is a big problem in the system.",
        "This are not correct."
    ]

    for sentence in test_sentences:
        corrected = checker.correct_text(sentence)
        print(f"❌ Original: {sentence}")
        print(f"✅ Corrected: {corrected}\n")
