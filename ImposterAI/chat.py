# GPTMixTape/ImposterAI/chat.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from SecureKeys import gpt_api_key
from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__, template_folder='my_templates')

with open("API_KEY") as f:
    file_contents = f.read()

print(file_contents)
os.environ["OPENAI_API_KEY"] = file_contents

# Set up OpenAI API credentials
openai.api_key = gpt_api_key #os.environ["OPENAI_API_KEY"]

# Define a function to generate a response from OpenAI's GPT
def generate_response(prompt):
    message = "Respond as if you were persistently and intently flirting with me. "+ prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": message},
        ]
    )
    message = response.choices[0].message.content
    return message

# Define the home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = generate_response(prompt)
        return render_template("index.html", prompt=prompt, response=response)
    else:
        return render_template("index.html")

# Start the app
if __name__ == "__main__":
    app.run(debug=True)
