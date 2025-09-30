# GoSprout_AI_Agent

Easily connect to OpenAI using a Flask API server and a browser-based interface.

![GoSprout_AI_Agent Screenshot](https://github.com/user-attachments/assets/2a3b539d-e5b0-4f07-aabd-7f18e4200e14)

## Prerequisites

- **Python** (Download from [python.org](https://www.python.org/downloads/))
- **OpenAI Account** ([Sign up here](https://platform.openai.com/signup))
- **OpenAI API Key** and **Assistant ID**

## Setup Instructions

1. **Clone this repository** and open it in your IDE (e.g., VS Code).
2. When prompted, create a `.venv` (virtual environment) for Python libraries to avoid global conflicts.
3. **Install required libraries** in your terminal:
    ```bash
    pip install beautifulsoup4 requests pandas
    pip install openai --upgrade
    pip install python-dotenv
    pip install flask-cors
    ```
4. **Create a `.env` file** in the project root with:
    ```
    OPENAI_API_KEY=Your_API_Key
    ASSISTANT_ID=Your_Assistant_ID
    ```
5. **Generate a `.gitignore` file**:
    ```bash
    python environment.py
    ```
6. **Start the Flask server**:
    ```bash
    python app.py
    ```
7. **Access the chatbot** in your browser at [http://127.0.0.1:5000/chatbot](http://127.0.0.1:5000/chatbot)

## Alternative: Run Locally in IDE

You can also use `main.py` to interact with your OpenAI Assistant directly:
```bash
python main.py
```

## Node.js Integration

A sample Node.js file, `runOpenAI.js`, demonstrates Python integration:
```bash
node runOpenAI.js
```

---

**Tip:** Install Python and all required libraries before starting!  
Get started and explore OpenAI with GoSprout_AI_Agent! 😎


