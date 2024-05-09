# basic flask app

from flask import Flask, render_template, url_for, request, jsonify, redirect
import os

# Getting Gemini API key from environment
API_KEY = os.environ.get("API_KEY") 

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        # return "Page under construction"
        return redirect('/generate-text')
    
    return render_template('index.html')

@app.route('/generate-text', methods = ['POST'])
def generate_text():
	# Get the user query from the request
	user_query = request.json.get('query')

	# Check if query is present
	if not user_query:
		return jsonify({'error': 'Missing query parameter'}), 400

	# Prepare the API request data
	request_data = {
			'contents': [{'parts': [{'text': user_query}]}]
	}

	# Import libraries only when needed (improves startup speed)
	import requests

	# Send the API request using requests library
	response = requests.post(
			"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY,
			json=request_data)

	# Handle response status code (basic implementation)
	if response.status_code == 200:
		# Parse the response (assuming successful response)
		generated_text = response.json()['generations'][0]['text']
		return jsonify({'generated_text': generated_text})
	else:
		return jsonify({'error': 'API request failed'}), response.status_code

if __name__=='__main__':
    app.run(debug=True)