# app.py
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    # data.json 읽기
    json_path = os.path.join(os.path.dirname(__file__), "..", "4_data", "daily.json")
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
