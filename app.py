from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3.2')

# Task prompts mapping
TASK_PROMPTS = {
    'summarize': 'Summarize the following text concisely:\n\n',
    'translate': 'Translate the following text to French:\n\n',
    'explain': 'Explain the following like I\'m 5 years old:\n\n',
    'keywords': 'Extract the main keywords from the following text. List them separated by commas:\n\n',
    'code': 'Generate Python code for the following request:\n\n'
}


def call_ollama(prompt):
    """Call Ollama local API"""
    try:
        url = f"{OLLAMA_BASE_URL}/api/generate"
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()['response']
    except Exception as e:
        return f"Error calling Ollama API: {str(e)}"


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    """Process the user's request"""
    data = request.json
    user_text = data.get('text', '').strip()
    task = data.get('task', '')
    
    if not user_text:
        return jsonify({'error': 'Please enter some text'}), 400
    
    if task not in TASK_PROMPTS:
        return jsonify({'error': 'Invalid task'}), 400
    
    # Create the full prompt
    prompt = TASK_PROMPTS[task] + user_text
    
    # Call Ollama
    result = call_ollama(prompt)
    
    return jsonify({'result': result})


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'provider': 'Ollama',
        'model': OLLAMA_MODEL
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
