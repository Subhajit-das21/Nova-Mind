from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Configure Google AI Gemini model
genai.configure(api_key=os.getenv("AIzaSyBqGHEdm2QQfmVb_Q2jncMtVR1UfO8cqIc"))

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
    system_instruction="You are an expert at everything. A champ 🏆."
)

# History to maintain conversation context
history = []

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the account page without the .html
@app.route('/account')
def account():
    return render_template('account.html')

# Route for the resources page without the .html
@app.route('/resources')
def resources():
    return render_template('resources.html')

# Route for the chatbot page without the .html
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Route for the contact page without the .html
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the signup page without the .html
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route for the signup page without the .html
@app.route('/faq')
def faq():
    return render_template('faq.htm')
# Route for the signup page without the .html
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
# Route for the signup page without the .html
@app.route('/termsandconditions')
def termsandconditions():
    return render_template('termsandconditions.html')

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
