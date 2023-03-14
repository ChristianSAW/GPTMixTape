from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__, template_folder='my_templates')

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to generate a response from OpenAI's GPT
def generate_response(prompt):
    message = "Respond as if you were Samuel L Jackson. "+ prompt
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
