from fastapi import FastAPI
from pydantic import BaseModel

from model_utils import classify_email, analyze_sentiment, generate_response
from rag import retrieve_context

app = FastAPI()

MODEL_VERSION = "v2.1"

# ---------------- REQUEST SCHEMA ----------------
class EmailRequest(BaseModel):
    text: str


# ---------------- HEALTH CHECK ----------------
@app.get("/")
def home():
    return {"message": "API is running 🚀"}


# ---------------- EMAIL ANALYSIS ----------------
@app.post("/analyze-email")
def analyze_email(req: EmailRequest):

    # Step 1: Classification
    category, confidence = classify_email(req.text)

    # Step 2: Sentiment
    sentiment = analyze_sentiment(req.text)

    # Step 3: RAG Context Retrieval
    context = retrieve_context(req.text)

    # Step 4: Confidence-based Routing
    if confidence < 0.6:
        response = "Escalated to human agent due to low confidence."
    else:
        response = generate_response(req.text, category, context)

    return {
        "category": category,
        "confidence": confidence,
        "sentiment": sentiment,
        "context": context,  # optional but good for debugging/demo
        "response": response,
        "model_version": MODEL_VERSION
    }


# ---------------- CHATBOT (RAG) ----------------
@app.post("/chat")
def chat(req: EmailRequest):

    context = retrieve_context(req.text)

    # Optional: use same generator for better answer
    answer = generate_response(req.text, "General Query", context)

    return {
        "question": req.text,
        "context": context,
        "answer": answer
    }