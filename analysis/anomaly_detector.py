import json
import os
import numpy as np

def compute_anomaly(today_data):
    """
    today_data = {
      "motion": ?, "light": ?, "temperature": ?, "humidity": ?
    }
    """

    history_folder = "data/history"
    os.makedirs(history_folder, exist_ok=True)

    # 최근 7일 데이터 읽기
    history_files = [f for f in os.listdir(history_folder) if f.endswith(".json")]

    if len(history_files) < 3:
        return 0  # 데이터 부족 → 이상감지 불가

    motions = []
    lights = []
    temps = []
    hums = []

    for file in history_files:
        with open(os.path.join(history_folder, file), "r", encoding="utf-8") as f:
            d = json.load(f)
            motions.append(d["motion"])
            lights.append(d["light"])
            temps.append(d["temperature"])
            hums.append(d["humidity"])

    # 평균 계산
    avg_motion = np.mean(motions)
    avg_light = np.mean(lights)
    avg_temp = np.mean(temps)
    avg_hum = np.mean(hums)

    diff_score = 0

    # 평균 대비 차이 비율
    diff_score += abs(today_data["motion"] - avg_motion) * 5
    diff_score += abs(today_data["temperature"] - avg_temp) * 2
    diff_score += abs(today_data["humidity"] - avg_hum) * 1

    return min(int(diff_score), 100)
