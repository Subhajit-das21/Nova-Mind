import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



# Create the model
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
  system_instruction="You are an expert at creating a difficult MCQ based physics test. Do not include answer key at the end. "
  )

history=[]

def chat():
    print("Welcome to the MCQ based Physics test for highschool students preparing for competitive examination.")
    print()
    print("If you want subjective questions please refer to the different tile of examination.")
    print()
    print("Introduce yourself to Anweshan, your AI assistant.")
    print()
    while True: 
        user_input=input("You: ")
        print()
        chat_session = model.start_chat(history=history)

        response = chat_session.send_message(user_input)
        model_response=response.text

        print("Anweshan: ",model_response)
        print()

        history.append({"role":"user","parts":[user_input]})
        history.append({"role":"model","parts":[model_response]})
                        
chat()