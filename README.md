# GoSprout_AI_Agent
Create a project for GoSprout to access OpenAI
![image](https://github.com/user-attachments/assets/2a3b539d-e5b0-4f07-aabd-7f18e4200e14)

Use Flask API server and HTML browser to connect and access openAI 🔥🔥🔥🔥
<p></p>
<p><strong>Download Instructions and Prerequisites</strong></p>
<p></p>
<p>Download Python</p>
<p></p>
<p>Need API Key</p>
<p></p>
<p>Need OpenAI Account and create an Assistant</p>
<p></p>
<p>Will need the ID of the Assistant</p>
<p></p>

<p><strong>Note:</strong> Once you start adding the Python Libraries mentioned below you will be asked to install the libraries on your IDE (VScode) instead of globally to avoid conflicts. Please say allow and pick a version to create a .venv for your Python Libraries</p>
<p></p>
<p>Recommend creating a project folder first (can right-click and create a folder inside your desktop) to clone your GitHub repo into. Make sure to create the .venv inside the project folder first (VScode will create one for you once you start installing the Python libraries in the terminal assuming you downloaded Python already), then continue installing the other Python libraries once the .venv is created</p>
<p>Next is to CD inside the Github repo project and get started</p>
</br>
<p><strong>The goal is to avoid pushing the .venv Python libraries into the project.</strong></p>
<p></p>
<p></p>
</br>
<p><strong>Python libraries you need to install inside your terminal</strong></p>
<p></p>
<p>pip install beautifulsoup4 requests pandas</p>
<p></p>
<p>pip install openai --upgrade</p>
<p></p>
<p>pip install python-dotenv</p>
<p></p>
<p>pip install flask-cors</p>
<p></p>
<p><strong>Instructions to set up environment and start server</strong></p>
<p></p>
<p>Run python environment.py to create .gitignore file</p>
<p></p>
<p>Create .env file in the root of the project folder</p>
<p></p>
<p>Inside .env file use environment variables:
<p>OPENAI_API_KEY=Your_API_Key</p>
<p>ASSISTANT_ID=Your_Assistant_ID</p></p>
<p>Run python app.py in the terminal to start server</p>
<p></p>
<p>copy paste in the browser http://127.0.0.1:5000/chatbot to use OpenAI</p>
<p></p>
<p>Get started!!😎 </p>

or

<p></p>
You can also just use <strong>main.py</strong> file so you can utilize and access your OpenAI Assistant locally on your machine inside your IDE by running the file in the terminal: python main.py
<p></p>
<p><strong>Recommend you install the Python and Python libraries mentioned above before you get started‼️</strong></p>
<p></p>
<p>I also have a node js file called <strong></strong>runOpenAI.js</strong> that utilizes the main.py file as well. I was doing a side project to see if you can integrate Python into Node.js</p>
<p>Just go into the terminal and type: node runOpenAI.js</p>


