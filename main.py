from sensors.motion import read_motion
from sensors.light import read_light
from sensors.temperature import read_temperature
from analysis.risk_calculator import calculate_risk
import json
import os

def run():
    # 센서 값 읽기 (현재는 mock)
    motion = read_motion()
    light = read_light()
    t = read_temperature()

    # 분석
    risk = calculate_risk(
        motion,
        light,
        t["temp"],
        t["humidity"]
    )

    # 데이터 저장
    data = {
        "motion": motion,
        "light": light,
        "temperature": t["temp"],
        "humidity": t["humidity"],
        "risk_score": risk
    }

    # 숫자 제거 후 정식 경로
    json_path = os.path.join("data", "daily.json")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Saved:", data)

if __name__ == "__main__":
    run()
