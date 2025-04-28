from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
