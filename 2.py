from flask import Flask, render_template, request
from openai import OpenAI

def get_api_key():
  with open('openai_key.txt', 'r') as f:
    return f.read().strip()

client = OpenAI(api_key=get_api_key())

messages = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    assistant_response = ""

    if request.method == 'POST':

        user_prompt = request.form.get('prompt')

        messages.append({"role": "user", "content": user_prompt})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        assistant_response = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_response})

    return render_template('2.html', response=assistant_response)


if __name__ == '__main__':
    app.run(debug=True)