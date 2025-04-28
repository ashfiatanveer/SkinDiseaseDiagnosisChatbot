# 🩺 Skin Disease Diagnosis and Care Chatbot
DermaAI is an AI-powered chatbot designed to assist users in identifying common skin diseases and providing caring, informative advice.
It combines powerful machine learning models to create a natural, friendly interaction experience for users seeking basic dermatological guidance.

# Project Overview
This project brings together:

Disease Classification ➔ A fine-tuned Roberta/Resnet model predicts the skin condition based on user-described symptoms

Conversational Care ➔ A medical language model (LLM) generates a compassionate, patient-friendly response based on the diagnosis and user's description.

# How It Works

User describes symptoms, either through text or image (e.g., "I have red itchy skin with small bumps.")

Roberta/Resnet model classifies the disease (e.g., "eczema").

LLM chatbot crafts a warm, informative, easy-to-understand care message for the user.

# Technologies Used

Roberta (fine-tuned) — for disease classification

Llama 3.1 MedPalm2 Imitate 8B — for chatbot replies (quantized GGUF model)

llama-cpp-python — lightweight inference of Llama models

PyTorch — deep learning framework

Transformers (HuggingFace) — for model management

Kaggle GPU environment — for faster runtime

# Getting Started

1. Clone the repository:

git clone https://github.com/ashfiatanveer/SkinDiseaseDiagnosisChatbot.git

cd SkinDiseaseDiagnosisChatbot

2. Install dependencies:

pip install torch transformers llama-cpp-python

3. Upload your trained Roberta model and GGUF chatbot model in your environment.

4. Run the chatbot script or notebook and start interacting!

