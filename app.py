from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Configure Google AI Gemini model
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use .env variable safely

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are an expert at everything. A champ 🏆."
)

# Maintain conversation history
history = []

# --------------------- ROUTES ---------------------

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<page>')
@app.route('/<page>.html')
def render_page(page):
    """ Dynamically render pages to support both '/page' and '/page.html' """
    try:
        return render_template(f"{page}.html")
    except:
        return "Page not found", 404

# 🧠 Handle AI chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')

    # Start chat session
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    # Update chat history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})

    return jsonify({'response': model_response})

# -------------------- MAIN --------------------
if __name__ == '__main__':
    app.run(debug=True)
