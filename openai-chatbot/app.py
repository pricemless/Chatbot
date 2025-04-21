from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify({"reply": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(debug=True)
