from sensors.motion import read_motion
from sensors.light import read_light
from sensors.temperature import read_temperature

from analysis.risk_rules import rule_based_risk
from analysis.anomaly_detector import compute_anomaly
from analysis.ai_explainer import generate_explanation

import json, os
from datetime import datetime

def run():
    # 1) 센서값 읽기
    motion = read_motion()
    light = read_light()
    t = read_temperature()

    today_data = {
        "motion": motion,
        "light": light,
        "temperature": t["temp"],
        "humidity": t["humidity"]
    }

    # 2) 규칙 기반 위험도
    rule_risk = rule_based_risk(
        motion,
        light,
        t["temp"],
        t["humidity"]
    )

    # 3) 평균 대비 이상 탐지
    anomaly_risk = compute_anomaly(today_data)

    # 4) 최종 위험 점수
    final_risk = min(rule_risk + anomaly_risk, 100)

    today_data["risk_score"] = final_risk

    # 5) AI 설명 생성
    today_data["ai_summary"] = generate_explanation(today_data)

    # 6) 저장
    json_path = os.path.join("data", "daily.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(today_data, f, indent=4, ensure_ascii=False)

    # 7) history 저장
    history_path = f"data/history/{datetime.now().strftime('%Y%m%d')}.json"
    os.makedirs("data/history", exist_ok=True)
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(today_data, f, indent=4, ensure_ascii=False)

    print("Saved:", today_data)


if __name__ == "__main__":
    run()
