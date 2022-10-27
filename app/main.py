import os
from dotenv_vault import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
  hello = os.getenv("HELLO")
  return f"<p>Hello, {hello}!</p>"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8000)