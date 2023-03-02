import openai
import os
openai.api_key = "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"


from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"
@app.route('/<prompt>')
def ask(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=550,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    #print(response)
    print(response['choices'][0]['text'])
    return response['choices'][0]['text']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8808)
