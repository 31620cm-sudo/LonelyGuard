def rule_based_risk(motion, light, temp, humidity):
    risk = 0

    # 1) 활동량 감소
    if motion < 3:
        risk += 30

    # 2) 조명 변화 없음
    if light == 0:
        risk += 20

    # 3) 온도 이상
    if temp < 18 or temp > 30:
        risk += 20

    # 4) 습도 이상
    if humidity < 30 or humidity > 70:
        risk += 10

    return min(risk, 100)
