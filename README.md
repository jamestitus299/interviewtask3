# Component Genie -- Componet Generation Application with visualization

Component Genie is basically purposed to generate React/html Components, but can also answer other general question. It might return factually wrong responses. User discretion is advised.

# Setup

1. Clone the repository
2. Create a python virtual environment and activate the environment, run below command in the terminal
```
python -m venv .venv
source .venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Set up your API key <GEMINI_API_KEY> (look at the .env.example file)
    Go to https://ai.google.dev/gemini-api/docs and click the Get a Gemini API Key
    Log in using your google account. You will be redirected to the Google AI Studio page 
    Click on Get API Key, and then click on Get API Key, select your Google Cloud project and then your API key will be generated (if you do not have a Google Cloud account, create one and create a new project)
    Copy the API key and save it
5. Create a .env file in the root of the directory and paste the copied API key
```
GEMINI_API_KEY="your_api_key"
```
6. Run your reflex app
```
reflex init
reflex run
```
Access the app at http://localhost:3000 (if you are using a dev container like codespaces be sure to forward the ports)

# Usage examples -- prompts
```
html code for a signup form with dark background and purple button

react code for a login form 
```
The application works great with HTML code, but may give some rendering errors for react code