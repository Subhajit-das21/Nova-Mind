from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Configure Google AI Gemini model
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model with specific configuration
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
    system_instruction="You are an expert at everything. Include examples and short sentences to make the conversation interesting and interactive."
)

# History to maintain conversation context
history = []

# Route to serve the home page
@app.route('/home')
def home():
    return render_template('home.html')

# Route to serve the chatbot HTML page
@app.route('/')
@app.route('/chatbot')
def index():
    return render_template('chatbot.html')

# Route to handle user input (text or voice) and return the bot response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')
    
    # Start the chat session with the model
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    # Update the conversation history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})

    return jsonify({'response': model_response})

if __name__ == '__main__':
    app.run(debug=True)
