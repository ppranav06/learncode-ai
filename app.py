# basic flask app

from flask import \
	Flask, render_template, url_for, request, jsonify, redirect
import os
# from IPython.display import display
from IPython.display import Markdown
import textwrap

def to_markdown(text):
	"""Convert normal text to markdown format"""
	text = text.replace('•', '  *')
	md_content = Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
	return md_content.__str__()


# Getting Gemini API key from environment
# API_KEY = os.environ.get("API_KEY") 
import google.generativeai as genai

API_KEY = os.environ.get('API_KEY')
genai.configure(api_key=API_KEY)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
	if request.method == 'POST':
		# Get the user query from the request
		user_query = request.form.get('query')
		return render_template('index.html', display_query=user_query, generated_response=gemini_model_response(user_query))		

	return render_template('index.html')

def gemini_model_response(user_query):
	"""Generate response via the Gemini genai module"""
	
	if not user_query:
		return "Please give query / error with parsing query"

	model = genai.GenerativeModel('gemini-pro')
	response = model.generate_content(user_query)
	return response.text

if __name__=='__main__':
	app.run(debug=True)