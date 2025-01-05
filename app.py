from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch

# Path to the model weights on your local machine
model_folder = "./model"  # Replace with your local path

# Load the model and tokenizer
distilBert_tokenizer = DistilBertTokenizer.from_pretrained(model_folder)
distilBert_model = DistilBertForSequenceClassification.from_pretrained(model_folder)

# Create the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get message and history from request
        data = request.json
        message = data.get('message', '')
        history = data.get('history', [])

        if not message:
            return jsonify({"error": "Message is required"}), 400

        if history is None:
            history = []

        # Define disease mapping
        disease_mapping = {
            0: 'Vitiligo',
            1: 'Scabies',
            2: 'Hives (Urticaria)',
            3: 'Folliculitis',
            4: 'Ringworm (Tinea Corporis)',
            5: "Athlete's Foot (Tinea Pedis)",
            6: 'Rosacea',
            7: 'Psoriasis',
            8: 'Shingles',
            9: 'Contact Dermatitis',
            10: 'Acne',
            11: 'Eczema',
            12: 'Shingles (Herpes Zoster)',
            13: 'Impetigo'
        }

        # Tokenize and predict
        inputs = distilBert_tokenizer(message, return_tensors="pt")
        outputs = distilBert_model(**inputs)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()
        disease_label = disease_mapping.get(predicted_class, "Unknown Disease")

        # Create a response, without the user message
        response = f"Chatbot: Based on the symptoms you mentioned, it seems you might have {disease_label}."

        # Return only the response and updated history
        return jsonify({"response": response, "history": history + [(message, response)]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
