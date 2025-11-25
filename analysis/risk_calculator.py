# risk_calculator.py

def calculate_risk(motion, light, temp, humidity):
    """
    각 센서 데이터를 기반으로 위험도 점수를 계산.
    알고리즘은 기본 버전이며, 필요하면 확장 가능.
    """
    score = 0

    # 움직임이 거의 없는 경우
    if motion == 0:
        score += 30

    # 조도가 변화가 없는 경우 (어두움)
    if light == 0:
        score += 20

    # 온도가 비정상 범위일 때
    if temp < 15 or temp > 32:
        score += 20

    # 습도가 너무 낮은 경우
    if humidity < 20:
        score += 10

    return score
