import time
from openai import OpenAI
from dotenv import load_dotenv 
import os

import sys
sys.stdout.reconfigure(encoding='utf-8')


class Run:
    def __init__(self, run_id):
        self.id = run_id


        print(f"\U0001f449 Run Created: {run.id}")

# pip install beautifulsoup4 requests pandas

# pip install openai --upgrade

# pip install python-dotenv


# Load environment variables from the .env file
load_dotenv()

# Now you can access the environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Use the environment variable in your script
client = OpenAI(api_key=OPENAI_API_KEY)

# Enter your Assistant ID here.
ASSISTANT_ID = "asst_VHUsedert1fAmMqSubO31QRf"


# Create a thread with a message.
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            # Update this with the query you want to use.
            "content": "5 * 5 + 15",
        }
    ]
)

# Submit the thread to the assistant (as a new run).
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
print(f"👉 Run Created: {run.id}")

# Wait for run to complete.
while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"🏃 Run Status: {run.status}")
    time.sleep(1)
else:
    print(f"🏁 Run Completed!")

# Get the latest message from the thread.
message_response = client.beta.threads.messages.list(thread_id=thread.id)
messages = message_response.data

# Print the latest message.
latest_message = messages[0]
print(f"💬 Response: {latest_message.content[0].text.value}")