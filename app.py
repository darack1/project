from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None
    error = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()

        if not prompt:
            error = "Поле не может быть пустым"
        else:
            try:
                response = requests.post(
                    "https://api.bluesminds.com/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {os.getenv('BLUESMINDS_API_KEY')}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "claude-sonnet-4-6",
                        "max_tokens": 300,
                        "messages": [
                            {"role": "user", "content": prompt}
                        ]
                    }
                )

                response.raise_for_status()
                data = response.json()

                response_text = data["choices"][0]["message"]["content"]

            except Exception as e:
                error = f"Ошибка: {str(e)}"

    return render_template(
        "index.html",
        response_text=response_text,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))