from flask import Flask, render_template
import json
import os
import sys

# analysis 폴더 경로 추가
sys.path.append(os.path.abspath(".."))

from analysis.ai_explainer import generate_explanation   # ← 함수 이름 맞게 변경

app = Flask(__name__)

@app.route("/")
def index():
    json_path = os.path.join("..", "data", "daily.json")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # AI 분석 실행
    ai_summary = generate_explanation(data)

    return render_template(
        "index.html",
        data=data,
        ai_summary=ai_summary
    )

if __name__ == "__main__":
    app.run(debug=True)
