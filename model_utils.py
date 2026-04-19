#gemini
import json
import os
from transformers import pipeline
import google.generativeai as genai

# ---------------- CLASSIFICATION ----------------
classifier = pipeline("text-classification", model="./fine_tuned_model")

with open("label_map.json") as f:
    label_map = json.load(f)

def classify_email(text):
    result = classifier(text)[0]
    label_index = int(result['label'].split("_")[-1])
    category = label_map[str(label_index)]
    confidence = round(result['score'], 2)
    return category, confidence


# ---------------- SENTIMENT ----------------
def analyze_sentiment(text):
    text = text.lower()
    if "not" in text or "issue" in text or "problem" in text:
        return "NEGATIVE"
    return "POSITIVE"


# ---------------- GEMINI SETUP ----------------
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None


# ---------------- RESPONSE ----------------
def generate_response(email_text, category, context):

    if model is None:
        return f"Your issue is categorized as '{category}'. Our support team will assist you."

    prompt = f"""
    You are a professional customer support assistant.

    Category: {category}

    Customer Email:
    {email_text}

    Context:
    {context}

    Give a helpful response.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return f"Your issue '{category}' is noted. Our team will assist you shortly."