from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
app.secret_key = "change-me-in-production"  # needed for Flask session

# --- Chatbot logic & memory helpers ---
RESPONSES = {
    "greet": ["Hello! 👋 How can I help you today?", "Hi there! 😊 How are you?"],
    "how_are_you": ["I'm just a bot, but I'm doing great! 🤖 How about you?"],
    "name": ["I'm MiniBot, your little AI friend! 🤖"],
    "bye": ["Goodbye! Have a great day! 👋", "See you later! ✨"]
}

KEYWORDS = {
    "hi": "greet",
    "hello": "greet",
    "hey": "greet",
    "how are you": "how_are_you",
    "your name": "name",
    "who are you": "name",
    "bye": "bye",
    "goodbye": "bye"
}

def get_memory():
    if "memory" not in session:
        session["memory"] = {"name": None, "mood": None}
    return session["memory"]

def set_memory(key, value):
    mem = get_memory()
    mem[key] = value
    session["memory"] = mem

def get_bot_response(user_input: str) -> str:
    ui = user_input.lower().strip()
    mem = get_memory()

    # Learn user's name
    if "my name is" in ui:
        name = ui.split("my name is", 1)[-1].strip().split()[0].capitalize()
        set_memory("name", name)
        return f"Nice to meet you, {name}! 😊"

    # Learn mood (very simple extractor)
    if "i am " in ui or "i'm " in ui:
        tokens = ui.replace("i'm", "i am").split()
        for w in ["happy", "sad", "good", "tired", "angry", "great", "excited", "stressed"]:
            if w in tokens:
                set_memory("mood", w)
                return f"Thanks for sharing. Noted you're feeling {w}. 🌟"

    # Context-aware greeting
    if any(g in ui for g in ["hi", "hello", "hey"]):
        if mem.get("name"):
            return f"Hello {mem['name']}! 👋 How’s your day going?"
        return random.choice(RESPONSES["greet"])

    # Recall mood
    if "how am i" in ui and mem.get("mood"):
        return f"You told me you're feeling {mem['mood']} earlier. 😊"

    # Keyword-based answers
    for k, tag in KEYWORDS.items():
        if k in ui:
            return random.choice(RESPONSES[tag])

    return "I'm not sure how to answer that. Can you ask something else? 🤔"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_msg = data.get("message", "")
    reply = get_bot_response(user_msg)
    # if user says bye, optionally clear session memory
    if "bye" in user_msg.lower():
        session.pop("memory", None)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
