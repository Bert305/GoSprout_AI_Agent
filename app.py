import time
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASSISTANT_ID = os.getenv('assistant_id')
# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire Flask app
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_message = data.get("message", "")
    assistant_id = ASSISTANT_ID

    # Create a thread with the user's message
    thread = client.beta.threads.create(
        messages=[{"role": "user", "content": user_message}]
    )

    # Submit the thread to the assistant (as a new run)
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)
    print(f"👉 Run Created: {run.id}")

    # Wait for the run to complete
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        print(f"🏃 Run Status: {run.status}")
        time.sleep(1)

    # Retrieve the latest message in the thread
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data
    latest_message = messages[0].content[0].text.value if messages else "No response available"

    return jsonify({"response": latest_message})

@app.route('/chatbot')
def home():
    return render_template('index3.html') # Render the HTML file: choose index.html or index2.html

if __name__ == '__main__':
    app.run(debug=True)

